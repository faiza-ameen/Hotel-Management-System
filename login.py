#line 175
from tkinter import *
from tkinter import ttk, Canvas
from tkinter import messagebox

from PIL import Image, ImageTk      #importing images

from abc import ABC, abstractmethod

import mysql.connector

from main import mainframe

#======================================================DONE========================================================

#creating only one function to open multiple tabs and calling them
def main():
    win = Tk()
    app = signup(win)
    win.mainloop()

    

class Login(ABC):
    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1500x780+0+0")
        self.root.state("zoomed")

        @abstractmethod
        def showe(self):
            pass

        @abstractmethod
        def hid(self):
            pass

        @abstractmethod
        def noentry(self):
            pass

        #creating variables
        self.var_first = StringVar()
        self.var_last = StringVar()
        self.var_email = StringVar()
        self.var_pas = StringVar()
        self.var_conpas = StringVar()

class page(Login):
        def __init__(self,root):
            super().__init__(root)

            #creatinh the loginframe or div
            self.frame = Frame(self.root, bg="#040405", width= 1600, height= 800)
            self.frame.place(x = 0, y=0)

            # adding side image
            #in python you have to convert it to back slash we can do it manually or add the r at start of image path
            self.side_path = r"D:\python\sem 2\project\images\front.jpg"
            self.side = Image.open(self.side_path)
            self.side = self.side.resize((750, 800), Image.Resampling.LANCZOS)  #provide scaling
            self.side_image = ImageTk.PhotoImage(self.side)

            self.sidelabel = Label(self.frame, image = self.side_image, bg = "black")
            self.sidelabel.place(x=0, y=0)


            self.start = Label(self.frame , text = "Sign In to Stanford Hotel", font=("yu gothic ui",20,"bold"), fg="white", bg="black")
            self.start.place(x= 1000, y=150)

class Username(page):
         def __init__(self,root):
            super().__init__(root)

            #adding username label and its box
            self.user = Label(self.frame , text = "Username:", font=("yu gothic ui",16,"bold"), fg="white", bg="black")
            self.user.place(x= 950, y=250)

            #enter
            self.userentry = Entry(self.frame ,textvariable=self.var_email, highlightthickness=0,insertbackground="white", relief=FLAT, font=("yu gothic ui",14,"bold"), fg="#6b6a69", bg="black")
            self.userentry.place(x= 980, y=300)

            #entry canvas
            self.userline = Canvas(self.frame, width=400, height=2.0, bg="#bdb9b1", highlightthickness=0)
            self.userline.place(x=950,y=330)

            #usernamelogo
            self.logo_path = r"D:\python\sem 2\project\images\icon.png"
            self.logo = Image.open(self.logo_path)
            self.logo = self.logo.resize((20, 20), Image.Resampling.LANCZOS)  #provide scaling
            self.logo_image = ImageTk.PhotoImage(self.logo)

            self.logolabel = Label(self.frame, image = self.logo_image, bg = "black")
            self.logolabel.place(x=950, y=300)
                
