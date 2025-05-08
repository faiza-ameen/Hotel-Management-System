import datetime
import tkinter as tk
from tkinter import ttk, messagebox, Canvas
import mysql.connector
from mysql.connector.errors import IntegrityError

from tkinter import *

#=======================================DONE=============================================
class system:
    @staticmethod
    def connect_db():
        return mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Faiza_065",
                    database="hotel_management"
                )
class MarkAttendance:
        def __init__(self, root):
            self.root = root
            self.window()
            self.widgets()
            self.load_employees()

            self.email_var = StringVar()

        def window(self):
            self.root.title("Employee management")
            self.root.geometry("500x400+500+180")
            self.root.resizable(False,False)

            self.frame = Frame(self.root, bg="#221d19", width= 1600, height= 800)
            self.frame.place(x = 0, y=0)

        def widgets(self):

            title = tk.Label(self.root, 
                        text="Employee Attendance", 
                        font=("Arial", 16, "bold"), 
                        bg="#221d19",
                        fg="white")
            title.place(x=145, y= 20)

            self.emp_var = tk.StringVar()
            self.emp_dict = {} 

            tk.Label(self.root, text="Select Employee:", bg="#221d19", fg="white", font=("Arial", 12, "bold")).place(x=100, y=65)
            self.emp_combo = ttk.Combobox(self.root, textvariable=self.emp_var, state="readonly")
            self.emp_combo.place(x= 250, y=65)

            tk.Label(self.root, text="Date:", bg="#221d19", fg="white", font=("Arial", 12, "bold")).place(x=100, y= 105)
            self.today_label = tk.Label(self.root, text=str(datetime.date.today()), bg="#221d19", fg="white", font=("Arial", 12, "bold"))
            self.today_label.place(x = 250, y=105)


            style = ttk.Style()
            style.configure("TRadiobutton", 
                            background="#221d19",  # Background color
                            foreground="white",      # Text color
                            font=("Arial", 10))     # Font

            # Variable for Radiobuttons
            self.status_var = StringVar(value="Present")

            tk.Label(self.root, text="Status:", bg="#221d19", fg="white", font=("Arial", 12, "bold")).place(x = 100, y = 145)
            ttk.Radiobutton(self.root, text="Present", variable=self.status_var, value="Present").place( x= 250, y = 145)
            ttk.Radiobutton(self.root, text="Absent", variable=self.status_var, value="Absent").place(x = 250, y =175)

            tk.Button(self.root, text="Mark Attendance", bg="#221d19", fg="white", font=("Arial", 12, "bold"), command=self.mark_attendance).place(x= 180, y = 230)

            tk.Button(self.root, text=" View Attendance", bg="#221d19", fg="white", font=("Arial", 12, "bold"), command=self.view_attendance).place(x= 80, y = 280)

            tk.Button(self.root, text="View Employees", bg="#221d19", fg="white", font=("Arial", 12, "bold"), command=self.view_employee).place(x= 280, y = 280)

        def load_employees(self):
            try:
                conn =system. connect_db()
                cursor = conn.cursor()
                cursor.execute("SELECT emp_id, first_name FROM employee")
                rows = cursor.fetchall()
                
                self.emp_dict = {f"{first_name} (ID: {emp_id})": emp_id for emp_id, first_name in rows}
                self.emp_combo['values'] = list(self.emp_dict.keys())
                
                cursor.close()
                conn.close()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

        def mark_attendance(self):
            selected_emp = self.emp_var.get()
            email = self.email_var.get()
            status = self.status_var.get()
            date_today = datetime.date.today()

            if not selected_emp:
                messagebox.showerror("Error", "Please select an employee.")
                return

            emp_id = self.emp_dict.get(selected_emp)
            if not emp_id:
                messagebox.showerror("Error", "Invalid employee selection")
                return

            conn = None
            cursor = None
            try:
                conn = system.connect_db()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO attendance (emp_id, date, status) VALUES (%s,%s, %s)",
                    (emp_id, date_today, status),
                    
                )
                cursor.execute("SELECT * FROM attendance ORDER BY emp_id ASC")
                cursor.fetchall()
                conn.commit()
                
            except IntegrityError:
                messagebox.showwarning("Warning", "Attendance already marked for today.", parent = self.root)
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
                    messagebox.showinfo("Success", f"Attendance marked as {status}", parent= self.root)

        def view_attendance(self):
            try:
                con = system.connect_db()
                cur = con.cursor(dictionary=True)
                cur.execute("""SELECT a.emp_id, e.first_name,e.last_name,e.email, e.role, a.date, a.status 
                                FROM attendance a
                                JOIN employee e ON a.emp_id = e.emp_id
                                ORDER BY a.date DESC, e.first_name""")
                record = cur.fetchall()

                if not record:
                    messagebox.showerror("Records", "No attendance record found.")
                    return
                
                #new window for showing records
                record_win = tk.Toplevel(self.root)
                record_win.title("Attendance record")
                record_win.geometry("800x500")

                #creating tree view for displaying records
                tree = ttk.Treeview(record_win, column = (
                    "ID", "First Name","Last Name","Email", "Role", "Date", "Status"
                ), show="headings")

                tree.heading("ID", text="Employee ID")
                tree.heading("First Name", text="First Name")
                tree.heading("Last Name", text="Last Name")
                tree.heading("Email", text="Email")
                tree.heading("Role", text="Role")
                tree.heading("Date", text="Date")
                tree.heading("Status", text="Status")

                tree.column("ID",width=100, anchor="center")
                tree.column("First Name",width=200, anchor="w")
                tree.column("Last Name",width=200, anchor="w")
                tree.column("Email",width=200, anchor="w")
                tree.column("Role",width=200, anchor="w")
                tree.column("Date",width=150, anchor="center")
                tree.column("Status",width=100, anchor="center")

                for record in record:
                    tree.insert("", "end", values=(
                        record['emp_id'],
                        record['first_name'],
                        record['last_name'],
                        record['email'],
                        record['role'],
                        record['date'].strftime('%Y-%m-%d'),
                        record['status']
                    ))

                # Add vertical scrollbar
                y_scroll = ttk.Scrollbar(record_win, orient="vertical", command=tree.yview)
                tree.configure(yscrollcommand=y_scroll.set)
                y_scroll.pack(side="right", fill="y")

                # Add horizontal scrollbar (if needed)
                x_scroll = ttk.Scrollbar(record_win, orient="horizontal", command=tree.xview)
                tree.configure(xscrollcommand=x_scroll.set)
                x_scroll.pack(side="bottom", fill="x")

                tree.pack(fill=tk.BOTH, expand=True)


                cur.close()
                con.close()
            except Exception as e:
                messagebox.showerror("DataBase Error", str(e))
        def view_employee(self):
            try:
                con = system.connect_db()
                cur = con.cursor(dictionary=True)
                cur.execute("""
                    SELECT emp_id, first_name,last_name, email, role 
                    FROM employee
                    ORDER BY emp_id
                """)
                employees = cur.fetchall()
                
                if not employees:
                    messagebox.showinfo("Employees", "No employees registered yet")
                    return
                    
                # Create a new window for displaying employees
                emp_window = tk.Toplevel(self.root)
                emp_window.title("Registered Employees")
                emp_window.geometry("800x500")
                
                # Treeview for displaying employees
                tree = ttk.Treeview(emp_window, columns=("ID", "First Name","Last Name", "Email", "Role"), show="headings")
                tree.heading("ID", text="Employee ID")
                tree.heading("First Name", text="First Name")
                tree.heading("Last Name", text="Last Name")
                tree.heading("Email", text="Email")
                tree.heading("Role", text="Role")
                
                tree.column("ID", width=100, anchor="center")
                tree.column("First Name", width=100, anchor="w")
                tree.column("Last Name", width=100, anchor="w")
                tree.column("Email", width=100, anchor="w")
                tree.column("Role", width=150, anchor="center")
                
                for emp in employees:
                    tree.insert("", "end", values=(
                        emp['emp_id'],
                        emp['first_name'],
                        emp['last_name'],
                        emp['email'],
                        emp['role']
                    ))
                
                # Add vertical scrollbar
                y_scroll = ttk.Scrollbar(emp_window, orient="vertical", command=tree.yview)
                tree.configure(yscrollcommand=y_scroll.set)
                y_scroll.pack(side="right", fill="y")

                # Add horizontal scrollbar (if needed)
                x_scroll = ttk.Scrollbar(emp_window, orient="horizontal", command=tree.xview)
                tree.configure(xscrollcommand=x_scroll.set)
                x_scroll.pack(side="bottom", fill="x")

                tree.pack(fill=tk.BOTH, expand=True)
                
                # Add delete button
                delete_frame = tk.Frame(emp_window)
                delete_frame.pack(fill="x", pady=5)
                
                tk.Label(delete_frame, text="Enter ID to delete:").pack(side="left", padx=5)
                
                self.delete_id_var = tk.StringVar()
                delete_entry = tk.Entry(delete_frame, textvariable=self.delete_id_var, width=10)
                delete_entry.pack(side="left", padx=5)
                
                delete_btn = tk.Button(delete_frame, 
                                    text="Delete Employee", 
                                    bg="white",
                                    fg="red",
                                    command=lambda: self.delete_employee(emp_window))
                delete_btn.pack(side="left", padx=5)
                
                cur.close()
                con.close()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

        def delete_employee(self, window):
            emp_id = self.delete_id_var.get().strip()
            
            if not emp_id:
                messagebox.showerror("Error", "Please enter an employee ID")
                return
                
            try:
                emp_id = int(emp_id)
            except ValueError:
                messagebox.showerror("Error", "Employee ID must be a number")
                return
                
            confirm = messagebox.askyesno("Confirm", f"Delete employee with ID {emp_id}?")
            if not confirm:
                return
                
            try:
                con = system.connect_db()
                cur = con.cursor()
                
                # Check if employee exists
                cur.execute("SELECT first_name FROM employee WHERE emp_id = %s", (emp_id,))
                result = cur.fetchone()
                
                if not result:
                    messagebox.showerror("Error", f"No employee found with ID {emp_id}")
                    return
                    
                # Delete employee
                cur.execute("DELETE FROM employee WHERE emp_id = %s", (emp_id,))
                con.commit()
                
                messagebox.showinfo("Success", f"Employee {result[0]} deleted successfully")
                self.delete_id_var.set("")
                self.load_employees()
                window.destroy()  # Close the employee view window
                self.view_employee()  # Reopen to show updated list
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
            finally:
                if 'cur' in locals() and cur:
                    cur.close()
                if 'con' in locals() and con:
                    con.close()


