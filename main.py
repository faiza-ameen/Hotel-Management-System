from tkinter import *
from tkinter import ttk, Canvas
from tkinter import messagebox

from PIL import Image, ImageTk
import datetime

from abc import ABC, abstractmethod

from customer import buttons
from book import button
from details import info
from chatbot import chatbot
import employees 

import mysql.connector
from mysql.connector.errors import IntegrityError

class window(ABC):
    def __init__(self,root):
        self.root = root
        self.root.title("Home page")
        self.root.geometry("1500x780+0+0")
        self.root.state("zoomed")

class page(window):
    def __init__(self,root):
        super().__init__(root)

        #creating the frame or div
        self.frame = Frame(self.root, bg="#e8e2e2", width= 1600, height= 800)
        self.frame.place(x = 0, y=0)

        #creating secind frame for image place ment
        self.frame2 = Frame(self.root, bg="white", width= 1600, height= 105)
        self.frame2.place(x = 0, y=0)

        # adding top image
        #in python you have to convert it to back slash we can do it manually or add the r at start of image path
        self.top_path = r"D:\python\sem 2\project\images\hi.png"
        self.top = Image.open(self.top_path)
        self.top = self.top.resize((173, 105), Image.Resampling.LANCZOS)  #provide scaling
        self.top_image = ImageTk.PhotoImage(self.top)

        self.toplabel = Label(self.frame2, image = self.top_image, bg = "white")
        self.toplabel.place(x = 710, rely=0)

    def room_details(self):
        self.new_win = Toplevel(self.root)
        self.app = button(self.new_win)

    def rooms(self):
        self.new_win = Toplevel(self.root)
        self.app = info(self.new_win)

    def cust_info(self):
        self.new_win = Toplevel(self.root)
        self.app = buttons(self.new_win)


    def logout(self):
        lout = messagebox.askyesno("Logout", "Do you want to logout?")
        if lout>0:
            self.root.destroy()
        else:
            return

class mainframe(page):
    def __init__(self, root):
        super().__init__(root)
        self.frame3 = Frame(self.frame, bg="black", width=1600, height = 675)
        self.frame3.place(x = 0, y = 120)

        self.side1_path = r"D:\python\sem 2\project\images\ji.jpg"
        self.side1 = Image.open(self.side1_path)
        self.side1 = self.side1.resize((591, 670), Image.Resampling.LANCZOS)  #provide scaling
        self.side1_image = ImageTk.PhotoImage(self.side1)

        self.side1label = Label(self.frame3, image = self.side1_image, bg = "black")
        self.side1label.place(x = 950, y=0)

        #adding welcome note
        self.start = Label(self.frame3 , text = "Welcome\n to\n Stanford Hotel", font=("times new roman",40,"bold"), fg="white", bg="black")
        self.start.place(x = 280, y= 210)

        self.start = Label(self.frame3 , text = " Where Comfort Meets Class.", font=("times new roman",16,"bold"), fg="white", bg="black")
        self.start.place(x = 320, y= 410)
       
        #create buttons for new windows based on the selection and placing it in frame 1
        cust=Button(self.frame2,text="Customers",width=20,font=("times new roman",14,"bold"),command=self.cust_info,
                    bg="white",fg="black",bd=0,cursor="hand2", activebackground="white")
        cust.place(x = 200, y = 35)

        room=Button(self.frame2,text="Bookings",command = self.room_details, width=10,font=("times new roman",14,"bold"),
                    bg="white",fg="black",bd=0,cursor="hand2", activebackground="white")
        room.place(x = 400, y = 35)

        details=Button(self.frame2,text="Rooms",command=self.rooms, width=10,font=("times new roman",14,"bold"),bg="white",fg="black",bd=0,cursor="hand2", activebackground="white")
        details.place(x =550, y=35)

        attendance=Button(self.frame2,text="Employees",command=self.emp_info, width=10,font=("times new roman",14,"bold"),bg="white",fg="black",bd=0,cursor="hand2", activebackground="white")
        attendance.place(x =950, y=35)

        chat = Button(self.frame2, text="Chatbot",command=self.open_chatbot,
                  font=("times new roman", 14, "bold"),
                  bg="white", fg="black", bd=0, cursor="hand2")
        chat.place(x=1130, y=35)

        report=Button(self.frame2,text="Logout",command=self.logout, width=10,font=("times new roman",14,"bold"),bg="white",fg="black",bd=0,cursor="hand2", activebackground="white")
        report.place(x = 1250, y =35)  

    def open_chatbot(self):
        chat_root = Toplevel(self.root)
        chatbot(chat_root)     
    
    def emp_info(self):
        employees.system_run(self.root)

if __name__== "__main__":
    root = Tk()
    app = mainframe(root)
    root.mainloop()