class Password(Username):
        def __init__(self, root):
            super().__init__(root)

            #adding password label and its box
            self.pas = Label(self.frame, text="Password:", font=("yu gothic ui",16,"bold"), fg="white", bg="black") 
            self.pas.place(x=950, y = 380)

            #enter
            self.pasentry = Entry(self.frame,textvariable=self.var_pas, highlightthickness=0,insertbackground="white", relief=FLAT, font=("yu gothic ui", 14, "bold"), fg = "#6b6a69", bg="black", show="*")
            self.pasentry.place(x=980, y = 430)

            #entrycanvas
            self.pasline = Canvas(self.frame, width=400, height=2.0, bg="#bdb9b1", highlightthickness=0)
            self.pasline.place(x=950, y= 460)
        
            #passwordlogo
            self.pas_path = r"D:\python\sem 2\project\images\passo.png"
            self.pas = Image.open(self.pas_path)
            self.pas = self.pas.resize((20, 20), Image.Resampling.LANCZOS)  #provide scaling
            self.pas_image = ImageTk.PhotoImage(self.pas)

            self.paslabel = Label(self.frame, image = self.pas_image, bg = "black")
            self.paslabel.place(x=950, y=425)

            #showing the password
            self.show_path = r"D:\python\sem 2\project\images\show.png"
            self.show = Image.open(self.show_path)
            self.show = self.show.resize((30, 20), Image.Resampling.LANCZOS)  #provide scaling
            self.show_image = ImageTk.PhotoImage(self.show)
            self.showlabel = Button(self.frame, image = self.show_image, fg="white", bd=0, cursor="hand2",activebackground="black",
                                 bg = "black", width=25, command=self.showe)
            self.showlabel.place(x=1310, y=430)


            #hiding the password
            self.hide_path = r"D:\python\sem 2\project\images\hide.png"
            self.hide = Image.open(self.hide_path)
            self.hide = self.hide.resize((30, 20), Image.Resampling.LANCZOS)  #provide scaling
            self.hide_image = ImageTk.PhotoImage(self.hide)

        def showe(self):
            self.hidelabel = Button(self.frame, image = self.hide_image, fg="white", bd=0, cursor="hand2",activebackground="black",
                                 bg = "black", width=25, command=self.hid)
            self.hidelabel.place(x=1310, y=430)

            self.pasentry.config(show="")

        def hid(self):
            self.showlabel = Button(self.frame, image = self.show_image, fg="white", bd=0, cursor="hand2",activebackground="black",
                                 bg = "black", width=25, command=self.showe)
            self.showlabel.place(x=1310, y=430)
            
            self.pasentry.config(show="*")
        

class loginbutton(Password):
    def __init__(self, root):
            super().__init__(root)

            #adding login bg
            self.log_path = r"D:\python\sem 2\project\images\lo.png"
            self.log = Image.open(self.log_path)
            self.log = self.log.resize((500, 100), Image.Resampling.LANCZOS)  #provide scaling
            self.log_image = ImageTk.PhotoImage(self.log)

            self.loglabel = Label(self.frame, image = self.log_image, bg = "black")
            self.loglabel.place(x=900, y=500)

            #adding login button
            self.login = Button(self.loglabel, text = "LOGIN" , font = ("yu gothic ui", 14 , "bold"),width=20, bd=0, cursor="hand2",activebackground="white",
                                 bg = "white", command=self.no)
            self.login.place(x=130, y= 40)

    def no(self):
            if self.userentry.get() == "" or self.pasentry.get() == "":
                messagebox.showerror("ERROR!","All fields should be filled.")
                return
            
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="Faiza_065", database="hotel_management") #connectivity of data base
                cur = con.cursor()
                #check if user exists

                query = "SELECT * FROM register WHERE email = %s AND password = %s"
                params = (self.var_email.get(), self.var_pas.get())
                
                cur.execute(query, params)
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("ERROR", "Either email or password is incorrect.")
                                
                else:
                    self.new_window = Toplevel(self.root)
                    self.app = mainframe(self.new_window)
                con.close()

            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

