from tkinter import *
from tkinter import ttk, Canvas
from tkinter import messagebox

from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import random
import mysql.connector

#====================================DONE================================

class detail:
    def __init__(self,root):
        self.root = root
        self.root.title("Room Details")
        self.root.geometry("1520x670+0+130")

        self.frame = Frame(self.root, bg="#221d19", width= 1600, height= 800)
        self.frame.place(x = 0, y=0)

        #add customer details
        self.start = Label(self.root , text = "Rooms Details", font=("times new roman",28,"bold"), fg="white", bg="#221d19")
        self.start.place(x = 600, y= 30)

        self.line = Label(self.root , text = "__________________________________________________________________________________________________________________________________________________________________",
                            font=("times new roman",28,"bold"), fg="white", bg="#221d19")
        self.line.place(x = 0, y= 76)

class info(detail):
    def __init__(self, root):
        super().__init__(root)
        
        self.left = LabelFrame(self.root, bd = 2, relief=RIDGE, text= "Room Booking Details", font=(("times new roman",16,"bold")), bg="#221d19",fg="white" , padx=2)
        self.left.place(x=50, y=135, width=590, height=280)

        #adding images
        self.side_path = r"D:\python\sem 2\project\images\room.jpg"
        self.side = Image.open(self.side_path)
        self.side = self.side.resize((800, 500), Image.Resampling.LANCZOS)  #provide scaling
        self.side_image = ImageTk.PhotoImage(self.side)

        self.sidelabel = Label(self.root, image = self.side_image, bg = "#221d19")
        self.sidelabel.place(x = 680, y=140)

        #floor 
        self.var_floor = StringVar()
        self.floor = Label(self.left, text= "Floor:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.floor.place(x=30 ,y= 10)

        self.flor = Entry(self.left,textvariable=self.var_floor, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.flor.place(x= 250, y=15)

        #Room No.
        self.roomno = Label(self.left, text= "Room No:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.roomno.place(x=30 ,y= 50)

        self.var_roomno = StringVar()
        self.romno = Entry(self.left,textvariable=self.var_roomno, width=32,insertbackground="white", font= (("times new roman",14)), fg="white", bg="#221d19")
        self.romno.place(x= 250, y=55)

        #room type
        self.room_type = Label(self.left, text= "Room Type:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.room_type.place(x=30 ,y= 90)

        self.var_roomtype = StringVar()
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
        self.roomtype.place(x= 250, y=95)

        #status
        self.room_status = Label(self.left, text= "Status:", font= (("times new roman",16,"bold")),bg="#221d19",fg="white" , padx=2, pady=6)
        self.room_status.place(x=30 ,y= 130)

        self.var_status = StringVar()
        style = ttk.Style()
        style.theme_use("default")  # Needed for full control over styling

        style.configure("CustomCombobox.TCombobox",
                            fieldbackground="#221d19",  # Inside area
                            background="#221d19",       # Drop-down background
                            foreground="white",       # Text color
                            arrowcolor="white",       # Arrow color
                            borderwidth=1)

        # Your combobox with custom style
        self.status = ttk.Combobox(self.left,textvariable=self.var_status, width=31, font=("Times New Roman", 14),
                                    values=("available", "occupied"),
                                    style="CustomCombobox.TCombobox")
        self.status.place(x= 250, y=135)

        #adding buttons
        btn = Frame(self.left, bd=2, relief=RIDGE, background="#221d19")
        btn.place(x=25, y=170, width=532,height=70)

        btn1 = Button(btn, text="Add",command=self.add_data, font=("times new roman",16,"bold"), bg="#221d19", fg="yellow", width=9, activebackground="#221d19")
        btn1.place(x = 10, y = 12)

        btn2 = Button(btn, text="Update",command=self.update, font=("times new roman",16,"bold"), bg="#221d19", fg="green", width=9, activebackground="#221d19")
        btn2.place(x = 140, y = 12)

        btn3 = Button(btn, text="Delete",command=self.delete, font=("times new roman",16,"bold"), bg="#221d19", fg="red", width=9, activebackground="#221d19")
        btn3.place(x = 270, y = 12)

        btn4 = Button(btn, text="Reset",command=self.reset, font=("times new roman",16,"bold"), bg="#221d19", fg="orange", width=9, activebackground="#221d19")
        btn4.place(x = 400, y = 12)

        #==================creating table frame ================
        self.table = LabelFrame(self.root, bd = 2, relief=RIDGE, text= "Search And View Details", font=(("times new roman",16,"bold")), bg="#221d19",fg="white" , padx=2)
        self.table.place(x=50, y=420, width=590, height=224)

        # Frame for Treeview and Scrollbars
        details = Frame(self.table, bd=2, relief=RIDGE, bg="#221d19")
        details.place(x=10, y=20, width=560, height=160)

        # Treeview Scrollbars
        scroll_x = Scrollbar(details, orient=HORIZONTAL)
        scroll_y = Scrollbar(details, orient=VERTICAL)

        # Treeview Widget
        self.room_details = ttk.Treeview(
            details,
            columns=("Floor", "Roomno", "Roomtype", "Status"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_details.xview)
        scroll_y.config(command=self.room_details.yview)


        self.room_details.heading("Floor", text="Floor")
        self.room_details.heading("Roomno", text="Room No.")
        self.room_details.heading("Roomtype", text="Room Type")
        self.room_details.heading("Status", text="Status")

        self.room_details["show"] = "headings"
        self.room_details.column("Floor", width=100)
        self.room_details.column("Roomno", width=100)
        self.room_details.column("Roomtype", width=100)
        self.room_details.column("Status", width=100)


        self.room_details.pack(fill=BOTH, expand=1)

        self.room_details.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetchdata()


    def fetchdata(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Faiza_065",
            database="hotel_management"
        )
        cur = con.cursor()
        cur.execute("SELECT floor, roomno, roomtype, status FROM room")
        rows = cur.fetchall()
        if rows:
            self.room_details.delete(*self.room_details.get_children())
            for row in rows:
                self.room_details.insert("", END, values=row)
        con.commit()
        con.close()

    def add_data(self):
        if self.var_roomno.get() == "":
            messagebox.showerror("Error", "All fields are required.", parent = self.root)
        else:
            #saving data into data base
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="Faiza_065", database="hotel_management") #connectivity of data base
                cur = con.cursor() #adding data
                cur.execute("INSERT INTO room (floor, roomno, roomtype, status) VALUES(%s,%s,%s, %s)", (
                                                                        self.var_floor.get(),
                                                                        self.var_roomno.get(),
                                                                        self.var_roomtype.get(),
                                                                        self.var_status.get()
                                                                                                ))
                con.commit()
                self.fetchdata()
                con.close()
                messagebox.showinfo("Success", 'New room added successfully!', parent = self.root)
            except:
                messagebox.showerror("WARNING", "Something went wrong!", parent = self.root)

    def get_cursor(self, event = ""):
        cursor_row= self.room_details.focus()
        content = self.room_details.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])
        self.var_status.set(row[3])

    def update(self):
        try:
            if self.var_roomno.get() == "":
                messagebox.showerror("ERROR", "Please enter room number.", parent = self.root)
            else:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Faiza_065",
                    database="hotel_management"
                )
                cur = con.cursor()
                cur.execute("UPDATE room SET floor=%s, roomtype=%s, status=%s WHERE roomno=%s",(
                                                                                        self.var_floor.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_status.get(),
                                                                                        self.var_roomno.get()
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
            query = "DELETE FROM room WHERE roomno = %s"
            value = (self.var_roomno.get(),)
            cur.execute(query, value)
        else:
            if not delete:
                return
        con.commit()
        self.fetchdata()
        self.reset()
        con.close()

    def reset(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("")
        self.var_status.set("")

    
        
if __name__ == "__main__":
    root = Tk()
    app = info(root)
    root.mainloop()
