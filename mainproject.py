import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
import tkinter.messagebox

class All_lottery:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("Alllotery")
        self.stock = ['778206', '676503']
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()
        self.create_data()
        self.login_store()

    def create_data(self):
        try:
            self.c.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username VARCHAR(30) NOT NULL,
                password TEXT NOT NULL,
                fname VARCHAR(30) NOT NULL,
                lname VARCHAR(30) NOT NULL,
                Nick_name VARCHAR(30) NOT NULL,
                Age VARCHAR(2) NOT NULL,
                email VARCHAR(30) NOT NULL,
                Bank_Number VARCHAR(12) NOT NULL,
                Bank_Name VARCHAR(30) NOT NULL,
                Address VARCHAR(200) NOT NULL,
                phone VARCHAR(10) NOT NULL,
                access VARCHAR(20) NOT NULL)''')
            
            self.c.execute('''CREATE TABLE IF NOT EXISTS lottery(
                id INTEGER PRIMARY KEY,
                type VARCHAR(30) NOT NULL,
                num_id TEXT NOT NULL,
                price VARCHAR(30) NOT NULL,
                value VARCHAR(30) NOT NULL,
                img BLOB NOT NULL)''')
            self.conn.commit()
        except Exception as e:
            print(f"Error: {e}")

    def login_store(self):
        # พื้นหลังสีขาว
        ctk.CTkFrame(self.root, bg_color="white", width=1920, height=1080).pack()
        
        # uilogin
        self.image = Image.open('img/Dark Grey and Green Neon Modern Bold Payment Mobile App Presentation.png')
        self.image = self.image.resize((720, 480), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = ctk.CTkLabel(self.root, image=self.photo, bg_color="white")
        self.label.place(x=500, y=80)

        # ช่องกรอกชื่อผู้ใช้
        self.username_entry = ctk.CTkEntry(self.root, font=('Prompt', 12), placeholder_text="Username")
        self.username_entry.place(x=915, y=248)

        # ช่องกรอกรหัสผ่าน
        self.password_entry = ctk.CTkEntry(self.root, font=('Prompt', 12), show="*", placeholder_text="Password")
        self.password_entry.place(x=915, y=325)

        # ปุ่มเข้าสู่ระบบ
        self.signin_button = ctk.CTkButton(self.root, text="เข้าสู่ระบบ", command=self.main_store_ui, fg_color='#ff3131', text_color="white")
        self.signin_button.place(x=912, y=380)

        # ปุ่มสมัครสมาชิก
        self.signup_button = ctk.CTkButton(self.root, text="สมัครสมาชิก", command=self.signup_form, fg_color='#2b2b2b', text_color="white")
        self.signup_button.place(x=912, y=426)

    def signup_form(self):
        self.signup_ui = ctk.CTkToplevel(self.root)
        self.signup_ui.geometry("960x540")
        
        # พื้นหลังสีขาว
        ctk.CTkFrame(self.signup_ui, bg_color="white", width=1920, height=1080).pack()
        
        # โหลดภาพพื้นหลังของหน้า signup
        self.image_signup = Image.open('img/signup_form.png')
        self.image_signup = self.image_signup.resize((960, 540), Image.LANCZOS)
        self.photo_signup = ImageTk.PhotoImage(self.image_signup)
        self.label = ctk.CTkLabel(self.signup_ui, image=self.photo_signup, bg_color="white")
        self.label.place(x=0, y=0)

        # ช่องกรอกข้อมูลการสมัครสมาชิก
        self.et_fname = ctk.CTkEntry(self.signup_ui, placeholder_text="ชื่อจริง", font=('Prompt', 12))
        self.et_fname.place(x=260, y=94)
        self.et_lname = ctk.CTkEntry(self.signup_ui, placeholder_text="นามสกุล", font=('Prompt', 12))
        self.et_lname.place(x=260, y=155)
        self.et_Nname = ctk.CTkEntry(self.signup_ui, placeholder_text="ชื่อเล่น", font=('Prompt', 12), width=120)
        self.et_Nname.place(x=260, y=224)
        self.et_Age = ctk.CTkEntry(self.signup_ui, placeholder_text="อายุ", font=('Prompt', 12), width=60)
        self.et_Age.place(x=420, y=224)
        self.et_phone = ctk.CTkEntry(self.signup_ui, placeholder_text="เบอร์โทร", font=('Prompt', 12), width=180)
        self.et_phone.place(x=260, y=292)
        self.et_email = ctk.CTkEntry(self.signup_ui, placeholder_text="อีเมล", font=('Prompt', 12), width=180)
        self.et_email.place(x=260, y=358)

    def main_store_ui(self):
        self.root.destroy()
        self.store = ctk.CTk()
        self.store.geometry("1280x720")
        
        # พื้นหลังหน้าร้าน
        ctk.CTkLabel(self.store, text="MENU", font=("Prompt", 20)).place(x=400, y=2)
        ctk.CTkFrame(self.store, width=420, height=50, fg_color="black").place(x=220, y=50)
        
        # ช่องค้นหาหวย
        self.et_find = ctk.CTkEntry(self.store, width=250, font=("Prompt", 12), placeholder_text="ค้นหาเลขหวย")
        self.et_find.place(x=280, y=60)
        ctk.CTkButton(self.store, text='ค้นหา', command=self.find_lot, fg_color='#4be89a', text_color='white').place(x=550, y=58)
        
        # แสดงเลขหวย
        y_position = 120  
        for stock_item in self.stock:
            ctk.CTkFrame(self.store, width=420, height=70, fg_color="lightgray").place(x=220, y=y_position)
            ctk.CTkLabel(self.store, text=f"Lottery No: {stock_item}", font=("Arial", 15)).place(x=230, y=y_position)
            y_position += 100

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # ระบบแสดงผลธีมของระบบ (System Dark/Light mode)
    root = ctk.CTk()
    app = All_lottery(root)
    root.mainloop()
