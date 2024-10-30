from tkinter import *
import tkinter as tk
import customtkinter as ctk
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk
import datetime
import tkinter.messagebox
import io

class All_lotery:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x620")
        self.root.title("Alllotery")
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()
        self.create_data()
        self.add_data()
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
           
            self.c.execute('''CREATE TABLE IF NOT EXISTS lottery(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_lottery VARCHAR(30) NOT NULL,
                num_id TEXT NOT NULL,
                price INTEGER NOT NULL,
                amount INTEGER NOT NULL,
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
        tk.Frame(self.root, bg="white", width=1080, height=620).pack()
        
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
        self.image_signup = self.image_signup.resize((960, 540), Image.LANCZOS)
        self.photo_signup = ImageTk.PhotoImage(self.image_signup)
        self.label = tk.Label(self.signup_ui, image=self.photo_signup, bg="white")
        self.label.place(x=0, y=0)

        self.et_fname = tk.Entry(self.signup_ui,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_fname.place(x = 260,y=97)
        self.et_lname = tk.Entry(self.signup_ui,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_lname.place(x = 260,y=155)
        self.et_Nname = tk.Entry(self.signup_ui,width=12,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_Nname.place(x = 260,y=224)

        self.dob_day = ttk.Combobox(self.signup_ui, values=list(range(1, 32)), width=3, font=('Prompt', 12))
        self.dob_day.place(x=250, y=225)

        self.dob_month = ttk.Combobox(self.signup_ui, values=[
            "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
            "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
        ], width=9, font=('Prompt', 12))
        self.dob_month.place(x=310, y=225)

        current_year = datetime.now().year
        self.dob_year = ttk.Combobox(self.signup_ui, values=list(range(current_year, 1923, -1)), width=6, font=('Prompt', 12))
        self.dob_year.place(x=425, y=225)

        self.et_phone = tk.Entry(self.signup_ui,width=18,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_phone.place(x =260,y=292)
        self.et_email = tk.Entry(self.signup_ui,width=18,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_email.place(x =260,y=358)

        self.et_banknumber = tk.Entry(self.signup_ui, width=14, font=('Prompt', 12), fg='black', bg='white', border=0)
        self.et_banknumber.place(x=260, y=419)
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
        ], width=10, font=('Prompt', 10))
        self.et_bankname.place(x=410, y=419)

        self.et_adress = tk.Text(self.signup_ui,width=22,heigh=8,font=('Prompt',12), fg='black', bg='white',border=0)
        self.et_adress.place(x=550,y=105)
        self.et_username = tk.Entry(self.signup_ui,width=18,font=('Prompt',12), fg='black', bg='white', border=0)
        self.et_username.place(x =560,y=295)
        self.et_password = tk.Entry(self.signup_ui,width=18,font=('Prompt',12), fg='black', bg='white', border=0, show='*')
        self.et_password.place(x =560,y=358)
        self.et_password_confirm = tk.Entry(self.signup_ui,width=18,font=('Prompt',12), fg='black', bg='white', border=0, show='*')
        self.et_password_confirm.place(x =560,y=419)

        self.et_submit = tk.Button(self.signup_ui, text="Submit", width=22, font=('Prompt',13), fg='white', bg='red', border=0,command=self.signup)
        self.et_submit.place(x=550, y=465)
        self.et_backtologin = tk.Button(self.signup_ui, text="Back to Login", width=22, font=('Prompt',13),fg='white',bg='grey',border=0,command=self.back_to_login)
        self.et_backtologin.place(x=250, y=465)

   

    def signup(self):
        username = self.et_username.get()
        password = self.et_password.get()
        email = self.et_email.get()
        password_confirm = self.et_password_confirm.get()

        day = self.dob_day.get()
        month = self.dob_month.get()
        year = self.dob_year.get()

        if not username or not password or not email or not day or not month or not year:
            tk.messagebox.showerror("Error", "กรุณาลองใหม่อีกครั้ง")
            return

        if password != password_confirm:
            tk.messagebox.showerror("Error", "รหัสผ่านไม่ตรงกัน")
            return
        self.c.execute("SELECT * FROM users WHERE username = ?", (username,))
        if self.c.fetchone():
            tk.messagebox.showerror("Error", "มีชื่อผู้ใช้งานอยู่ในระบบ")
            return
        self.c.execute("INSERT INTO users (username, password, email, role, date_of_birth) VALUES (?, ?, ?, ?, ?)", 
                       (username, password, email, 'user', f"{year}-{month}-{day}"))
        self.conn.commit()

        tk.messagebox.showinfo("Success", "สร้างบัญชีเสร็จสิ้น")
        self.login_store() 

    def back_to_login(self):
        self.signup_ui.destroy()

    def show_admin_menu(self):
        admin_window = tk.Toplevel(self.root)
        admin_window.geometry("1280x720")
        admin_window.title("Admin Panel")
        tk.Label(admin_window, text="Admin Panel", font=('Prompt', 18)).pack()   
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            tk.messagebox.showerror("Error", "กรุณากรอกข้อมูลให้ครบ")
            return

        self.c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = self.c.fetchone()

        if result:
            self.user_id = result[0]
            self.user_role = result[12] 

            if self.user_role == "admin":
                self.show_admin_menu()
            else:
                self.main_store_ui()
        else:
            tk.messagebox.showerror("Error", "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")         
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

                    price = 80  # ราคาเป็นตัวอย่าง
                    amount = 1  # จำนวนเป็นตัวอย่าง
                      

                    # เพิ่มข้อมูลลงในฐานข้อมูล (ไม่รวม id)
                    self.c.execute("INSERT INTO lottery(type_lottery, num_id, price, amount, img_lottery) VALUES (?, ?, ?, ?, ?)",
                                (type_lottery, num_id, price, amount, img_binary_data))
            
                # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
                self.conn.commit()
                
                
        except Exception as e:
            print(f"Error inserting data: {e}")
        finally:
            self.conn.close()


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
        self.home_image = Image.open(r'D:\python_finalproject\img\icon\white\22.png')  # แก้ไขเส้นทางให้ถูกต้อง
        self.home_img_icon = ctk.CTkImage(self.home_image, size=(80, 40))  # ปรับขนาดที่ต้องการ
        # สร้าง CTkButton พร้อมภาพ
        self.home_btn = ctk.CTkButton(
            bar_icon,
            fg_color='#e32320',
            border_width=0,
            corner_radius=0,
            width=100,
            height=10,
            image=self.home_img_icon,
            text="หน้าหลัก",
            font=('Kanit Regular',14),
            compound=TOP,
            bg_color='#e32320',
            hover_color='#e32320',  # เปลี่ยนสีเมื่อ hover
            command=self.home_page
        )
        self.home_btn.place(x=0, y=85)

        self.search_image = Image.open(r'D:\python_finalproject\img\icon\white\23.png')  # แก้ไขเส้นทางให้ถูกต้อง
        self.search_img_icon = ctk.CTkImage(self.search_image, size=(80, 40))  # ปรับขนาดที่ต้องการ

        search_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
            border_width=0,
            corner_radius=0,
            width=100,
            height=90,
            image=self.search_img_icon,
            text='ค้นหา',
            font=('Kanit Regular',14),
            compound=TOP,
            bg_color='#e32320',
            hover_color='#e32320'  # เปลี่ยนสีเมื่อ hover
           )
        search_btn.place(x=0,y=175)
        
        self.cart_image = Image.open(r'D:\python_finalproject\img\icon\white\26.png')  # แก้ไขเส้นทางให้ถูกต้อง
        self.cart_img_icon = ctk.CTkImage(self.cart_image, size=(80, 40))  # ปรับขนาดที่ต้องการ
        
        cart_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
            border_width=0,
            corner_radius=0,
            width=100,
            height=90,
            image=self.cart_img_icon,
            text='ตะกร้า',
            font=('Kanit Regular',14),
            compound=TOP,
            bg_color='#e32320',
            hover_color='#e32320'  # เปลี่ยนสีเมื่อ hover
           )
        cart_btn.place(x=0,y=265)
        
        self.profile_image = Image.open(r'D:\python_finalproject\img\icon\white\24.png')  # แก้ไขเส้นทางให้ถูกต้อง
        self.profile_img_icon = ctk.CTkImage(self.profile_image, size=(80, 40))  # ปรับขนาดที่ต้องการ
        
        profile_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
            border_width=0,
            corner_radius=0,
            width=100,
            height=90,
            image=self.profile_img_icon,
            text='ข้อมูลส่วนตัว',
            font=('Kanit Regular',14),
            compound=TOP,
            bg_color='#e32320',
            hover_color='#e32320',
            command=self.profile_page
           )
        profile_btn.place(x=0,y=355)
        
        self.logout_image = Image.open(r'D:\python_finalproject\img\icon\white\25.png')  # แก้ไขเส้นทางให้ถูกต้อง
        self.logout_img_icon = ctk.CTkImage(self.logout_image, size=(80, 40))  # ปรับขนาดที่ต้องการ
        logout_btn = ctk.CTkButton(bar_icon,fg_color='#e32320',
            border_width=0,
            corner_radius=0,
            width=100,
            height=90,
            image=self.logout_img_icon,
            text='ออกจากระบบ',
            font=('Kanit Regular',14),
            compound=TOP,
            bg_color='#e32320',
            hover_color='#e32320'  # เปลี่ยนสีเมื่อ hover
           )
        logout_btn.place(x=0,y=500)
        
        self.allcon_frame = ctk.CTkCanvas(self.store)
        self.allcon_frame.place(x=100,y=0,width=1820,height=1080)

        self.home_page()
        
        
    def home_page(self):
        
        self.home_image2 = Image.open(r'D:\python_finalproject\img\icon\black\Home black.png')  # แก้ไขเส้นทางให้ถูกต้อง
        self.home_img_icon2 = ctk.CTkImage(self.home_image2, size=(80, 40))  # ปรับขนาดที่ต้องการ
        
        self.home_btn.configure(image = self.home_img_icon2,text_color='#2b2b2b') 
        
        # สร้าง Frame หลักสำหรับการแสดงข้อมูล
        container = ctk.CTkFrame(self.store, width=1920, height=1080, corner_radius=10, fg_color='white')
        container.place(x=100, y=0)

        # สร้าง Canvas
        self.scroll_canvas = tk.Canvas(container, bg='white',highlightthickness=0)
        self.scroll_canvas.place(x=5, y=10, width=1920, height=600)

        # สร้าง Scrollbar
        self.scrollbar1 = ctk.CTkScrollbar(container, orientation='vertical',hover='white'
                                           ,corner_radius=10,
                                           fg_color='white',
                                           bg_color='white',button_color='white',
                                           width=18,height=100
                                           ,command=self.scroll_canvas.yview)
        
        self.scrollbar1.place(x=1915, y=10)
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar1.set)

        # สร้าง Frame ภายใน Canvas
        self.main_con = tk.Frame(self.scroll_canvas, bg='white')

        self.scroll_canvas.create_window((0, 0), window=self.main_con, anchor='nw')

        # อัปเดต scrollregion ของ Canvas
        self.scroll_canvas.bind("<Configure>", lambda e: self.scroll_canvas.configure(scrollregion=self.main_con.bbox("all")))

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
        
        self.header_frame = ctk.CTkFrame(self.main_con,fg_color='#2b2b2b',width=1920,height=50)
        self.header_frame.grid(row =0,column = 0,sticky = NSEW)
                
        self.ads_frame = ctk.CTkFrame(self.main_con,fg_color='#2b2b2b',width=400,height=250)
        self.ads_frame.grid(row =1,column = 0,pady= 5,sticky = NSEW)
        
        self.search_con = ctk.CTkFrame(self.main_con,width=1080,height=40)
        self.search_con.grid(row = 2 , column= 0,sticky =NSEW,pady= 8,padx =20)
        self.et_search = ctk.CTkEntry(self.search_con,text_color="black",fg_color='white',width=200,height=35)
        self.et_search.place(x = 0,y=2)       
        # สร้าง Frame สำหรับปุ่มหวย
        self.button_frame = tk.Frame(self.main_con, bg='white')
        self.button_frame.grid(row=3, column=0,padx=20,sticky = NSEW,pady = 8)  # วางอยู่ที่แถว 0 ของ main_con

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
        self.frame_item_con.grid(row = 4,column =0,sticky = NSEW)        
        
        self.allLot()
        
    def clear_frameItem_con(self):
        self.frame_item_con
        for widget in  self.frame_item_con.winfo_children():
            widget.destroy()
        
        
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
            self.c.execute('SELECT img_lottery, type_lottery FROM lottery')
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
            self.c.execute("SELECT img_lottery, type_lottery FROM lottery WHERE type_lottery ='หวยคู่' ")
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
            self.c.execute("SELECT img_lottery, type_lottery FROM lottery WHERE type_lottery ='หวยเดี่ยว' ")
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
            for j in range(5):  # กำหนดจำนวนคอลัมน์
                if index < len(typelot):
                    img_data, typelot_data = typelot[index]

                    # แปลงข้อมูล BLOB เป็นภาพ
                    img1 = Image.open(io.BytesIO(img_data))
                    img1 = img1.resize((160, 83))
                    photo1 = ImageTk.PhotoImage(img1)

                    # สร้างกรอบสำหรับสินค้า
                    frame_item = ctk.CTkFrame(self.frame_item_con, width=185, height=146, corner_radius=10, fg_color='#2b2b2b')
                    frame_item.grid(row =i,column =j,padx =26,pady =10)
                    self.frame_item_con.configure(width=980, height=1920)

                    # ใส่รูปภาพในกรอบสินค้า
                    label_image = tk.Label(frame_item, image=photo1)
                    label_image.image = photo1  # เก็บ reference ให้กับ image
                    label_image.place(x=10, y=25)

                    # แสดงประเภทหวย
                    typelot_label = tk.Label(frame_item, text=typelot_data, font=('Prompt', 8), fg='white', bg='#2b2b2b', width=9)
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

    def cart_page(self):
       
        pass  
    
    def profile_page(self): 
        pass        
            
# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    root = tk.Tk()
    app = All_lotery(root)
    root.mainloop()
