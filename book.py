from tkinter import *
from tkinter import ttk, Canvas
from tkinter import messagebox

from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import random
import mysql.connector

import mysql.connector

class Database:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Faiza_065",
            database="hotel_management"
        )
        self.cur = self.con.cursor()

    def fetchone(self, query, params):
        self.cur.execute(query, params)
        return self.cur.fetchone()

    def fetchall(self, query, params=None):
        self.cur.execute(query, params or ())
        return self.cur.fetchall()

    def execute(self, query, params):
        self.cur.execute(query, params)
        self.con.commit()

    def close(self):
        self.cur.close()
        self.con.close()

class rooms(Database):
    def __init__(self,root):
        self.root = root
        self.root.title("Stay details")
        self.root.geometry("1520x670+0+130")

        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()
        #email and password from reguster table
        self.var_email = StringVar()
        self.var_password = StringVar()

        self.frame = Frame(self.root, bg="#221d19", width= 1600, height= 800)
        self.frame.place(x = 0, y=0)

        #add customer details
        self.start = Label(self.root , text = "Room Booking Details", font=("times new roman",28,"bold"), fg="white", bg="#221d19")
        self.start.place(x = 600, y= 30)

        self.line = Label(self.root , text = "__________________________________________________________________________________________________________________________________________________________________",
                            font=("times new roman",28,"bold"), fg="white", bg="#221d19")
        self.line.place(x = 0, y= 76)

        
    # def login(self):
    #         db = Database()
    #         cur = db.cur
    #         cur.execute("SELECT * FROM register WHERE email=%s AND password=%s", (self.var_email.get(), self.var_password.get()))
    #         row = cur.fetchone()
    #         if row:
    #             self.logged_in_email = self.var_email.get()  # SAVING THE EMAIL
    #             self.root.destroy()
    #             self.open_main_window()
    #         else:
    #             messagebox.showerror("Error", "Invalid Email or Password")


