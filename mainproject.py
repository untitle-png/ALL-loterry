from tkinter import *
import tkinter as tk
import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk
import datetime
from tkinter import messagebox
from datetime import datetime
import tkinter.messagebox
import io

class main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x620")
        self.root.title("Alllotery")
        
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()
        self.create_data()
        self.add_data()
        self.isLogin = False
        self.login_store()
        

    def create_data(self):
        try:
            self.c.execute('''CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY,
                username varchar(30) NOT NULL,
                password text NOT NULL,
                fname varchar(30) NOT NULL,
                lname varchar(30) NOT NULL,
                Age varchar(2) NOT NULL,
                email varchar(30) NOT NULL,
                Bank_Number varchar(12) NOT NULL,
                Bank_Name varchar(30) NOT NULL,
                Address varchar(200) NOT NULL,
                phone varchar(10) NOT NULL,
                access varchar(20) NOT NULL)''')
           
            self.c.execute('''CREATE TABLE IF NOT EXISTS lottery(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_lottery VARCHAR(30) NOT NULL,
                num_id TEXT NOT NULL,
                price INTEGER NOT NULL,
                amount INTEGER NOT NULL,
                img_lottery BLOB NOT NULL)''')
            self.conn.commit()
            
            self.c.execute('''CREATE TABLE IF NOT EXISTS orders(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                User_orders varchar(30) NOT NULL,
                orders_ID TEXT NOT NULL,
                amount_orders INTEGER NOT NULL,
                price_orders INTEGER NOT NULL,
                Cash INTEGER NOT NULL,
                status text NOT NULL
            )''')
            self.conn.commit()
        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {e}")
        finally:
            self.conn.close()
            
    def create_admin(self):
        pass

    def login_store(self):
        # สร้าง Frame พื้นหลังสีขาว
        tk.Frame(self.root, bg="white", width=1080, height=620).pack()
        
        # uilogin
        self.image = Image.open('img/login.png')
        self.image = self.image.resize((1080, 620), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(self.root, image=self.photo, bg="#e32020",width=1080,height=620)
        self.label.place(x=0, y=0)

        self.username_entry = tk.Entry(self.root, font=('Prompt',12), fg='black', bg='white', border=0)
        self.username_entry.place(x=705, y=253)

        # สร้าง Entry สำหรับรับข้อมูล (password)
        self.password_entry = tk.Entry(self.root, font=('Prompt',12), fg='black', bg='white', border=0, show="*")
        self.password_entry.place(x=705, y=323)

        # btn
        self.signin_button = ctk.CTkButton(self.root, font=('Prompt',16),text='เข้าสู่ระบบ',
                                           width=260,height=38
                                           ,fg_color='#e32320',
                                           hover_color='#c20300'
                                           ,command= self.login)
        self.signin_button.place(x=695, y=372)
        
        self.signup_button = ctk.CTkButton(self.root, font=('Prompt',16), 
                                           width =260,height=38, 
                                           text="สมัครสมาชิก",
                                           fg_color='#2b2b2b',
                                        hover_color='#000000'
                                      ,command=self.signup_form)
        self.signup_button.place(x=695, y=413)

    def register(self):
        pass
    
    def login(self):
        self.username = self.username_entry.get()
        password = self.password_entry.get()

        if not self.username or not password:
            tkinter.messagebox.showerror("Error", "กรุณากรอกข้อมูลให้ครบ")
            return

        try:
            self.conn = sqlite3.connect('data.db')
            self.c = self.conn.cursor()
            
            self.c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (self.username, password))
            result = self.c.fetchone()

            if result:
                self.user_id = result[0]
                self.user_role = result[11]  # ตรวจสอบสิทธิ์การเข้าถึง

                if self.user_role == "admin":
                    self.show_admin_menu()  # ถ้าเป็นผู้ดูแลระบบ
                    self.isLogin = True
                else:
                    self.main_store_ui()  # ถ้าเป็นผู้ใช้ธรรมดา
                    self.isLogin = True
            else:
                tkinter.messagebox.showerror("Error", "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
        except Exception as e:
            print(f"Error logging in: {e}")
        finally:
            self.conn.close()     

    def signup_form(self):
        self.signup_ui = tk.Toplevel(self.root)
        self.signup_ui.geometry("960x540")
        self.bg = tk.Frame(self.signup_ui, bg="#e32320", width=1920, height=1080)
        self.bg.pack()

        self.image_signup = Image.open('img/signup.png')
        self.image_signup = self.image_signup.resize((960, 540), Image.LANCZOS)
        self.photo_signup = ImageTk.PhotoImage(self.image_signup)
        self.label = tk.Label(self.signup_ui, image=self.photo_signup, bg="#e32320")
        self.label.place(x=0, y=0)

        self.et_fname = tk.Entry(self.signup_ui,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_fname.place(x = 260,y=106)
        self.et_lname = tk.Entry(self.signup_ui,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_lname.place(x = 260,y=166)
        
        style = ttk.Style()
        style.theme_use("default")  # ธีมอื่น ๆ ที่อาจลองใช้ได้เช่น 'alt' หรือ 'default'

        # ปรับสไตล์ของ Combobox ให้ border ดูบางลงหรือหายไป
        style.configure("TCombobox", 
                        fieldbackground="white",   # สีพื้นหลังใน combobox
                        borderwidth=0,             # ความหนาของขอบ
                        relief="flat",              # กำหนดลักษณะ relief ให้แบน
                    )
        style.configure("Vertical.TScrollbar", 
                gripcount=0,
                background="#cfcfcf",  # สีพื้นหลัง Scrollbar
                darkcolor="#2b2b2b",
                lightcolor="#2b2b2b",
                troughcolor="white",     # สีพื้นหลังราง Scrollbar
                bordercolor="white",
                arrowcolor="black",
                relief = "flat")
        
        self.dob_day = ttk.Combobox(self.signup_ui, values=list(map(str,range(1, 32))),
                                    width=3, height=8,style="TCombobox",
                                    font=('Prompt', 8),background='white',justify='center')
        self.dob_day.place(x=255, y=237,width=52) 
        
        self.dob_month_Option = tk.StringVar()

       
        self.dob_month = ttk.Combobox(
            master=self.signup_ui,
            font=('Prompt',8),
            values=[
                
                "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
                "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
            ],
            width=18,
            height=8,justify='center'
        )
        self.dob_month.place(x=320, y=237,width=120)
        current_year = datetime.now().year
        self.dob_year = ttk.Combobox(self.signup_ui, values=list(range(current_year, 1923, -1)),
                                     width=6,justify='center', font=('Prompt', 8))
        self.dob_year.place(x=458, y=237,width=52)

        self.et_phone = tk.Entry(self.signup_ui,width=18,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_phone.place(x =260,y=300)
        self.et_email = tk.Entry(self.signup_ui,width=18,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_email.place(x =260,y=368)
        self.et_banknumber = tk.Entry(self.signup_ui, width=14, font=('Prompt', 12), fg='black', bg='white', border=0)
        self.et_banknumber.place(x=260, y=428,width=130)
        self.et_bankname = ttk.Combobox(self.signup_ui, values=[
            "ธนาคารกรุงเทพ", "ธนาคารกสิกรไทย", "ธนาคารกรุงไทย", "ธนาคารทหารไทย", "ธนาคารไทยพาณิชย์", 
            "ธนาคารกรุงศรีอยุธยา", "ธนาคารเกียรตินาคิน", "ธนาคารซีไอเอ็มบีไทย", "ธนาคารทิสโก้", 
            "ธนาคารธนชาต", "ธนาคารยูโอบี", "ธนาคารสแตนดาร์ดชาร์เตอร์ด (ไทย)", 
            "ธนาคารไทยเครดิตเพื่อรายย่อย", "ธนาคารแลนด์ แอนด์ เฮาส์", 
            "ธนาคารไอซีบีซี (ไทย)", "ธนาคารพัฒนาวิสาหกิจขนาดกลางและขนาดย่อมแห่งประเทศไทย", 
            "ธนาคารเพื่อการเกษตรและสหกรณ์การเกษตร", "ธนาคารเพื่อการส่งออกและนำเข้าแห่งประเทศไทย", 
            "ธนาคารออมสิน", "ธนาคารอาคารสงเคราะห์", "ธนาคารอิสลามแห่งประเทศไทย", 
            "ธนาคารแห่งประเทศจีน", "ธนาคารซูมิโตโม มิตซุย ทรัสต์ (ไทย)", 
            "ธนาคารฮ่องกงและเซี้ยงไฮ้แบงกิ้งคอร์ปอเรชั่น จำกัด"
        ], width=20, font=('Prompt', 8),justify='center')
        self.et_bankname.place(x=408, y=428,width=98,height=25)

        self.et_adress = tk.Text(self.signup_ui,width=22,heigh=8,font=('Prompt',8), fg='black', bg='white',border=0)
        self.et_adress.place(x=550,y=118,width=196)
        self.et_username = tk.Entry(self.signup_ui,width=18,font=('Prompt',8), fg='black', bg='white', border=0)
        self.et_username.place(x =560,y=304)
        self.et_password = tk.Entry(self.signup_ui,width=18,font=('Prompt',8), fg='black', bg='white', border=0, show='*')
        self.et_password.place(x =560,y=364,width=190)
        self.et_password_confirm = tk.Entry(self.signup_ui,width=18,font=('Prompt',8), fg='black', bg='white', border=0, show='*')
        self.et_password_confirm.place(x =560,y=422,width=190)

        self.et_submit = ctk.CTkButton(self.signup_ui, text="Submit", 
                                       width=150, font=('Prompt',13), 
                                       text_color='white', fg_color='#2b2b2b',
                                        bg_color='#e32320',
                                       hover_color= 'black',
                                       corner_radius=5,
                                       border_width=0,
                                       border_color='#e32320',
                                       command=self.signup)
        self.et_submit.place(x=550, y=460)
       

    def signup(self):
        self.username = self.et_username.get()
        password = self.et_password.get()
        email = self.et_email.get()
        password_confirm = self.et_password_confirm.get()
        
        self.fname = self.et_fname.get()
        self.lname = self.et_lname.get()
        phone = self.et_phone.get()
        self.address = self.et_adress.get("1.0", "end-1c")
        self.bank_number = self.et_banknumber.get()
        self.bank_name = self.et_bankname.get()

        day = self.dob_day.get()
        month = self.dob_month.get()
        year = self.dob_year.get()

        # ตรวจสอบว่ามีการกรอกข้อมูลครบหรือไม่
        if not self.username or not password or not email or not day or not month or not year:
            tkinter.messagebox.showerror("Error", "กรุณากรอกข้อมูลให้ครบ")
            return

        if password != password_confirm:
            tkinter.messagebox.showerror("Error", "รหัสผ่านไม่ตรงกัน")
            return

        if not phone.isdigit() or len(phone) != 10:
            tkinter.messagebox.showerror("Error", "กรุณากรอกเบอร์โทรศํพท์ให้ถูกต้อง")
            return

        if not self.bank_number.isdigit() or not (10 <= len(self.bank_number) <= 12):
            tkinter.messagebox.showerror("Error", "กรุณากรอกเลขบัญชีธนาคารให้ถูกต้อง")
            return

        if "@" not in email or "." not in email or email.count("@") != 1 or email.startswith("@") or email.endswith("@") or email.endswith("."):
            tkinter.messagebox.showerror("Error", "กรุณากรอกอีเมลให้ถูกต้อง เช่น allottery@gmail.com")
            return


        # แปลงเดือนจากชื่อไทยเป็นตัวเลข
        month_dict = {
            "มกราคม": 1, "กุมภาพันธ์": 2, "มีนาคม": 3, "เมษายน": 4, "พฤษภาคม": 5, 
            "มิถุนายน": 6, "กรกฎาคม": 7, "สิงหาคม": 8, "กันยายน": 9, "ตุลาคม": 10, 
            "พฤศจิกายน": 11, "ธันวาคม": 12
        }
        month_number = month_dict[month]

        # คำนวณอายุ
        today = datetime.today()
        birth_date = datetime(int(year), month_number, int(day))
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        # ตรวจสอบอายุไม่ถึง 20 ปี
        if age < 20:
            tkinter.messagebox.showerror("Error", "คุณต้องมีอายุมากกว่า 20 ปีขึ้นไปจึงจะสามารถสมัครได้")
            return

        # ดำเนินการเก็บข้อมูลลงในฐานข้อมูล
        try:
            self.conn = sqlite3.connect('data.db')
            self.c = self.conn.cursor()

            # ตรวจสอบว่าผู้ใช้งานซ้ำหรือไม่
            self.c.execute("SELECT * FROM users WHERE username = ?", (self.username,))
            if self.c.fetchone():
                tkinter.messagebox.showerror("Error", "มีชื่อผู้ใช้งานอยู่ในระบบ")  
                return

            # เพิ่มข้อมูลผู้ใช้พร้อมอายุลงในฐานข้อมูล
            self.c.execute("INSERT INTO users (username, password, fname, lname, Age, email, phone, Bank_Number, Bank_Name, Address, access) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                        (self.username, password, self.fname, self.lname, str(age), email, phone, self.bank_number, self.bank_name, self.address, "user"))
            self.conn.commit()
            tkinter.messagebox.showinfo("Success", "สร้างบัญชีเสร็จสิ้น")  
            self.signup_ui.destroy()  # ปิดหน้าต่างสมัครสมาชิก
            self.login_store()  # กลับไปหน้าล็อกอิน
        except Exception as e:
            print(f"Error inserting user data: {e}")
        finally:
            self.conn.close()
            
    def add_data(self):
        # เชื่อมต่อกับฐานข้อมูล
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()
    
        try:
            self.c.execute("SELECT COUNT(*) FROM lottery ")
            self.max_stock = self.c.fetchone()[0]
            if self.max_stock <20:
                for i in range(20-self.max_stock):  # ปรับจำนวนที่ต้องการได้
                    image_path = f'img/ลอตเตอรี่/ลอตเตอรี่01.jpg'  # สมมุติว่าไฟล์ภาพถูกตั้งชื่อเรียงกัน
                    
                    # เปิดภาพ
                    self.img_lottery = Image.open(image_path)
                    
                    # แปลงภาพเป็นข้อมูลไบนารี
                    img_binary = io.BytesIO()
                    self.img_lottery.save(img_binary, format='JPEG')
                    img_binary_data = img_binary.getvalue()

                    # เตรียมข้อมูลสำหรับการแทรก
                    type_lottery = 'หวยเดี่ยว'  # สามารถเปลี่ยนแปลงได้
                    
                    # ตรวจสอบว่า num_id ถูกกำหนดค่า
                    num_id = f"123456"  # กำหนดหมายเลขล็อตเตอรี่
                    if not num_id:  # ถ้า num_id เป็น NULL จะมีการแจ้งเตือน
                        raise ValueError("num_id cannot be NULL")

                    self.price = 80  # ราคาเป็นตัวอย่าง
                    amount = 1  # จำนวนเป็นตัวอย่าง
                      

                    # เพิ่มข้อมูลลงในฐานข้อมูล (ไม่รวม id)
                    self.c.execute("INSERT INTO lottery(type_lottery, num_id, price, amount, img_lottery) VALUES (?, ?, ?, ?, ?)",
                                (type_lottery, num_id, self.price, amount, img_binary_data))
            
                # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
                self.conn.commit()
                
                
        except Exception as e:
            print(f"Error inserting data: {e}")
        finally:
            self.conn.close()
            
    def clear_frameItem_con(self):
        for widget in  self.frame_item_con.winfo_children():
            widget.destroy()
            
    def clear_main_con(self):
        for widget in  self.main_con.winfo_children():
            widget.destroy()
        


    def main_store_ui(self):
        self.root.destroy()  # ปิดหน้าต่างหลัก
        self.store = tk.Tk()  # สร้างหน้าต่างใหม่สำหรับหน้าร้าน
        self.store.tk.call('tk', 'scaling', 1.5)
        self.store.geometry("1080x620")
        self.store.title('ALL LOTTERY')
        self.store.configure(bg ="white")
        
        
    #รวมเมนูต่างๆ    

        bar_icon = tk.Frame(self.store,background='#e32320',width=100,height=1080)
        bar_icon.place(x=0,y=0)
        
       
        # โหลดภาพและปรับขนาดโดยใช้ CTkImage
        home_image = Image.open(r'D:\python_finalproject\img\icon\white\22.png')  # แก้ไขเส้นทางให้ถูกต้อง
        home_img_icon = ctk.CTkImage(home_image, size=(80, 40))  # ปรับขนาดที่ต้องการ
        # สร้าง CTkButton พร้อมภาพ
        self.home_btn = ctk.CTkButton(
            bar_icon,
            fg_color='#e32320',
            border_width=0,
            corner_radius=0,
            width=100,
            height=10,
            image=home_img_icon,
            text="หน้าหลัก",
            font=('Kanit Regular',14),
            compound=TOP,
            bg_color='#e32320',
            hover_color='#e32320',  # เปลี่ยนสีเมื่อ hover
            command=self.home_page
        )
        self.home_btn.place(x=0, y=85)    
           
        cart_image = Image.open(r'D:\python_finalproject\img\icon\white\26.png')  
        cart_img_icon = ctk.CTkImage(cart_image, size=(80, 40)) 
        
        self.cart_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
            border_width=0,
            corner_radius=0,
            width=100,
            height=90,
            image=cart_img_icon,
            text='ตะกร้า',
            font=('Kanit Regular',14),
            compound=TOP,
            bg_color='#e32320',
            hover_color='#e32320',
            command = self.cart_page # เปลี่ยนสีเมื่อ hover
           )
        self.cart_btn.place(x=0,y=175)


        save_image = Image.open(r'D:\python_finalproject\img\icon\white\27.png')  # แก้ไขเส้นทางให้ถูกต้อง
        save_img_icon = ctk.CTkImage(save_image, size=(80, 40))  # ปรับขนาดที่ต้องการ

        self.save_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
            border_width=0,
            corner_radius=0,
            width=100,
            height=90,
            image=save_img_icon,
            text='ตู้เซฟ',
            font=('Kanit Regular',14),
            compound=TOP,
            bg_color='#e32320',
            hover_color='#e32320',
            command=self.Mysave_page
           )
        self.save_btn.place(x=0,y=265)
        

        
        profile_image = Image.open(r'D:\python_finalproject\img\icon\white\24.png')  # แก้ไขเส้นทางให้ถูกต้อง
        profile_img_icon = ctk.CTkImage(profile_image, size=(80, 40))  # ปรับขนาดที่ต้องการ
        
        self.profile_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
            border_width=0,
            corner_radius=0,
            width=100,
            height=90,
            image=profile_img_icon,
            text='ข้อมูลส่วนตัว',
            font=('Kanit Medium',14),
            compound=TOP,
            bg_color='#e32320',
            hover_color='#e32320',
            command=self.profile_page
           )
        self.profile_btn.place(x=0,y=355)
        
        logout_image = Image.open(r'D:\python_finalproject\img\icon\white\25.png')  # แก้ไขเส้นทางให้ถูกต้อง
        logout_img_icon = ctk.CTkImage(logout_image, size=(80, 40))  # ปรับขนาดที่ต้องการ
        logout_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
            border_width=0,
            corner_radius=0,
            width=100,
            height=90,
            image=logout_img_icon,
            text='ออกจากระบบ',
            font=('Kanit Medium',14),
            compound=TOP,
            bg_color='#e32320',
            hover_color='#e32320'  # เปลี่ยนสีเมื่อ hover
           )
        logout_btn.place(x=0,y=500)
        
        
        self.allcon_frame = ctk.CTkCanvas(self.store)
        self.allcon_frame.place(x=100,y=0,width=1820,height=1080)

        self.home_page()
        
    def changeColor_icon(self, page, add_icon, icon_config):
        # ไอคอนสีดำเมื่ออยู่ในหน้าเฉพาะ
        icon_settings = {
            "home": r'D:\python_finalproject\img\icon\black\Home black.png',
            "cart": r'D:\python_finalproject\img\icon\black\cart black.png',
            "profile": r'D:\python_finalproject\img\icon\black\profile black.png',
            "save": r'D:\python_finalproject\img\icon\black\save black.png'
        }

        # ไอคอนสีขาวเมื่อไม่อยู่ในหน้าเฉพาะ
        icon_settings_white = {
            "home": r'D:\python_finalproject\img\icon\white\22.png',
            "cart": r'D:\python_finalproject\img\icon\white\26.png',
            "profile": r'D:\python_finalproject\img\icon\white\24.png',
            "save": r'D:\python_finalproject\img\icon\white\27.png'
        }
        
        # รีเซ็ตทุกปุ่มให้เป็นไอคอนสีขาวก่อน
        buttons = {
            "home": self.home_btn,
            "cart": self.cart_btn,
            "profile": self.profile_btn,
            "save": self.save_btn
        }
        
        for name, button in buttons.items():
            img = Image.open(icon_settings_white[name])
            img_icon = ctk.CTkImage(img, size=(80, 40))
            button.configure(image=img_icon, text_color='#ffffff')
        
        # ถ้าอยู่ในหน้าที่ระบุให้ตั้งไอคอนเป็นสีดำเฉพาะปุ่มนั้น ๆ
        if page:
            img = Image.open(icon_settings[add_icon])
            img_icon = ctk.CTkImage(img, size=(80, 40))
            icon_config.configure(image=img_icon, text_color='#2b2b2b')        
            
        
    
        
    def home_page(self):
        self.changeColor_icon(self.home_page,"home",self.home_btn)
        
        # สร้าง Frame หลักสำหรับการแสดงข้อมูล
        self.container = ctk.CTkFrame(self.store, width=1920, height=600, corner_radius=0, fg_color='white')
        self.container.place(x=100, y=0,relx= 0,rely = 0, relwidth =1 ,relheight = 1 )

        # สร้าง Canvas
        self.scroll_canvas = tk.Canvas(self.container, bg='white',highlightthickness=0)
        self.scroll_canvas.place(x=0, y=0, width=1920, height=600)

        # สร้าง Scrollbar
        self.scrollbar1 = ctk.CTkScrollbar(self.container, orientation='vertical',hover='white'
                                           ,corner_radius=10,
                                           fg_color='white',
                                           bg_color='white',button_color='white',
                                           width=18,height=100
                                           ,command=self.scroll_canvas.yview)
        
        self.scrollbar1.place(x=1902, y=0)
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar1.set)

        # สร้าง Frame ภายใน Canvas
        self.main_con = tk.Frame(self.scroll_canvas, bg='#ffffff')

        self.scroll_canvas.create_window((0, 0), window=self.main_con, anchor='nw')

        # อัปเดต scrollregion ของ Canvas
        self.main_con.bind("<Configure>", lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))

        # ฟังก์ชันสำหรับการเลื่อน Canvas เมื่อใช้ Scroll Wheel
        def on_mouse_scroll(event):
            self.scroll_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            if event.delta > 0 or event.keysym == 'Up':     # เลื่อนขึ้น
                self.scroll_canvas.yview_scroll(-1, "units")
            elif event.delta < 0 or event.keysym == 'Down': # เลื่อนลง
                self.scroll_canvas.yview_scroll(1, "units")        

        # ผูก Scroll Wheel เข้ากับ Canvas
        self.scroll_canvas.bind_all("<MouseWheel>", on_mouse_scroll) 
        self.scroll_canvas.bind_all("<Up>", on_mouse_scroll)# สำหรับ Windows
        self.scroll_canvas.bind_all("<Down>", on_mouse_scroll)# สำหรับ Windows
        
        self.header_frame = ctk.CTkFrame(self.store,fg_color='#2b2b2b'
                                         ,width=1920,height=50,
                                         corner_radius=0)
        self.header_frame.place(x =  100,y =0 )
        
        self.cash_con = ctk.CTkFrame(self.header_frame,fg_color='#ffffff',
                                     width=100,
                                     height=30)
        self.cash_con.place(x = 700,y = 10)
        
        self.cash_label = ctk.CTkLabel(self.cash_con,text='250',
                                       font=('Prompt',14)
                                       ,text_color='black')
        self.cash_label.place(x =40,y=0 )
                
        self.ads_frame = ctk.CTkFrame(self.main_con,fg_color='#b91c1c',
                                      width=400,height=250,
                                      corner_radius=0)
        self.ads_frame.grid(row =1,column = 0,pady= 5,sticky = NSEW)
        
        self.ads_item_con = ctk.CTkFrame(self.ads_frame,fg_color='#b91c1c',width=800 ,height=250,corner_radius=0)
        self.ads_item_con.place(x  = 90 , y= 0)
        
        # สร้าง Frame สำหรับปุ่มหวย
        self.button_frame = tk.Frame(self.main_con, bg='#ffffff')
        self.button_frame.grid(row=3, column=0,padx=20,sticky = NSEW,pady = 8)  # วางอยู่ที่แถว 0 ของ main_con
       
        self.search_con = ctk.CTkFrame(self.button_frame,width=1080,height=40,fg_color='white')
        self.search_con.grid(row = 0 , column= 3,sticky =NSEW,pady= 8,padx =20)
        self.et_search = ctk.CTkEntry(
                                self.search_con,
                                font=('Prompt', 14),           # กำหนดฟอนต์และขนาด
                                width=200,
                                height=32,# tk.Entry ใช้จำนวนตัวอักษรเป็นความกว้าง
                                fg_color='white',                     # สีพื้นหลัง
                                bg_color='white',
                                border_color='#cfcfcf',
                                text_color='black',
                                corner_radius=10)
        self.et_search.place(x = 0,y=3) 
        
        self.search_btn = ctk.CTkButton(self.search_con,text='ค้นหา',font=('Prompt',12),
                                        fg_color='#2b2b2b',
                                        width=50,height=32)
        self.search_btn.place(x = 210, y = 3 )      

        # ปุ่มหวย - วางใน button_frame
        self.allLot_btn = ctk.CTkButton(self.button_frame, text='ทั้งหมด', font=('Prompt', 12),
                                        width=84, height=35,
                                        fg_color='#e32320',
                                        hover_color='#e32320',
                                        text_color='white',
                                        command=self.allLot)
        self.allLot_btn.grid(row=0, column=0, padx=5)  # ใช้ grid แทน place

        self.pairLot_btn = ctk.CTkButton(self.button_frame, text='หวยชุด', font=('Prompt', 12),
                                        width=84, height=35,
                                        fg_color='#cfcfcf',
                                        hover_color='#cfcfcf',
                                        text_color='#2b2b2b',
                                        command=self.pairLot)
        self.pairLot_btn.grid(row=0, column=1, padx=5)  # ใช้ grid แทน place

        self.oddLot_btn = ctk.CTkButton(self.button_frame, text='หวยเดี่ยว', font=('Prompt', 12),
                                        width=84, height=35,
                                        fg_color='#cfcfcf',
                                        hover_color='#cfcfcf',
                                        text_color='#2b2b2b',
                                        command=self.oddLot)
        self.oddLot_btn.grid(row=0, column=2, padx=5)  # ใช้ grid แทน place
        
        
        self.frame_item_con = ctk.CTkFrame(self.main_con,fg_color='white') 
        self.frame_item_con.grid(row = 4,column =0,sticky = NSEW,padx = 5)        
        
        self.allLot()
        
        
    def allLot(self):
        self.clear_frameItem_con()
        
        self.allLot_btn.configure(fg_color='#e32320',hover_color='#e32320', text_color='white')
        self.pairLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
        self.oddLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
                    
        # เชื่อมต่อฐานข้อมูล
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()

        # ดึงข้อมูลภาพและเลขหวยจากฐานข้อมูล
        try:    
            self.c.execute('SELECT img_lottery,amount,price,type_lottery FROM lottery')
            self.alllottery_data = self.c.fetchall()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return

        if not self.alllottery_data:
            print("No images or lottery types found in the database.")
            return
        self.store_loterry(self.alllottery_data)

    def pairLot(self):
        self.clear_frameItem_con()
        self.allLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
        self.pairLot_btn.configure(fg_color='#e32320',hover_color='#e32320', text_color='white')
        self.oddLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
        
            # ลบ Frame ที่แสดงผลก่อนหน้า
       

        # เชื่อมต่อฐานข้อมูล
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()
        
        try:
            self.c.execute("SELECT img_lottery,amount,price,type_lottery FROM lottery WHERE type_lottery ='หวยคู่' ")
            self.pairlottery_data = self.c.fetchall()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return

        if not self.pairlottery_data:
            print("No images or lottery types found in the database.")
            return
        
        self.store_loterry(self.pairlottery_data)
        


    def oddLot(self):
        self.clear_frameItem_con()
        self.allLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
        self.pairLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
        self.oddLot_btn.configure(fg_color='#e32320',hover_color='#e32320', text_color='white')
        
            # ลบ Frame ที่แสดงผลก่อนหน้า
 
        # เชื่อมต่อฐานข้อมูล
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()
        
        try:
            self.c.execute("SELECT img_lottery,amount,price, type_lottery FROM lottery WHERE type_lottery ='หวยเดี่ยว' ")
            self.oddlottery_data = self.c.fetchall()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return
        

        if not self.oddlottery_data:
            print("No images or lottery types found in the database.")
            return
        self.store_loterry(self.oddlottery_data)
        
    
    def store_loterry(self,typelot):
        
        # แสดงข้อมูลภาพและ Combobox ในหน้า
        index = 0
        for i in range(len(typelot)):  # กำหนดจำนวนแถว
            for j in range(4):  # กำหนดจำนวนคอลัมน์
                if index < len(typelot):
                    img_data,amount_data,price_data, typelot_data= typelot[index]

                    # แปลงข้อมูล BLOB เป็นภาพ
                    img1 = Image.open(io.BytesIO(img_data))
                    img1 = img1.resize((200, 100))
                    self.img_lot = ImageTk.PhotoImage(img1)

                    # สร้างกรอบสำหรับสินค้า
                    frame_item = ctk.CTkFrame(self.frame_item_con, width=226, height=180, corner_radius=10, fg_color='#2b2b2b')
                    frame_item.grid(row =i,column =j,padx =8,pady =10)
                    self.frame_item_con.configure(width=980, height=1920)

                    # ใส่รูปภาพในกรอบสินค้า
                    self.label_image = tk.Label(frame_item, image=self.img_lot)
                    self.label_image.image = self.img_lot  # เก็บ reference ให้กับ image
                    self.label_image.place(x=10, y=35)

                    # แสดงประเภทหวย
                    typelot_label = tk.Label(frame_item, text=typelot_data, font=('Prompt', 10), fg='white', bg='#2b2b2b', width=9)
                    typelot_label.place(x=65, y=5)

                    # สร้าง Combobox สำหรับเลือกจำนวน
                    self.amount_combo = ctk.CTkComboBox(frame_item,
                                                    values=[str(amount_data)],
                                                    width=50, height=23,
                                                    corner_radius=5, border_width=0,
                                                    bg_color='#2b2b2b', fg_color='white',
                                                    text_color='#2b2b2b',
                                                    dropdown_fg_color='white',
                                                    dropdown_hover_color='#ebe8e8',
                                                    dropdown_text_color='#2b2b2b',
                                                    button_color='white',
                                                    button_hover_color='#ebe8e8')
                    self.amount_combo.place(x=12, y=148)
                    
                    self.cartPick_image = Image.open(r'D:\python_finalproject\img\icon\white\26.png')  
                    self.cartPick_img_icon = ctk.CTkImage(self.cartPick_image, size=(30, 20)) 

                    pick_btn = ctk.CTkButton(frame_item, text='หยิบใส่ตระกร้า',
                                             image=self.cartPick_img_icon,
                                             compound=RIGHT,
                                             anchor='w',
                                            font=('Prompt', 12),
                                            width=45, height=16,
                                            border_width=0,
                                            bg_color='#2b2b2b',
                                            fg_color='#2b2b2b',
                                            hover_color='black'
                                            ,command=self.add_cart)
                    pick_btn.place(x=70, y=145)

                index += 1  # เพิ่มตัวนับรูปภาพ
        self.conn.close()
        
    def add_cart(self):
        self.conn =sqlite3.connect('data.db')
        self.c =self.conn.cursor()
        amout = self.amount_combo.get()

        self.c.execute('SELECT * FROM users WHERE username = ? ',self.username)
        username = self.c.fetchone()
        d = (username,amout,self.price)
        
        self.c.execute('INSERT INTO orders(User_orders,amont_orders,price_orders,) VALUES (?,?,?)',d)
        self.conn.commit()  
              
        self.conn.close()
        
        
        
        
        
        
        pass        

    def cart_page(self):
        self.changeColor_icon(self.cart_page,"cart",self.cart_btn)
        self.clear_main_con()
        
        self.cartFrame_con =ctk.CTkFrame(self.main_con,fg_color='#2b2b2b',
                                          width=1000,
                                          height=200,
                                          corner_radius=0) 
        self.cartFrame_con.grid( row = 0 , column = 0)
        
        self.label_image = tk.Label(self.cartFrame_con, image=self.img_lot)
        self.label_image.image = self.img_lot  # เก็บ reference ให้กับ image
        self.label_image.place(x=10, y=35)

       
          
    def Mysave_page(self):
        self.changeColor_icon(self.Mysave_page,"save",self.save_btn)
        self.clear_main_con()
       
        
    
    def profile_page(self):
        self.changeColor_icon(self.profile_page,"profile",self.profile_btn)
        self.clear_main_con() 
       
            
            
# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    root = tk.Tk()
    app = main(root)
    default_font = ("Prompt",8)  # ตั้งฟอนต์ภาษาไทย เช่น "Prompt" ขนาด 14
    root.option_add("*Font", default_font)

    root.mainloop()
