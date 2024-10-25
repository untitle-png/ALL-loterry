import tkinter as tk
import sqlite3
import ALLregistration
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter.messagebox

class All_lotery:
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
           
            self.c.execute('''CREATE TABLE IF NOT EXISTS lotery(id integer PRIMARY KEY,
                type varchar(30) NOT NULL,
                num_id text NOT NULL,
                price varchar(30) NOT NULL,
                value varchar(30) NOT NULL,
                img BLOB NOT NULL)''')
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
        self.image = Image.open('img/Dark Grey and Green Neon Modern Bold Payment Mobile App Presentation.png')
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
            self.create_store_ui()
            self.root.destroy()

    def store(self):
        pass

    def signup_form(self):
        self.signup_ui = tk.Toplevel(self.root)
        self.signup_ui.geometry("960x540")
        self.bg = tk.Frame(self.signup_ui, bg="white", width=1920, height=1080)
        self.bg.pack()
        
        self.image_signup = Image.open('img/signup_form.png')
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
    
    def find_lot(self):
        self.find_lotery = self.et_find.get()
        if self.find_lotery in self.stock:
            y_position = 120  
            for i, stock_item in enumerate(self.stock):
                tk.Frame(self.store, width=420, height=70, bg="lightgray").place(x=220, y=y_position)
                tk.Label(self.store, text=f"Lottery No: {stock_item}", font=("Arial", 15), bg="lightgray").place(x=230, y=y_position)
                y_position += 100  
    
    def main_store_ui(self):
        self.root.destroy()
        self.store= tk.Tk()
        self.store.geometry("1920x1080")
        tk.Label(self.store,text = "MENU",font=25).place(x=400,y=2)
        tk.Frame(self.store,width=420,height=50,bg="black").place(x=220,y=50) 
        self.et_find = tk.Entry(self.store,width=25,font= 25 ,justify='center')
        self.et_find.place(x=280,y=60)
        tk.Button(self.store,width=6,text='search',borderwidth=0,border=0,bg='#4be89a',fg='white',font='2',command=self.find_lot).place(x=550,y=58)
        
        y_position = 120  
        for i, stock_item in enumerate(self.stock):
            tk.Frame(self.store, width=420, height=70, bg="lightgray").place(x=220, y=y_position)
            tk.Label(self.store, text=f"Lottery No: {stock_item}", font=("Arial", 15), bg="lightgray").place(x=230, y=y_position)
            y_position += 100  

if __name__ == "__main__":
    root = tk.Tk()
    app = All_lotery(root)
    root.mainloop()