class button(rooms):
    def __init__(self, root): #, logged_in_email
        super().__init__(root)
        # self.logged_in_email = logged_in_email

        self.left = LabelFrame(self.root, bd = 2, relief=RIDGE, text= "Room Booking Details", font=(("times new roman",16,"bold")), bg="#221d19",fg="white" , padx=2)
        self.left.place(x=50, y=135, width=590, height=510)

        # labels and their entries
        #customer contact
        self.cust_contact = Label(self.left, text= "Customer Contact:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.cust_contact.place(x=30 ,y= 10)

        self.contact = Entry(self.left,textvariable=self.var_contact, width=21,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.contact.place(x= 250, y=15)

        #fetching the data
        btn1 = Button(self.left, text="Fetch",command=self.fetchcontact, font=("times new roman",14,"bold"), bg="#221d19", fg="green", width=7, activebackground="#221d19")
        btn1.place(x = 455, y = 8)

        #check in date
        self.check_in_date = Label(self.left, text= "Check-in Date:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.check_in_date.place(x=30 ,y= 50)

        self.checkin_date = Entry(self.left,textvariable=self.var_checkin, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.checkin_date.place(x= 250, y=55)

        #check out date
        self.check_out_date = Label(self.left, text= "Check-out Date:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.check_out_date.place(x=30 ,y= 90)

        self.checkout_date = Entry(self.left,textvariable=self.var_checkout, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.checkout_date.place(x=250, y=95)

        #room type
        self.room_type = Label(self.left, text= "Room Type:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.room_type.place(x=30 ,y= 130)


        style = ttk.Style()
        style.theme_use("default")  # Needed for full control over styling

        style.configure("CustomCombobox.TCombobox",
                            fieldbackground="#221d19",  # Inside area
                            background="#221d19",       # Drop-down background
                            foreground="white",       # Text color
                            arrowcolor="white",       # Arrow color
                            borderwidth=1)

        # Your combobox with custom style
        self.roomtype = ttk.Combobox(self.left,textvariable=self.var_roomtype, width=31, font=("Times New Roman", 14),
                                    values=("Single", "Double", "Luxury"),
                                    style="CustomCombobox.TCombobox")
        self.roomtype.place(x= 250, y=135)

        #Available room
        self.room_availablity = Label(self.left, text= "Available Room:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.room_availablity.place(x=30 ,y= 170)

        #creating data base to show the rooms type
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Faiza_065",
            database="hotel_management"
        )
        cur = con.cursor()
        cur.execute("SELECT roomno FROM room")
        row = cur.fetchall()

        style = ttk.Style()
        style.theme_use("default")  # Needed for full control over styling

        style.configure("CustomCombobox.TCombobox",
                            fieldbackground="#221d19",  # Inside area
                            background="#221d19",       # Drop-down background
                            foreground="white",       # Text color
                            arrowcolor="white",       # Arrow color
                            borderwidth=1)

        # Your combobox with custom style
        self.available_room = ttk.Combobox(self.left,textvariable=self.var_roomavailable, width=31, font=("Times New Roman", 14),
                                    values=row,
                                    style="CustomCombobox.TCombobox")
        self.available_room.place(x= 250, y=175)

        #Meal
        self.meal = Label(self.left, text= "Meal:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.meal.place(x=30 ,y= 210)

        style = ttk.Style()
        style.theme_use("default")  # Needed for full control over styling

        style.configure("CustomCombobox.TCombobox",
                            fieldbackground="#221d19",  # Inside area
                            background="#221d19",       # Drop-down background
                            foreground="white",       # Text color
                            arrowcolor="white",       # Arrow color
                            borderwidth=1)

        # Your combobox with custom style
        self.meal_asked = ttk.Combobox(self.left,textvariable=self.var_meal, width=31, font=("Times New Roman", 14),
                                    values=("none", "Breakfast", "Lunch", "Dinner"),
                                    style="CustomCombobox.TCombobox")
        self.meal_asked.place(x= 250, y=215)
        
        #No. of days
        self.number_days = Label(self.left, text= "No. of days:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.number_days.place(x=30 ,y= 250)

        self.days_entry = Entry(self.left,textvariable=self.var_noofdays, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.days_entry.place(x=250, y=255)

        #paid tax
        self.paid_tax = Label(self.left, text= "Paid Tax:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.paid_tax.place(x=30 ,y= 290)

        self.tax = Entry(self.left,textvariable=self.var_paidtax, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.tax.place(x=250, y=295)

        #Sub Total
        self.sub_total = Label(self.left, text= "Actual Cost:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.sub_total.place(x=30 ,y= 330)

        self.total = Entry(self.left,textvariable=self.var_actualtotal, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.total.place(x= 250, y=335)

        #Total cost
        self.total_cost = Label(self.left, text= "Total cost:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.total_cost.place(x=30 ,y= 370)

        self.cost = Entry(self.left,textvariable=self.var_total, width=21,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.cost.place(x= 250, y=375)

        #billing button that will make our noof days correct
        btn0 = Button(self.left, text="Bill",command=self.time, font=("times new roman",14,"bold"), bg="#221d19", fg="white", width=7, activebackground="#221d19")
        btn0.place(x = 455, y = 366)

        btn = Frame(self.left, bd=2, relief=RIDGE, background="#221d19")
        btn.place(x=0, y=410, width=582,height=70)

        btn1 = Button(btn, text="Add",command=self.add_data, font=("times new roman",16,"bold"), bg="#221d19", fg="yellow", width=10, activebackground="#221d19")
        btn1.place(x = 10, y = 12)

        btn2 = Button(btn, text="Update",command=self.update, font=("times new roman",16,"bold"), bg="#221d19", fg="green", width=10, activebackground="#221d19")
        btn2.place(x = 150, y = 12)

        btn3 = Button(btn, text="Delete",command=self.delete, font=("times new roman",16,"bold"), bg="#221d19", fg="red", width=10, activebackground="#221d19")
        btn3.place(x = 290, y = 12)

        btn4 = Button(btn, text="Reset",command=self.reset, font=("times new roman",16,"bold"), bg="#221d19", fg="orange", width=10, activebackground="#221d19")
        btn4.place(x = 430, y = 12)

        #=====================adding table=======================

        self.table = LabelFrame(self.root, bd = 2, relief=RIDGE, text= "Search And View Details", font=(("times new roman",16,"bold")), bg="#221d19",fg="white" , padx=2)
        self.table.place(x=690, y=350, width=800, height=294)

        self.searchby = Label(self.table, text= "Search By:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white")
        self.searchby.place(x=30 ,y= 15)

        self.search_var = StringVar()



        style = ttk.Style()
        style.theme_use("default")  # Needed for full control over styling

        style.configure("CustomCombobox.TCombobox",
                            fieldbackground="#221d19",  # Inside area
                            background="#221d19",       # Drop-down background
                            foreground="white",       # Text color
                            arrowcolor="white",       # Arrow color
                            borderwidth=1)

        # Your combobox with custom style
        search = ttk.Combobox(self.table ,textvariable=self.search_var, width=20, font=("Times New Roman", 14),
                                    values=("Contact", "Room"),
                                    style="CustomCombobox.TCombobox")
        search.place(x=135, y=15)

        self.txt_search=StringVar()
        self.searchentry = Entry(self.table,textvariable=self.txt_search, width=23,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.searchentry.place(x= 345, y=15)

        btnSearch = Button(self.table, text="Search",command=self.search, font=("times new roman",16,"bold"), bg="#221d19", fg="white", width=8, activebackground="#221d19")
        btnSearch.place(x = 565, y = 5)

        btnShow = Button(self.table, text="Show",command=self.fetchdata, font=("times new roman",16,"bold"), bg="#221d19", fg="white", width=8, activebackground="#221d19")
        btnShow.place(x = 680, y = 5)

        #adding images
        self.side_path = r"D:\python\sem 2\project\images\rom.jpg"
        self.side = Image.open(self.side_path)
        self.side = self.side.resize((400, 200), Image.Resampling.LANCZOS)  #provide scaling
        self.side_image = ImageTk.PhotoImage(self.side)

        self.sidelabel = Label(self.root, image = self.side_image, bg = "#221d19")
        self.sidelabel.place(x = 1080, y=140)

        #==========================table customising=======================
        
        # Frame for Treeview and Scrollbars
        details = Frame(self.table, bd=2, relief=RIDGE, bg="#221d19")
        details.place(x=20, y=60, width=750, height=200)

        # Treeview Scrollbars
        scroll_x = Scrollbar(details, orient=HORIZONTAL)
        scroll_y = Scrollbar(details, orient=VERTICAL)

        # Treeview Widget
        self.book_details = ttk.Treeview(
            details,
            columns=("booking_id","roomno", "customer_id", "emp_id", "contact", "check_in", "check_out", 
             "roomtype", "meal", "noofdays", "tax", "actualtotal", "total"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.book_details.xview)
        scroll_y.config(command=self.book_details.yview)

        # Configure headings (make sure names match column names)
        self.book_details.heading("booking_id", text="Booking Id")
        self.book_details.heading("roomno", text="Room No")
        self.book_details.heading("customer_id", text="Customer Id")
        self.book_details.heading("emp_id", text="Employee Id")
        self.book_details.heading("contact", text="Contact")
        self.book_details.heading("check_in", text="Check in")
        self.book_details.heading("check_out", text="Check out")
        self.book_details.heading("roomtype", text="Room Type")
        self.book_details.heading("meal", text="Meal")
        self.book_details.heading("noofdays", text="No of days")
        self.book_details.heading("tax", text="Tax")
        self.book_details.heading("actualtotal", text="Actual amount")
        self.book_details.heading("total", text="Total")

        self.book_details["show"] = "headings"
        self.book_details.column("booking_id", width=100)
        self.book_details.column("roomno", width=100)
        self.book_details.column("customer_id", width=100)
        self.book_details.column("emp_id", width=100)
        self.book_details.column("contact", width=100)
        self.book_details.column("check_in", width=100)
        self.book_details.column("check_out", width=100)
        self.book_details.column("roomtype", width=100)
        self.book_details.column("meal", width=100)
        self.book_details.column("noofdays", width=100)
        self.book_details.column("tax", width=100)
        self.book_details.column("actualtotal", width=100)
        self.book_details.column("total", width=100)

        self.book_details.pack(fill=BOTH, expand=1)
        self.book_details.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetchdata()

        #============creating an info table===========
        showdataframe = Frame(self.root, bd=4,relief=RIDGE, padx=2, background="#221d19")
        showdataframe.place(x=693, y=143, width=360, height=200)


    def fetchcontact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter contact number.", parent = self.root)
        else:
            #etting the name
            con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Faiza_065",
            database="hotel_management"
            )
            cur = con.cursor()
            query = ("SELECT name FROM customer WHERE mobile=%s")
            value = (self.var_contact.get(),)
            cur.execute(query, value)
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "This number has not been found.", parent = self.root)
            else:
                con.commit()
                con.close()

                showdataframe = Frame(self.root, bd=4,relief=RIDGE, padx=2, background="#221d19")
                showdataframe.place(x=693, y=143, width=360, height=200)

                lblname = Label(showdataframe, text="Name:", font=("times new roman",16,"bold"), background="#221d19", fg="white")
                lblname.place(x=3,y=6)

                lbl = Label(showdataframe, text = row, font=("times new roman", 16), fg="white", bg="#221d19")
                lbl.place(x=110, y=6)


                #getting the gender
                con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Faiza_065",
                database="hotel_management"
                )
                cur = con.cursor()
                query = ("SELECT Gender FROM customer WHERE mobile=%s")
                value = (self.var_contact.get(),)
                cur.execute(query, value)
                row = cur.fetchone()

                lblgender = Label(showdataframe, text="Gender:", font=("times new roman",16,"bold"), background="#221d19", fg="white")
                lblgender.place(x=3,y=39)

                lblgen = Label(showdataframe, text = row, font=("times new roman", 16), fg="white", bg="#221d19")
                lblgen.place(x=110, y=39)


                #getting the email
                con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Faiza_065",
                database="hotel_management"
                )
                cur = con.cursor()
                query = ("SELECT Email FROM customer WHERE mobile=%s")
                value = (self.var_contact.get(),)
                cur.execute(query, value)
                row = cur.fetchone()

                lblemail = Label(showdataframe, text="Email:", font=("times new roman",16,"bold"), background="#221d19", fg="white")
                lblemail.place(x=3,y=71)

                lblem = Label(showdataframe, text = row, font=("times new roman", 16), fg="white", bg="#221d19")
                lblem.place(x=110, y=71)

                #getting the nationality
                con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Faiza_065",
                database="hotel_management"
                )
                cur = con.cursor()
                query = ("SELECT Nationality FROM customer WHERE mobile=%s")
                value = (self.var_contact.get(),)
                cur.execute(query, value)
                row = cur.fetchone()

                lblnationality = Label(showdataframe, text="Nationality:", font=("times new roman",16,"bold"), background="#221d19", fg="white")
                lblnationality.place(x=3,y=105)

                lblnation = Label(showdataframe, text = row, font=("times new roman", 16), fg="white", bg="#221d19")
                lblnation.place(x=110, y=105)

                #getting the address
                con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Faiza_065",
                database="hotel_management"
                )
                cur = con.cursor()
                query = ("SELECT Address FROM customer WHERE mobile=%s")
                value = (self.var_contact.get(),)
                cur.execute(query, value)
                row = cur.fetchone()

                lbladdress = Label(showdataframe, text="Address:", font=("times new roman",16,"bold"), background="#221d19", fg="white")
                lbladdress.place(x=3,y=140)

                lbladd = Label(showdataframe, text = row, font=("times new roman", 16), fg="white", bg="#221d19")
                lbladd.place(x=110, y=140)

    def add_data(self):
        if not self.var_contact.get() or not self.var_checkin.get():
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
            return
        try:
            db = Database()

            customers = db.fetchall("SELECT customer_id FROM customer WHERE mobile=%s", (self.var_contact.get(),))
            if not customers:
                messagebox.showerror("Error", "Customer not found.", parent=self.root)
                db.close()
                return
            for customer in customers:
                customer_id = customer[0]

            # employees = db.fetchall("SELECT emp_id FROM register WHERE email=%s", (self.logged_in_email,))
            # if not employees:
            #     messagebox.showerror("Error", "Employee not found.", parent=self.root)
            #     db.close()
            #     return
            # for employee in employees:
            #     employee_id = employee[0]

            
            db.execute("""
                INSERT INTO booking (roomno, customer_id, emp_id, contact, check_in, check_out, roomtype, meal, noofdays, tax, actualtotal, total)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.var_roomavailable.get(),
                customer_id,
                1,
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_paidtax.get(),
                self.var_actualtotal.get(),
                self.var_total.get()
            ))

            db.execute("UPDATE room SET status='occupied' WHERE roomno=%s", (self.var_roomavailable.get(),))

            db.close()
            self.fetchdata()
            messagebox.showinfo("Success", "Booking created successfully!", parent=self.root)
        except Exception as e:
            print(str(e))
            messagebox.showerror("Error", "An unexpected error occurred.", parent=self.root)




    def get_cursor(self, event = ""):
        cursor_row= self.book_details.focus()
        content = self.book_details.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[4]),
        self.var_checkin.set(row[5])
        self.var_checkout.set(row[6])
        self.var_roomtype.set(row[7])
        self.var_roomavailable.set(row[1])
        self.var_meal.set(row[8])
        self.var_noofdays.set(row[9])
        self.var_paidtax.set(row[10])
        self.var_actualtotal.set(row[11])
        self.var_total.set(row[12])
    
    
    def update(self):
        try:
            if self.var_contact.get() == "":
                messagebox.showerror("ERROR", "Please enter mobile number.", parent = self.root)
            else:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Faiza_065",
                    database="hotel_management"
                )
                cur = con.cursor()

                 # Verify booking exists
                cur.execute("SELECT booking_id FROM booking WHERE roomno=%s",
                        (self.var_roomavailable.get(),))
                if not cur.fetchone():
                    messagebox.showerror("Error", "Booking not found")
                    return
                
                db = Database()
                customers = db.fetchall("SELECT customer_id FROM customer WHERE mobile=%s", (self.var_contact.get(),))
                if not customers:
                    messagebox.showerror("Error", "Customer not found.", parent=self.root)
                    db.close()
                    return
                for customer in customers:
                    customer_id = customer[0]

                cur.execute("""
                            UPDATE booking SET contact=%s,customer_id= %s, check_in=%s, check_out=%s, roomtype=%s,  meal=%s, noofdays=%s, tax=%s, actualtotal=%s, total=%s 
                            WHERE roomno=%s
                        """, (
                            
                            self.var_contact.get(),
                            customer_id,
                            self.var_checkin.get(),
                            self.var_checkout.get(),
                            self.var_roomtype.get(),
                            self.var_meal.get(),
                            self.var_noofdays.get(),
                            self.var_paidtax.get().replace("$", ""),
                            self.var_actualtotal.get().replace("$", ""),
                            self.var_total.get().replace("$", ""),
                            self.var_roomavailable.get(),
                            
                        ))
                con.commit()
                self.fetchdata()
                con.close()
                messagebox.showinfo("SUCCESS", "Room details has been updated successfully!", parent = self.root)
        except:
            messagebox.showerror("Error", "Something went wrong.")
    
    

    def delete(self):
        delete = messagebox.askyesno("Deletion", "Do you want to delete this data?", parent = self.root)
        if delete>0:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Faiza_065",
                database="hotel_management"
            )
            cur = con.cursor()
            query = "DELETE FROM booking WHERE roomno = %s"
            value = (self.var_roomavailable.get(),)
            cur.execute(query, value)
        else:
            if not delete:
                return
        con.commit()
        self.fetchdata()
        self.reset()
        con.close()

    def reset(self):
        self.var_roomavailable.set("")
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")  

    def fetchdata(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Faiza_065",
            database="hotel_management"
        )
        cur = con.cursor()
        cur.execute("SELECT booking_id,roomno,customer_id, emp_id, contact, check_in, check_out, roomtype, meal, noofdays, tax, actualtotal, total FROM booking")
        rows = cur.fetchall()
        if rows:
            self.book_details.delete(*self.book_details.get_children())
            for row in rows:
                self.book_details.insert("", END, values=row)
        con.commit()
        con.close()

    #use of search button
    def search(self):
        con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Faiza_065",
                database="hotel_management"
            )
        cur = con.cursor()

        query = "SELECT * FROM booking WHERE {} LIKE %s".format(self.search_var.get())
        value = "%" + self.txt_search.get() + "%"
        cur.execute(query, (value,))
        row = cur.fetchall()

        if len(row) != 0:
            self.book_details.delete(*self.book_details.get_children())
            for i in row:
                self.book_details.insert("", END, values=i)

        con.commit()
        con.close()


    def time(self):
        try:
            indate = datetime.strptime(self.var_checkin.get(), "%d/%m/%Y")
            outdate = datetime.strptime(self.var_checkout.get(), "%d/%m/%Y")
        except ValueError:
            indate = datetime.strptime(self.var_checkin.get(), "%Y-%m-%d")
            outdate = datetime.strptime(self.var_checkout.get(), "%Y-%m-%d")
            self.var_noofdays.set(abs(outdate-indate).days)

        if (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Luxury"):
            #value for breakfast
            value1 = float(100)
            #vaalue of luxury breakfast
            value2 = float(150)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #sum of luxury breakfast and breakfast
            value4 = float(value1+value2)
            #the finl actual sum
            value5 = float(value3*value4)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.1))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.1)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single"):
            #value for breakfast
            value1 = float(100)
            #vaalue of luxury breakfast
            value2 = float(50)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #sum of luxury breakfast and breakfast
            value4 = float(value1+value2)
            #the finl actual sum
            value5 = float(value3*value4)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.01))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.01)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Double"):
            #value for breakfast
            value1 = float(100)
            #vaalue of luxury breakfast
            value2 = float(100)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #sum of luxury breakfast and breakfast
            value4 = float(value1+value2)
            #the finl actual sum
            value5 = float(value3*value4)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.05))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.05)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury"):
            #value for breakfast
            value1 = float(150)
            #vaalue of luxury breakfast
            value2 = float(150)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #sum of luxury breakfast and breakfast
            value4 = float(value1+value2)
            #the finl actual sum
            value5 = float(value3*value4)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.1))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.1)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxury"):
            #value for breakfast
            value1 = float(130)
            #vaalue of luxury breakfast
            value2 = float(150)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #sum of luxury breakfast and breakfast
            value4 = float(value1+value2)
            #the finl actual sum
            value5 = float(value3*value4)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.1))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.1)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            #value for breakfast
            value1 = float(110)
            #vaalue of luxury breakfast
            value2 = float(50)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #sum of luxury breakfast and breakfast
            value4 = float(value1+value2)
            #the finl actual sum
            value5 = float(value3*value4)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.01))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.01)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
            #value for breakfast
            value1 = float(130)
            #vaalue of luxury breakfast
            value2 = float(50)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #sum of luxury breakfast and breakfast
            value4 = float(value1+value2)
            #the finl actual sum
            value5 = float(value3*value4)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.01))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.01)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double"):
            #value for breakfast
            value1 = float(120)
            #vaalue of luxury breakfast
            value2 = float(100)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #sum of luxury breakfast and breakfast
            value4 = float(value1+value2)
            #the finl actual sum
            value5 = float(value3*value4)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.05))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.05)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double"):
            #value for breakfast
            value1 = float(110)
            #vaalue of luxury breakfast
            value2 = float(100)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #sum of luxury breakfast and breakfast
            value4 = float(value1+value2)
            #the finl actual sum
            value5 = float(value3*value4)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.05))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.05)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)

        elif (self.var_meal.get()=="none" and self.var_roomtype.get() == "Single"):
            #vaalue of luxury breakfast
            value2 = float(50)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #the finl actual sum
            value5 = float(value3*value2)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.05))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.05)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)

        elif (self.var_meal.get()=="none" and self.var_roomtype.get() == "Double"):
            #vaalue of luxury breakfast
            value2 = float(100)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #the finl actual sum
            value5 = float(value3*value2)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.05))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.05)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)
        
        elif (self.var_meal.get()=="none" and self.var_roomtype.get() == "Luxury"):
            #vaalue of luxury breakfast
            value2 = float(150)
            #and the no. of days
            value3 = float(self.var_noofdays.get())
            #the finl actual sum
            value5 = float(value3*value2)
            #calculating the tax
            tax = "$"+str("%.2f"%(value5*0.05))
            actualamount= "$"+str("%.2f"%(value5))
            totalbill = "$"+str("%.2f"%((value5) + (value5*0.05)))
            #now seting the values in actual variables
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(actualamount)
            self.var_total.set(totalbill)

        else:
            messagebox.showerror("Error", "Something went wrong.")



                


if __name__ == "__main__":
    root = Tk()
    obj=button(root)
    root.mainloop()