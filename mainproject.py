import tkinter as tk
import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter.messagebox
import io

class All_lotery:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("Alllotery")
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()
        self.create_data()
        self.login_store()

    def create_data(self):
        try:
            self.c.execute('''CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY,
                username varchar(30) NOT NULL,
                password text NOT NULL,
                fname varchar(30) NOT NULL,
                lname varchar(30) NOT NULL,
                Nick_name varchar(30) NOT NULL,
                Age varchar(2) NOT NULL,
                email varchar(30) NOT NULL,
                Bank_Number varchar(12) NOT NULL,
                Bank_Name varchar(30) NOT NULL,
                Address varchar(200) NOT NULL,
                phone varchar(10) NOT NULL,
                access varchar(20) NOT NULL)''')
           
            self.c.execute('''CREATE TABLE IF NOT EXISTS lottery(id integer PRIMARY KEY,
                type_lottery varchar(30) NOT NULL,
                num_id text NOT NULL,
                price integer NOT NULL,
                amount integer NOT NULL,
                img_lottery BLOB NOT NULL)''')
            self.conn.commit()
        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {e}")
        finally:
            self.conn.close()
            
    def create_admin(self):
        pass

    def login_store(self):
        # สร้าง Frame พื้นหลังสีขาว
        tk.Frame(self.root, bg="white", width=1920, height=1080).pack()
        
        # uilogin
        self.image = Image.open('img/login.png')
        self.image = self.image.resize((720, 480), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(self.root, image=self.photo, bg="white")
        self.label.place(x=500, y=80)

        self.username_entry = tk.Entry(self.root, font=('Prompt',12), fg='black', bg='white', border=0)
        self.username_entry.place(x=915, y=248)

        # สร้าง Entry สำหรับรับข้อมูล (password)
        self.password_entry = tk.Entry(self.root, font=('Prompt',12), fg='black', bg='white', border=0, show="*")
        self.password_entry.place(x=915, y=325)

        # btn
        self.signin_button = tk.Button(self.root, font=('Prompt',12),border=0, bg='#ff3131',fg="white", width=20, text="เข้าสู่ระบบ", activebackground='#ff3131', relief='flat',command= self.main_store_ui)
        self.signin_button.place(x=912, y=380)
        self.signup_button = tk.Button(self.root, font=('Prompt',12),border=0, bg='#2b2b2b',fg="white", width=20, text="สมัครสมาชิก", activebackground='#2b2b2b', relief='flat',command=self.signup_form)
        self.signup_button.place(x=912, y=426)

    def register(self):
        pass
    
    def check_user(self):
        self.checkUser = self.username_entry.get()
        self.checkPass = self.password_entry.get()
        if self.checkUser == '' and self.checkPass == '':
            self.main_store_ui()
            self.root.destroy()

    def store(self):
        pass

    def signup_form(self):
        self.signup_ui = tk.Toplevel(self.root)
        self.signup_ui.geometry("960x540")
        self.bg = tk.Frame(self.signup_ui, bg="white", width=1920, height=1080)
        self.bg.pack()
        
        self.image_signup = Image.open('img/signup.png')
        self.image_signup = self.image_signup.resize((960,540), Image.LANCZOS)
        self.photo_signup = ImageTk.PhotoImage(self.image_signup)
        self.label = tk.Label(self.signup_ui, image=self.photo_signup, bg="white")
        self.label.place(x=0, y=0)
        
        self.et_fname = tk.Entry(self.signup_ui,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_fname.place(x = 260,y=94)
        self.et_lname = tk.Entry(self.signup_ui,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_lname.place(x = 260,y=155)
        self.et_Nname = tk.Entry(self.signup_ui,width=12,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_Nname.place(x = 260,y=224)
        self.et_Age = tk.Entry(self.signup_ui,width=6,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_Age.place(x = 420,y=224)
        self.et_phone = tk.Entry(self.signup_ui,width=18,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_phone.place(x =260,y=292)
        self.et_email = tk.Entry(self.signup_ui,width=18,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_email.place(x =260,y=358)

    def sigup_data(self):
        self.fname = self.et_fname.get()
        self.lname = self.et_lname.get()
        self.N_name = self.et_Nname.get()
        self.Age = self.et_Age.get()
        self.phone =self.et_phone.get()
        self.data_signup = (self.fname,self.lname)
        
        if self.fname == '':
            tkinter.messagebox.showerror()
        elif self.lname == '':
            tkinter.messagebox.showerror()
        elif self.fname == '':
            tkinter.messagebox.showerror()
        
        elif self.password != self.confirm_pass:
            tkinter.messagebox.showerror()
        
        else:
            self.signup_ui.destroy()
            
        self.c.execute('''INSERT INTO user(fname,lname,Nick_name,Age,phone,email,Bank_Number,Bank_Name,address,username,password) VALUES(?,?,?,?,?,?,?,?,?,?,?)''',self.data_signup)
        self.conn.commit()
        


    def main_store_ui(self):
        self.root.destroy()  # ปิดหน้าต่างหลัก
        self.store = tk.Tk()  # สร้างหน้าต่างใหม่สำหรับหน้าร้าน
        self.store.geometry("1080x620")
        
               
        bar_icon = tk.Frame(self.store,background='#e32320',width=80,height=1080)
        bar_icon.place(x=0,y=0)
        
        home_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
                             border_width=0,
                             corner_radius=0,
                             width=80,height=90,
                             command=self.home_page)
        home_btn.place(x=0,y=85)
        
        search_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
                                   corner_radius=0,
                                   width=80,height=90)
        search_btn.place(x=0,y=175)
        
        cart_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
                                   corner_radius=0,
                                   width=80,height=90)
        cart_btn.place(x=0,y=265)
        
        profile_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
                                   corner_radius=0,
                                   width=80,height=90)
        profile_btn.place(x=0,y=355)
        
        logout_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
                                   corner_radius=0,
                                   width=80,height=90)
        logout_btn.place(x=0,y=500)
        
        self.home_page()
        
    def home_page(self):    
        #ปุ่มหวย
        self.allLot_btn = ctk.CTkButton(self.store,text='ทั้งหมด',font=('Prompt',12),
                                    width=84,height=35,
                                    fg_color='#e32320',
                                    hover_color='#e32320',
                                    text_color='white',
                                    command=self.allLot
                                    )
        self.allLot_btn.place(x=132,y=32) 
        
        self.pairLot_btn = ctk.CTkButton(self.store,text='หวยชุด',font=('Prompt',12),
                                    width=84,height=35,
                                    fg_color='#cfcfcf',
                                    hover_color='#cfcfcf',
                                    text_color='#2b2b2b',
                                    command=self.pairLot
                                    
                             
                                    )
        self.pairLot_btn.place(x=228,y=32)
        
        self.oddLot_btn = ctk.CTkButton(self.store,text='หวยเดี่ยว',font=('Prompt',12),
                                    width=84,height=35,
                                    fg_color='#cfcfcf',
                                    hover_color='#cfcfcf',
                                    text_color='#2b2b2b',
                                    command=self.oddLot
                                    
                                    )
        self.oddLot_btn.place(x=324,y=32)
        
        
        # สร้าง Frame สำหรับการแสดงข้อมูล
        container = ctk.CTkFrame(self.store, width=830, height=520, corner_radius=10, fg_color='white')
        container.place(x=120, y=81)

        # สร้าง Canvas
        self.scroll_canvas = tk.Canvas(container, bg='white',border=0)
        self.scroll_canvas.place(x=0, y=0, width=830, height=520)

        # สร้าง Scrollbar
        self.scrollbar1 = ctk.CTkScrollbar(container, orientation='vertical',width=18,height=50,command=self.scroll_canvas.yview)
        self.scrollbar1.place(x=820, y=10)
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar1.set)

        # สร้าง Frame ภายใน Canvas
        self.main_con = tk.Frame(self.scroll_canvas, bg='white')
        self.scroll_canvas.create_window((0, 0), window=self.main_con, anchor='nw')

        # อัปเดต scrollregion ของ Canvas
        self.main_con.bind("<Configure>", lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))
    
        self.allLot()
        
    def allLot(self):
        
        self.allLot_btn.configure(fg_color='#e32320',hover_color='#e32320', text_color='white')
        self.pairLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
        self.oddLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
        
        
         # ลบ Frame ที่แสดงผลก่อนหน้า
        if hasattr(self, 'main_con'):
            for widget in self.main_con.winfo_children():
                widget.destroy()

        
        # เชื่อมต่อฐานข้อมูล
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()

        # ดึงข้อมูลภาพและเลขหวยจากฐานข้อมูล
        try:    
            self.c.execute('SELECT img_lottery, type_lottery FROM lottery')
            self.lottery_data = self.c.fetchall()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return

        if not self.lottery_data:
            print("No images or lottery types found in the database.")
            return
        
        # แสดงข้อมูลภาพและ Combobox ในหน้า
        index = 0
        for i in range(len(self.lottery_data)):  # กำหนดจำนวนแถว
            for j in range(4):  # กำหนดจำนวนคอลัมน์
                if index < len(self.lottery_data):
                    img_data, typelot_data = self.lottery_data[index]

                    # แปลงข้อมูล BLOB เป็นภาพ
                    img1 = Image.open(io.BytesIO(img_data))
                    img1 = img1.resize((160, 83))
                    photo1 = ImageTk.PhotoImage(img1)

                    # สร้างกรอบสำหรับสินค้า
                    frame_item = ctk.CTkFrame(self.main_con, width=185, height=146, corner_radius=10, fg_color='#2b2b2b')
                    frame_item.grid(row=i, column=j, padx=10, pady=10)  # ใช้ grid

                    # ใส่รูปภาพในกรอบสินค้า
                    label_image = tk.Label(frame_item, image=photo1)
                    label_image.image = photo1  # เก็บ reference ให้กับ image
                    label_image.place(x=10, y=25)

                    # แสดงประเภทหวย
                    typelot_label = tk.Label(frame_item, text=typelot_data, font=('Prompt', 9), fg='white', bg='#2b2b2b', width=9)
                    typelot_label.place(x=58, y=1)

                    # สร้าง Combobox สำหรับเลือกจำนวน
                    amount_combo = ctk.CTkComboBox(frame_item,
                                                    values=["1", "2", "3", "4", "5"],
                                                    width=50, height=18,
                                                    corner_radius=5, border_width=0,
                                                    bg_color='#2b2b2b', fg_color='white',
                                                    text_color='#2b2b2b',
                                                    dropdown_fg_color='white',
                                                    dropdown_hover_color='#e32320',
                                                    dropdown_text_color='#2b2b2b',
                                                    button_color='white',
                                                    button_hover_color='#ebe8e8')
                    amount_combo.place(x=12, y=118)

                    pick_btn = ctk.CTkButton(frame_item, text='หยิบใส่ตระกร้า',
                                            font=('Prompt', 12),
                                            width=20, height=16,
                                            border_width=0,
                                            bg_color='#2b2b2b',
                                            fg_color='#2b2b2b',
                                            hover_color='black')
                    pick_btn.place(x=70, y=116)

                index += 1  # เพิ่มตัวนับรูปภาพ
        self.conn.close()        

    def pairLot(self):
        
        self.allLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
        self.pairLot_btn.configure(fg_color='#e32320',hover_color='#e32320', text_color='white')
        self.oddLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
        
            # ลบ Frame ที่แสดงผลก่อนหน้า
        if hasattr(self, 'main_con'):
            for widget in self.main_con.winfo_children():
                widget.destroy()

        # เชื่อมต่อฐานข้อมูล
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()
        
        try:
            self.c.execute("SELECT img_lottery, type_lottery FROM lottery WHERE type_lottery ='หวยคู่' ")
            self.pairlottery_data = self.c.fetchall()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return

        if not self.pairlottery_data:
            print("No images or lottery types found in the database.")
            return
        
        
        # แสดงข้อมูลภาพและ Combobox ในหน้า
        index = 0
        for i in range(len(self.pairlottery_data)):  # กำหนดจำนวนแถว
            for j in range(4):  # กำหนดจำนวนคอลัมน์
                if index < len(self.pairlottery_data):
                    img_data, typelot_data = self.pairlottery_data[index]

                    # แปลงข้อมูล BLOB เป็นภาพ
                    img1 = Image.open(io.BytesIO(img_data))
                    img1 = img1.resize((160, 83))
                    photo1 = ImageTk.PhotoImage(img1)

                    # สร้างกรอบสำหรับสินค้า
                    frame_item = ctk.CTkFrame(self.main_con2, width=185, height=146, corner_radius=10, fg_color='#2b2b2b')
                    frame_item.grid(row=i, column=j, padx=10, pady=10)  # ใช้ grid

                    # ใส่รูปภาพในกรอบสินค้า
                    label_image = tk.Label(frame_item, image=photo1)
                    label_image.image = photo1  # เก็บ reference ให้กับ image
                    label_image.place(x=10, y=25)

                    # แสดงประเภทหวย
                    typelot_label = tk.Label(frame_item, text=typelot_data, font=('Prompt', 9), fg='white', bg='#2b2b2b', width=9)
                    typelot_label.place(x=58, y=1)

                    # สร้าง Combobox สำหรับเลือกจำนวน
                    amount_combo = ctk.CTkComboBox(frame_item,
                                                    values=["1", "2", "3", "4", "5"],
                                                    width=50, height=18,
                                                    corner_radius=5, border_width=0,
                                                    bg_color='#2b2b2b', fg_color='white',
                                                    text_color='#2b2b2b',
                                                    dropdown_fg_color='white',
                                                    dropdown_hover_color='#e32320',
                                                    dropdown_text_color='#2b2b2b',
                                                    button_color='white',
                                                    button_hover_color='#ebe8e8')
                    amount_combo.place(x=12, y=118)

                    pick_btn = ctk.CTkButton(frame_item, text='หยิบใส่ตระกร้า',
                                            font=('Prompt', 12),
                                            width=20, height=16,
                                            border_width=0,
                                            bg_color='#2b2b2b',
                                            fg_color='#2b2b2b',
                                            hover_color='black')
                    pick_btn.place(x=70, y=116)

                index += 1  # เพิ่มตัวนับรูปภาพ
        self.conn.close() 

    def oddLot(self):
        
        self.allLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
        self.pairLot_btn.configure(fg_color='#cfcfcf',hover_color='#cfcfcf', text_color='#2b2b2b')
        self.oddLot_btn.configure(fg_color='#e32320',hover_color='#e32320', text_color='white')
        
            # ลบ Frame ที่แสดงผลก่อนหน้า
        if hasattr(self, 'main_con'):
            for widget in self.main_con.winfo_children():
                widget.destroy()

        # เชื่อมต่อฐานข้อมูล
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()
        
        try:
            self.c.execute("SELECT img_lottery, type_lottery FROM lottery WHERE type_lottery ='หวยเดี่ยว' ")
            self.oddlottery_data = self.c.fetchall()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return
        

        if not self.oddlottery_data:
            print("No images or lottery types found in the database.")
            return
        

        
        # แสดงข้อมูลภาพและ Combobox ในหน้า
        index = 0
        for i in range(len(self.oddlottery_data)):  # กำหนดจำนวนแถว
            for j in range(4):  # กำหนดจำนวนคอลัมน์
                if index < len(self.oddlottery_data):
                    img_data, typelot_data = self.oddlottery_data[index]

                    # แปลงข้อมูล BLOB เป็นภาพ
                    img1 = Image.open(io.BytesIO(img_data))
                    img1 = img1.resize((160, 83))
                    photo1 = ImageTk.PhotoImage(img1)

                    # สร้างกรอบสำหรับสินค้า
                    frame_item = ctk.CTkFrame(self.main_con, width=185, height=146, corner_radius=10, fg_color='#2b2b2b')
                    frame_item.grid(row=i, column=j, padx=10, pady=10)  # ใช้ grid

                    # ใส่รูปภาพในกรอบสินค้า
                    label_image = tk.Label(frame_item, image=photo1)
                    label_image.image = photo1  # เก็บ reference ให้กับ image
                    label_image.place(x=10, y=25)

                    # แสดงประเภทหวย
                    typelot_label = tk.Label(frame_item, text=typelot_data, font=('Prompt', 9), fg='white', bg='#2b2b2b', width=9)
                    typelot_label.place(x=58, y=1)

                    # สร้าง Combobox สำหรับเลือกจำนวน
                    amount_combo = ctk.CTkComboBox(frame_item,
                                                    values=["1", "2", "3", "4", "5"],
                                                    width=50, height=18,
                                                    corner_radius=5, border_width=0,
                                                    bg_color='#2b2b2b', fg_color='white',
                                                    text_color='#2b2b2b',
                                                    dropdown_fg_color='white',
                                                    dropdown_hover_color='#e32320',
                                                    dropdown_text_color='#2b2b2b',
                                                    button_color='white',
                                                    button_hover_color='#ebe8e8')
                    amount_combo.place(x=12, y=118)

                    pick_btn = ctk.CTkButton(frame_item, text='หยิบใส่ตระกร้า',
                                            font=('Prompt', 12),
                                            width=20, height=16,
                                            border_width=0,
                                            bg_color='#2b2b2b',
                                            fg_color='#2b2b2b',
                                            hover_color='black')
                    pick_btn.place(x=70, y=116)

                index += 1  # เพิ่มตัวนับรูปภาพ
        self.conn.close()         
            
# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    root = tk.Tk()
    app = All_lotery(root)
    root.mainloop()