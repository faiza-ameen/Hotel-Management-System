from tkinter import *
from tkinter import ttk, Canvas
from tkinter import messagebox

from PIL import Image, ImageTk
import random
import mysql.connector

#=======================================DONE=============================================

class cust:
    def __init__(self,root):
        self.root = root
        self.root.title("Customer info")
        self.root.geometry("1520x750+0+130")

        #creating variables
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_address = StringVar()


        self.frame = Frame(self.root, bg="#221d19", width= 1600, height= 800)
        self.frame.place(x = 0, y=0)

        #add customer details
        self.start = Label(self.root , text = "Add Customer Details", font=("times new roman",28,"bold"), fg="white", bg="#221d19")
        self.start.place(x = 600, y= 30)

        self.line = Label(self.root , text = "__________________________________________________________________________________________________________________________________________________________________",
                            font=("times new roman",28,"bold"), fg="white", bg="#221d19")
        self.line.place(x = 0, y= 68)

class buttons(cust):
    def __init__(self, root):
        super().__init__(root)

        self.left = LabelFrame(self.root, bd = 2, relief=RIDGE, text= "Customer Details", font=(("times new roman",16,"bold")), bg="#221d19",fg="white" , padx=2)
        self.left.place(x=50, y=130, width=590, height=510)

        # labels and their entries
        self.cust_ref = Label(self.left, text= "Customer Reference:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.cust_ref.place(x=30 ,y= 10)

        self.ref = Entry(self.left, textvariable=self.var_ref, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.ref.place(x= 250, y=15)

        self.name = Label(self.left, text= "Customer Name:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.name.place(x=30 ,y= 50)

        self.nam = Entry(self.left,textvariable=self.var_cust_name, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.nam.place(x= 250, y=55)

        self.gender = Label(self.left, text= "Gender:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.gender.place(x=30 ,y= 90)

        style = ttk.Style()
        style.theme_use("default")  # Needed for full control over styling

        style.configure("CustomCombobox.TCombobox",
                            fieldbackground="#221d19",  # Inside area
                            background="#221d19",       # Drop-down background
                            foreground="white",       # Text color
                            arrowcolor="white",       # Arrow color
                            borderwidth=1)

        # Your combobox with custom style
        gen = ttk.Combobox(self.left, width=31,textvariable=self.var_gender, font=("Times New Roman", 14),
                                    values=("male", "female", "other"),
                                    style="CustomCombobox.TCombobox")
        gen.place(x=250, y=95)
        # gen.current(0)

        self.postcode = Label(self.left, text= "Post Code:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.postcode.place(x=30 ,y= 130)

        self.post = Entry(self.left,textvariable=self.var_post, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.post.place(x= 250, y=135)

        self.mobile = Label(self.left, text= "Mobile:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.mobile.place(x=30 ,y= 170)

        self.mob = Entry(self.left, width=32,textvariable=self.var_mobile, insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.mob.place(x= 250, y=175)

        self.email = Label(self.left, text= "Email:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.email.place(x=30 ,y= 210)

        self.ema = Entry(self.left, width=32,textvariable=self.var_email ,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.ema.place(x= 250, y=215)
        
        self.nationality = Label(self.left, text= "Nationality:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.nationality.place(x=30 ,y= 250)

        style = ttk.Style()
        style.theme_use("default")  # Needed for full control over styling

        style.configure("CustomCombobox.TCombobox",
                            fieldbackground="#221d19",  # Inside area
                            background="#221d19",       # Drop-down background
                            foreground="white",       # Text color
                            arrowcolor="white",       # Arrow color
                            borderwidth=1)

        # Your combobox with custom style
        nation = ttk.Combobox(self.left, width=31,textvariable=self.var_nationality, font=("Times New Roman", 14),
                                    values=("Pakistani", "Indian", "American", "other"),
                                    style="CustomCombobox.TCombobox")
        nation.place(x=250, y=255)
        # nation.current(0)

        self.idproof = Label(self.left, text= "ID proof type:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.idproof.place(x=30 ,y= 290)

        style = ttk.Style()
        style.theme_use("default")  # Needed for full control over styling

        style.configure("CustomCombobox.TCombobox",
                            fieldbackground="#221d19",  # Inside area
                            background="#221d19",       # Drop-down background
                            foreground="white",       # Text color
                            arrowcolor="white",       # Arrow color
                            borderwidth=1)

        # Your combobox with custom style
        id = ttk.Combobox(self.left, width=31,textvariable=self.var_idproof, font=("Times New Roman", 14),
                                    values=("ID Card", "B-Form","Birth Certificate", "Other"),
                                    style="CustomCombobox.TCombobox")
        id.place(x=250, y=295)
        # id.current(0)

        self.idnnumber = Label(self.left, text= "ID number:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.idnnumber.place(x=30 ,y= 330)

        self.num = Entry(self.left,textvariable=self.var_idnumber, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.num.place(x= 250, y=335)

        self.address = Label(self.left, text= "Address:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.address.place(x=30 ,y= 370)

        self.add = Entry(self.left,textvariable=self.var_address, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.add.place(x= 250, y=375)

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

        self.table = LabelFrame(self.root, bd = 2, relief=RIDGE, text= "Search And View Details", font=(("times new roman",16,"bold")), bg="#221d19",fg="white" , padx=2)
        self.table.place(x=690, y=130, width=800, height=510)

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
                                    values=("Mobile", "Reference"),
                                    style="CustomCombobox.TCombobox")
        search.place(x=135, y=15)

        self.txt_search=StringVar()
        self.searchentry = Entry(self.table,textvariable=self.txt_search, width=23,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.searchentry.place(x= 345, y=15)

        btnSearch = Button(self.table,command=self.search, text="Search", font=("times new roman",16,"bold"), bg="#221d19", fg="white", width=8, activebackground="#221d19")
        btnSearch.place(x = 565, y = 5)

        btnShow = Button(self.table,command=self.fetchdata, text="Show", font=("times new roman",16,"bold"), bg="#221d19", fg="white", width=8, activebackground="#221d19")
        btnShow.place(x = 680, y = 5)

        # Frame for Treeview and Scrollbars
        details = Frame(self.table, bd=2, relief=RIDGE, bg="#221d19")
        details.place(x=50, y=80, width=700, height=350)

        # Treeview Scrollbars
        scroll_x = Scrollbar(details, orient=HORIZONTAL)
        scroll_y = Scrollbar(details, orient=VERTICAL)

        # Treeview Widget
        self.cust_details = ttk.Treeview(
            details,
            columns=("Customer Id","Reference", "Name", "Gender", "Post", "Mobile", "Email", "Nationality", "Idproof", "Idnumber", "Address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_details.xview)
        scroll_y.config(command=self.cust_details.yview)

        # Configure headings (make sure names match column names)
        self.cust_details.heading("Customer Id", text="Cust Id")
        self.cust_details.heading("Reference", text="Ref No.")
        self.cust_details.heading("Name", text="Name")
        self.cust_details.heading("Gender", text="Gender")
        self.cust_details.heading("Post", text="Post Code")
        self.cust_details.heading("Mobile", text="Mobile")
        self.cust_details.heading("Email", text="Email")
        self.cust_details.heading("Nationality", text="Nationality")
        self.cust_details.heading("Idproof", text="Id Proof")
        self.cust_details.heading("Idnumber", text="Id Number")
        self.cust_details.heading("Address", text="Address")

        self.cust_details["show"] = "headings"
        self.cust_details.column("Customer Id", width=100)
        self.cust_details.column("Reference", width=100)
        self.cust_details.column("Name", width=100)
        self.cust_details.column("Gender", width=100)
        self.cust_details.column("Post", width=100)
        self.cust_details.column("Mobile", width=100)
        self.cust_details.column("Email", width=100)
        self.cust_details.column("Nationality", width=100)
        self.cust_details.column("Idproof", width=100)
        self.cust_details.column("Idnumber", width=100)
        self.cust_details.column("Address", width=100)

        self.cust_details.pack(fill=BOTH, expand=1)
        self.cust_details.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetchdata()


    def add_data(self):
        if self.var_mobile.get() == "" or self.var_idnumber.get() == "":
            messagebox.showerror("Error", "All fields are required.", parent = self.root)
        else:
            #saving data into data base
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="Faiza_065", database="hotel_management") #connectivity of data base
                cur = con.cursor() #adding data
                cur.execute("INSERT INTO customer (reference, name, Gender, Post, mobile, Email, Nationality, Idproof, Idnumber, Address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                        self.var_ref.get(),
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_post.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_idproof.get(),
                                                                                        self.var_idnumber.get(),
                                                                                        self.var_address.get()
                                                                                                        ))
                con.commit()
                self.fetchdata()
                # con.close()
                messagebox.showinfo("Success", 'Customer has been added', parent = self.root)
            except:
                messagebox.showerror("WARNING", "Something went wrong!", parent = self.root)
            finally:
                if con and con.is_connected():
                    cur.close()
                    con.close()

    def fetchdata(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Faiza_065",
            database="hotel_management"
        )
        cur = con.cursor()
        cur.execute("SELECT customer_id, reference, name, Gender, Post, mobile, Email, Nationality, Idproof, Idnumber, Address FROM customer")
        rows = cur.fetchall()
        if rows:
            self.cust_details.delete(*self.cust_details.get_children())
            for row in rows:
                self.cust_details.insert("", END, values=row)
        con.commit()
        con.close()

    def get_cursor(self, event = ""):
        cursor_row= self.cust_details.focus()
        content = self.cust_details.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[1])
        self.var_cust_name.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idnumber.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("ERROR", "Please enter mobile number.", parent = self.root)
        else:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Faiza_065",
                database="hotel_management"
            )
            cur = con.cursor()
            cur.execute("UPDATE customer set name=%s, Gender=%s, Post=%s, mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s where reference=%s",(
                                                                                                                                                    self.var_cust_name.get(),
                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                    self.var_post.get(),
                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                    self.var_email.get(),
                                                                                                                                                    self.var_nationality.get(),
                                                                                                                                                    self.var_idproof.get(),
                                                                                                                                                    self.var_idnumber.get(),
                                                                                                                                                    self.var_address.get(),
                                                                                                                                                    self.var_ref.get()
                                                                                                                                                                    ))
            con.commit()
            self.fetchdata()
            con.close()
            messagebox.showinfo("SUCCESS", "Data has been updated successfully!", parent = self.root)

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
            query = "delete from customer where Reference = %s"
            value = (self.var_ref.get(),)
            cur.execute(query, value)
        else:
            if not delete:
                return
        con.commit()
        self.fetchdata()
        con.close()

    def reset(self):
        # self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
        self.var_idproof.set("")
        self.var_idnumber.set("")
        self.var_address.set("")

        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Faiza_065",
                database="hotel_management"
            )
        cur = con.cursor()

        query = "SELECT customer_id, reference, name, Gender, Post, mobile, Email, Nationality, Idproof, Idnumber, Address FROM customer WHERE {} LIKE %s".format(self.search_var.get())
        value = "%" + self.txt_search.get() + "%"
        cur.execute(query, (value,))
        row = cur.fetchall()

        if len(row) != 0:
            self.cust_details.delete(*self.cust_details.get_children())
            for i in row:
                self.cust_details.insert("", END, values=i)

        con.commit()
        con.close()

if __name__ == "__main__":
    root = Tk()
    app = buttons(root)
    root.mainloop()