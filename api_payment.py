import requests
import json
import uuid
import base64
from PIL import Image, ImageTk
from io import BytesIO
import io

class API_PAYMENT:
    def __init__(self):
        self.API_KEY = "l7e87e90a9280d470fb880bf31f18a19ee"
        self.API_SECRET = "3522aee56adc41809e9b9be57a0955e9"
        self.API_URL = "https://api-sandbox.partners.scb/partners/sandbox/v1/oauth/token"
        self.QR_CODE_URL = "https://api-sandbox.partners.scb/partners/sandbox/v1/payment/qrcode/create"
        self.requestUId = str(uuid.uuid4())

    def save_qr_image_from_base64(self, base64_string):
        try:
            img_data = base64.b64decode(base64_string)
            img = Image.open(BytesIO(img_data)).resize((400, 400))
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error saving QR Image: {e}")
            return None

    def get_oauth_token(self):
        headers = {
            "Content-Type": "application/json",
            "resourceOwnerId": self.API_KEY,
            "accept-language": "EN",
            "requestUId": self.requestUId
        }
        data = {
            "applicationKey": self.API_KEY,
            "applicationSecret": self.API_SECRET
        }

        try:
            response = requests.post(self.API_URL, json=data, headers=headers)
            response.raise_for_status()

            response_data = response.json()
            return response_data.get("data", {}).get("accessToken")
        except requests.RequestException as e:
            print(f"Error getting token: {e}")
            return None

    def create_qr_code(self, access_token, biller_id, amount, ref1, ref2, ref3="NSUALLLOTTERY"):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
            "resourceOwnerId": self.API_KEY,
            "requestUId": self.requestUId,
            "accept-language": "EN"
        }
        data = {
            "qrType": "PP",
            "ppType": "BILLERID",
            "ppId": biller_id,
            "amount": amount,
            "ref1": ref1,
            "ref2": ref2,
            "ref3": ref3
        }

        try:
            response = requests.post(self.QR_CODE_URL, json=data, headers=headers)
            response.raise_for_status()

            response_data = response.json()

            if response_data.get("status", {}).get("description") == "Success":
                return response_data.get("data", {}).get("qrImage")
            else:
                print(f"Error creating QR code: {json.dumps(response_data, indent=2)}")
                return None
        except requests.RequestException as e:
            print(f"Error creating QR Code: {e}")
            return None

    def payment_success(self):
        
        # URL สำหรับตรวจสอบการชำระเงิน (โดยใช้ biller_id, ref1 และ transaction_date)
        success_url = f"https://webhook.site/186d5261-3fb6-4531-8f30-500f2e4bbd06"

        try:
            response = requests.post(success_url)
            response.raise_for_status()  # ตรวจสอบว่าไม่มีข้อผิดพลาด HTTP

            response_data = response.json()

            # ตรวจสอบว่า status เป็น Success หรือไม่
            if response_data.get( "resDesc ", {}) == "Success":
                               
                return "Success"
                
            else:
                print(f"Error checking payment status: {json.dumps(response_data, indent=2)}")
                return "Failed"

        except requests.RequestException as e:
            print(f"Error checking payment status: {e}")
            return "Failed"