class forget(loginbutton):
    def __init__(self,root):
        super().__init__(root)

        #forgotten password button
        self.forgot = Button(self.frame, text = "Forgot Password?" ,command=self.forpas, font = ("yu gothic ui", 14 , "bold underline"),
                                fg="white", bd=0, cursor="hand2",activebackground="black",
                                bg = "black", width=25)
        self.forgot.place(x=1010, y= 610)

    def forpas(self):
        if self.userentry.get() == "":
            messagebox.showerror("Error", "Please enter username to reset password.")
            return
        
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Faiza_065",
                database="hotel_management"
            )
            cur = con.cursor()

            # Assuming user enters email as username
            email = self.userentry.get()  
            query = "SELECT * FROM register WHERE email = %s"
            cur.execute(query, (email,))
            row = cur.fetchone()

            # You can proceed to reset password
            if row == None:
                messagebox.showerror("Error", "Enter the valid user name.")
                
            else:
                con.close()

                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("500x400+500+200")
                self.root2.config(bg="#040405")
                self.root2.resizable(False, False)

                # Centered layout frame
                frame = Frame(self.root2, bg="#040405", width=400, height=300)
                frame.place(relx=0.5, rely=0.5, anchor="center")

                # Title
                title = Label(frame, text="Reset Your Password", fg="white", bg="#040405",
                            font=("yu gothic ui", 18, "bold"))
                title.place(relx=0.5, y=20, anchor="center")

                # New Password Label + Entry
                newlabel = Label(frame, text="New Password:", font=("yu gothic ui", 13),
                                fg="white", bg="#040405")
                newlabel.place(x=50, y=80)

                self.newentry = Entry(frame, font=("yu gothic ui", 12), bg="black",
                                    fg="white", insertbackground="white", relief=FLAT, width=25)
                self.newentry.place(x=50, y=110)

                Canvas(frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0).place(x=50, y=135)

                # Confirm Password Label + Entry
                conlabel = Label(frame, text="Confirm Password:", font=("yu gothic ui", 13),
                                    fg="white", bg="#040405")
                conlabel.place(x=50, y=160)

                self.conentry = Entry(frame, font=("yu gothic ui", 12), bg="black",
                                        fg="white", insertbackground="white", relief=FLAT, width=25)
                self.conentry.place(x=50, y=190)

                Canvas(frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0).place(x=50, y=215)

                # Reset Button
                resbtn = Button(frame, text="Reset Password", font=("yu gothic ui", 12, "bold"),
                                fg="white", bg="black", activebackground="#444444",
                                activeforeground="white", cursor="hand2", command=self.reset_password)
                resbtn.place(relx=0.5, y=260, anchor="center")

        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def reset_password(self):
        if self.newentry.get() == "":
            messagebox.showerror("Error", "Enter new password", )
        elif self.newentry.get() != self.conentry.get():
            messagebox.showerror("Error", "New password and confirm password must be same")
        else:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Faiza_065",
                database="hotel_management"
            )
            cur = con.cursor()  
            query = "Update register set password= %s where email = %s"
            value = (self.newentry.get(), self.userentry.get())
            cur.execute(query, value)

            con.commit()
            con.close()
            messagebox.showinfo("Success", "Password reset successfully!")
            self.root2.destroy()


class signup(forget):
        def __init__(self, root):
            super().__init__(root)

            #creating sign up page
            self.signup = Button(self.frame, text = "No account yet?" , font = ("yu gothic ui", 14 , "bold"),
                                 fg="white", bd=0,activebackground="black",
                                 bg = "black", width=25)
            self.signup.place(x=890, y=690)
            #regiter background
            self.reg_path = r"D:\python\sem 2\project\images\lo.png"
            self.reg = Image.open(self.reg_path)
            self.reg = self.reg.resize((180, 90), Image.Resampling.LANCZOS)  #provide scaling
            self.reg_image = ImageTk.PhotoImage(self.reg)

            self.reglabel = Label(self.frame, image = self.reg_image, bg="black")
            self.reglabel.place(x=1100, y=650)

            #regiter text
            self.reg = Button(self.reglabel, text = "REGISTER" ,command=self.tabopen , font = ("yu gothic ui", 14 , "bold"), bd=0, cursor="hand2",activebackground="white",
                                 bg = "white", fg="black")
            self.reg.place(x = 39, y = 35)
            
        #helps in opening new window
        def tabopen(self):
            self.new_window = Toplevel(self.root)#top level is already present in python
            self.app = done(self.new_window)

            


#register tab
class register(ABC):
    def __init__(self,root):
        self.root = root
        self.root.title("Register page")
        self.root.geometry("1500x780+0+0")
        self.root.state("zoomed")

        self.frame = Frame(self.root, bg="#221d19", width= 1600, height= 800)
        self.frame.place(x = 0, y=0)

        #====================================creating variables for each entry====================================
        self.var_first = StringVar()
        self.var_last = StringVar()
        self.var_email = StringVar()
        self.var_pas = StringVar()
        self.var_conpas = StringVar()

        # adding side image
        self.side_path = r"D:\python\sem 2\project\images\rcep.jpg"
        self.side = Image.open(self.side_path)
        self.side = self.side.resize((800, 800), Image.Resampling.LANCZOS)  #provide scaling
        self.side_image = ImageTk.PhotoImage(self.side)

        self.sidelabel = Label(self.frame, image = self.side_image, bg = "#221d19")
        self.sidelabel.place(x=740, y=0)

        self.start = Label(self.frame, text = "Register to Stanford Hotel", font=("yu gothic ui",20,"bold"), fg="white", bg="#221d19")
        self.start.place(x= 190, y=70)

        @abstractmethod
        def showe(self):
            pass

        @abstractmethod
        def hid(self):
            pass

        @abstractmethod
        def regster_data(self):
            pass