# === Register Employee Window ===
class RegisterEmployee:
        def __init__(self, root):
            self.root = root
            self.window()
            self.widgets()

        def window(self):
            self.root.title("Employee Registration")
            self.root.geometry("500x400+500+180")
            self.root.resizable(False, False)
            self.root.configure(bg="#221d19")

        def widgets(self):

            self.fname_var = tk.StringVar()
            self.lname_var = tk.StringVar()
            self.role_var = tk.StringVar()
            self.email_var = tk.StringVar()

            tk.Label(self.root, text="Regitser new employee", bg="#221d19", fg="white", font=("Arial", 12, "bold")).place(x=155, y=35)
            
            

            tk.Label(self.root, text="First Name:", bg="#221d19", fg="white", font=("Arial", 12, "bold")).place(x=100, y=95)
            self.name_entry = tk.Entry(self.root, textvariable=self.fname_var, width=24)
            self.name_entry.place(x=250, y=95)

            tk.Label(self.root, text="Last Name:", bg="#221d19", fg="white", font=("Arial", 12, "bold")).place(x=100, y=135)
            self.name_entry = tk.Entry(self.root, textvariable=self.lname_var, width=24)
            self.name_entry.place(x=250, y=135)

            tk.Label(self.root, text="Email:", bg="#221d19", fg="white", font=("Arial", 12, "bold")).place(x=100, y=175)
            self.name_entry = tk.Entry(self.root, textvariable=self.email_var, width=24)
            self.name_entry.place(x=250, y=175)


            tk.Label(self.root, text="Role:", bg="#221d19", fg="white", font=("Arial", 12, "bold")).place(x= 100, y =215)
            self.role_combo = ttk.Combobox(self.root, textvariable=self.role_var, state="readonly", width=21)
            self.role_combo['values'] = ("admin", "receptionist", "housekeeping") 
            self.role_combo.place(x=250 , y= 215)

            tk.Button(self.root, text="Register", bg="#221d19", fg="white", font=("Arial", 12, "bold"), command=self.register_employee).place(x = 210, y=265)
            tk.Button(self.root, text="View Employees", bg="#221d19", fg="white", font=("Arial", 12, "bold"), command=self.view_employee).place(x = 180, y=315)

        def register_employee(self):
            first_name = self.fname_var.get()
            last_name = self.lname_var.get()
            email = self.email_var.get()
            role = self.role_var.get()

            if not first_name or not role or not last_name or not email:
                messagebox.showerror("Error", "All fields are required")
                return

            conn = None
            cursor = None
            try:
                conn = system.connect_db()
                if conn.is_connected():  # Verify connection
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO employee (first_name,last_name, email, role) VALUES (%s,%s,%s, %s)", (first_name,last_name, email, role))
                    conn.commit()
                    messagebox.showinfo("Success", "Employee registered successfully")
                    self.fname_var.set("")
                    self.lname_var.set("")
                    self.email_var.set("")
                    self.role_var.set("")
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
            finally:
                if cursor:
                    cursor.close()
                if conn and conn.is_connected():
                    conn.close()

        def view_employee(self):
            try:
                con = system.connect_db()
                cur = con.cursor(dictionary=True)
                cur.execute("""
                    SELECT emp_id, first_name,last_name, email, role 
                    FROM employee
                    ORDER BY emp_id
                """)
                employees = cur.fetchall()
                
                if not employees:
                    messagebox.showinfo("Employees", "No employees registered yet")
                    return
                    
                # Create a new window for displaying employees
                emp_window = tk.Toplevel(self.root)
                emp_window.title("Registered Employees")
                emp_window.geometry("800x500")
                
                # Treeview for displaying employees
                tree = ttk.Treeview(emp_window, columns=("ID", "First Name","Last Name", "Email", "Role"), show="headings")
                tree.heading("ID", text="Employee ID")
                tree.heading("First Name", text="First Name")
                tree.heading("Last Name", text="Last Name")
                tree.heading("Email", text="Email")
                tree.heading("Role", text="Role")
                
                tree.column("ID", width=100, anchor="center")
                tree.column("First Name", width=100, anchor="w")
                tree.column("Last Name", width=100, anchor="w")
                tree.column("Email", width=100, anchor="w")
                tree.column("Role", width=150, anchor="center")
                
                for emp in employees:
                    tree.insert("", "end", values=(
                        emp['emp_id'],
                        emp['first_name'],
                        emp['last_name'],
                        emp['email'],
                        emp['role']
                    ))
                
                # Add vertical scrollbar
                y_scroll = ttk.Scrollbar(emp_window, orient="vertical", command=tree.yview)
                tree.configure(yscrollcommand=y_scroll.set)
                y_scroll.pack(side="right", fill="y")

                # Add horizontal scrollbar (if needed)
                x_scroll = ttk.Scrollbar(emp_window, orient="horizontal", command=tree.xview)
                tree.configure(xscrollcommand=x_scroll.set)
                x_scroll.pack(side="bottom", fill="x")

                tree.pack(fill=tk.BOTH, expand=True)
                
                # Add delete button
                delete_frame = tk.Frame(emp_window)
                delete_frame.pack(fill="x", pady=5)
                
                tk.Label(delete_frame, text="Enter ID to delete:").pack(side="left", padx=5)
                
                self.delete_id_var = tk.StringVar()
                delete_entry = tk.Entry(delete_frame, textvariable=self.delete_id_var, width=10)
                delete_entry.pack(side="left", padx=5)
                
                delete_btn = tk.Button(delete_frame, 
                                    text="Delete Employee", 
                                    bg="white",
                                    fg="red",
                                    command=lambda: self.delete_employee(emp_window))
                delete_btn.pack(side="left", padx=5)
                
                cur.close()
                con.close()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

        def delete_employee(self, window):
            emp_id = self.delete_id_var.get().strip()
            
            if not emp_id:
                messagebox.showerror("Error", "Please enter an employee ID")
                return
                
            try:
                emp_id = int(emp_id)
            except ValueError:
                messagebox.showerror("Error", "Employee ID must be a number")
                return
                
            confirm = messagebox.askyesno("Confirm", f"Delete employee with ID {emp_id}?")
            if not confirm:
                return
                
            try:
                con = system.connect_db()
                cur = con.cursor()
                
                # Check if employee exists
                cur.execute("SELECT first_name FROM employee WHERE emp_id = %s", (emp_id,))
                result = cur.fetchone()
                
                if not result:
                    messagebox.showerror("Error", f"No employee found with ID {emp_id}")
                    return
                    
                # Delete employee
                cur.execute("DELETE FROM employee WHERE emp_id = %s", (emp_id,))
                con.commit()
                
                messagebox.showinfo("Success", f"Employee {result[0]} deleted successfully")
                self.delete_id_var.set("")
                window.destroy()  # Close the employee view window
                self.view_employee()  # Reopen to show updated list
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
            finally:
                if 'cur' in locals() and cur:
                    cur.close()
                if 'con' in locals() and con:
                    con.close()



def system_run(parent_window):
    """Function to be called from main application"""
    question = messagebox.askyesno("Employee", "Are you here to mark attendance?", parent=parent_window)
    if question>0:
        attendance_window = tk.Toplevel(parent_window)
        app = MarkAttendance(attendance_window)
    else:
        ask = messagebox.askyesno("Employee", "Do you want to see employee list?", parent=parent_window)
        if ask >0:
            registration_window = tk.Toplevel(parent_window)
            app = RegisterEmployee(registration_window)
        else:
            messagebox.showerror("Error", "Sorry! No window can be opened.")