class acc(register):
    def __init__(self, root):
        super().__init__(root)

        self.acc = Label(self.frame, text = "Already have an account?", font=("yu gothic ui",10,"bold"), fg="white", bg="#221d19")
        self.acc.place(x= 130, y=160)

        #regiter text
        self.acc = Button(self.frame, text="Login",command=self.des, font=("yu gothic ui", 10, "bold", "underline"), bd=0, cursor="hand2",
                  activebackground="#221d19", fg="white", bg="#221d19")
        self.acc.place(x = 300, y = 157)

    def des(self):
        self.root.destroy()

class new(acc):
    def __init__(self, root):
        super().__init__(root)

        self.acc = Label(self.frame, text = "Create A New Account", font=("yu gothic ui",16,"bold"), fg="white", bg="#221d19")
        self.acc.place(x= 130, y=210)


class first(new):
    def __init__(self, root):
        super().__init__(root)
        self.first = Label(self.frame , text = "First Name:", font=("yu gothic ui",14,"bold"), fg="white", bg="#221d19")
        self.first.place(x= 130, y=290)

        #enter
        self.firstentry = Entry(self.frame ,text = self.var_first , highlightthickness=0, relief=FLAT,insertbackground="white",
                                 font=("yu gothic ui",12,"bold"), fg="#6b6a69", bg="#221d19",)
        self.firstentry.place(x= 130, y=360)

        #entry canvas
        self.firstline = Canvas(self.frame, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.firstline.place(x=130,y=390)

class last(first):
    def __init__(self,root):
        super().__init__(root)
        self.last = Label(self.frame , text = "Last Name:", font=("yu gothic ui",14,"bold"), fg="white", bg="#221d19")
        self.last.place(x= 400, y=290)

        #enter
        self.lastentry = Entry(self.frame , text = self.var_last, highlightthickness=0, relief=FLAT,insertbackground="white",
                                font=("yu gothic ui",12,"bold"), fg="#6b6a69", bg="#221d19")
        self.lastentry.place(x= 400, y=360)

        #entry canvas
        self.lastline = Canvas(self.frame, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.lastline.place(x=400,y=390)

class email(last):
    def __init__(self,root):
        super().__init__(root)
        self.email = Label(self.frame , text = "Email Address:", font=("yu gothic ui",14,"bold"), fg="white", bg="#221d19")
        self.email.place(x= 130, y=430)

        #enter
        self.emailentry = Entry(self.frame ,text = self.var_email, highlightthickness=0, relief=FLAT,insertbackground="white",
                                 font=("yu gothic ui",12,"bold"), fg="#6b6a69", bg="#221d19")
        self.emailentry.place(x= 130, y=480)

        #entry canvas
        self.emailline = Canvas(self.frame, width=470, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.emailline.place(x=130,y=510)  
        
         

class pas(email):
    def __init__(self, root):
        super().__init__(root)
        self.pas = Label(self.frame , text = "Password:", font=("yu gothic ui",14,"bold"), fg="white", bg="#221d19")
        self.pas.place(x= 130, y=550)

        #enter
        self.pasentry = Entry(self.frame ,text = self.var_pas, highlightthickness=0, relief=FLAT,insertbackground="white",
                               font=("yu gothic ui",12,"bold"), fg="#6b6a69", bg="#221d19")
        self.pasentry.place(x= 130, y=600)

        #entry canvas
        self.pasline = Canvas(self.frame, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.pasline.place(x=130,y=630)

        self.conpas = Label(self.frame , text = "Confirm Password:", font=("yu gothic ui",14,"bold"), fg="white", bg="#221d19")
        self.conpas.place(x= 400, y=550)

        #enter
        self.conpasentry = Entry(self.frame ,text = self.var_conpas, highlightthickness=0, relief=FLAT,insertbackground="white",
                                  font=("yu gothic ui",12,"bold"), fg="#6b6a69", bg="#221d19")
        self.conpasentry.place(x= 400, y=600)

        #entry canvas
        self.conpasline = Canvas(self.frame, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.conpasline.place(x=400,y=630)

class hide(pas):
    def __init__(self,root):
        super().__init__(root)
        self.show_path = r"D:\python\sem 2\project\images\show.png"
        self.show = Image.open(self.show_path)
        self.show = self.show.resize((30, 20), Image.Resampling.LANCZOS)  #provide scaling
        self.show_image = ImageTk.PhotoImage(self.show)
        self.showlabel = Button(self.frame, image = self.show_image, fg="white", bd=0, cursor="hand2",activebackground="#221d19",
                                 bg = "#221d19", width=25, command=self.showe)
        self.showlabel.place(x=300, y=600)


        #hiding the password
        self.hide_path = r"D:\python\sem 2\project\images\hide.png"
        self.hide = Image.open(self.hide_path)
        self.hide = self.hide.resize((30, 20), Image.Resampling.LANCZOS)  #provide scaling
        self.hide_image = ImageTk.PhotoImage(self.hide)

    def showe(self):
        self.hidelabel = Button(self.frame, image = self.hide_image, fg="white", bd=0, cursor="hand2",activebackground="#221d19",
                                 bg = "#221d19", width=25, command=self.hid)
        self.hidelabel.place(x=300, y=600)
        self.pasentry.config(show="")

        self.hidelabel = Button(self.frame, image = self.hide_image, fg="white", bd=0, cursor="hand2",activebackground="#221d19",
                                 bg = "#221d19", width=25, command=self.hid)
        self.hidelabel.place(x=570, y=600)
        self.conpasentry.config(show="")

    def hid(self):
        self.showlabel = Button(self.frame, image = self.show_image, fg="white", bd=0, cursor="hand2",activebackground="#221d19",
                                 bg = "#221d19", width=25, command=self.showe)
        self.showlabel.place(x=300, y=600)
        self.pasentry.config(show="*")


        self.showlabel = Button(self.frame, image = self.show_image, fg="white", bd=0, cursor="hand2",activebackground="#221d19",
                                 bg = "#221d19", width=25, command=self.showe)
        self.showlabel.place(x=570, y=600)
        self.conpasentry.config(show="*")

    

class done(hide):
    def __init__(self, root):
        super().__init__(root)

        #adding login bg
        self.log_path = r"D:\python\sem 2\project\images\lo.png"
        self.log = Image.open(self.log_path)
        self.log = self.log.resize((500, 100), Image.Resampling.LANCZOS)  #provide scaling
        self.log_image = ImageTk.PhotoImage(self.log)

        self.loglabel = Label(self.frame, image = self.log_image, bg = "#221d19")
        self.loglabel.place(x=130, y=635)

         #adding login button
        self.login = Button(self.loglabel, text = "SIGN UP" , font = ("yu gothic ui", 14 , "bold"),width=20, bd=0, cursor="hand2",activebackground="white",
                                 bg = "white", command=self.sign)
        self.login.place(x=130, y= 40)

    def regster_data(self):
        if self.firstentry.get()=="" or self.lastentry.get()=="" or self.emailentry.get()=="" or self.pasentry.get()=="" or self.conpasentry.get()=="":
            messagebox.showerror("Error", "All fields must be filled.")

        if self.pasentry.get() != self.conpasentry.get():
            messagebox.showerror("Error", "Password and Confirm password must match.")
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="Faiza_065", database="hotel_management") #connectivity of data base
                cur = con.cursor() #adding data

                #check if user exists

                query = ("SELECT * FROM register WHERE email = %s")
                value = (self.var_email.get(),)
                cur.execute(query,value)
                row = cur.fetchone()

                if row == NONE:
                    messagebox.showerror("ERROR", "User must enter his credentials.")
                    return
                
                query = ("SELECT emp_id FROM employee WHERE email=%s")
                value =  (self.var_email.get(),)
                cur.execute(query,value)
                employee = cur.fetchone()
                if not employee:
                    messagebox.showerror("Error", "Only employees can register. Email not found in employee table.")
                    con.close()
                    return

                employee_id = employee[0]

                
                cur.execute("INSERT INTO register (emp_id, firstname, lastname, email, password) values(%s,%s, %s,%s,%s)", (
                                                                            employee_id,
                                                                            self.var_first.get(),
                                                                            self.var_last.get(),
                                                                            self.var_email.get(),
                                                                            self.var_pas.get()

                                                                            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registered successfully.")

            except mysql.connector.Error as err:
                # messagebox.showerror("Error","Only employees can register to this system.")
                return


        self.regster_data()
        self.des()

    def sign(self):
        self.regster_data()
        self.des()

if __name__ == "__main__":
    main()