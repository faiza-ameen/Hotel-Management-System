from fpdf import FPDF
import os
import mysql.connector
from tkinter import *
from tkinter import messagebox

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 16)
        self.cell(0, 10, "Hotel Management System Report", ln=True, align='C')
        self.ln(10)  # Add some space below the header

    def footer(self):
        self.set_y(-15)  # Position at 1.5 cm from the bottom
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')  # Page number at the bottom

    def add_page_with_border(self):
        self.add_page()
        self.rect(5, 5, 200, 287)  # Draw a rectangle around the page
        self.ln(10)

class report(PDF):
    def generate_full_report(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Faiza_065",  
                database="hotel_management"       
            )
            cursor = conn.cursor()

            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)

            # --- Customer Details Page ---
            cursor.execute("SELECT * FROM customer")
            customers = cursor.fetchall()

            pdf.add_page_with_border()

            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "Customer Details Report", ln=True, align="C")
            pdf.ln(10)

            # Table Header
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(30, 10, "ID", border=1, align='C')
            pdf.cell(70, 10, "Name", border=1, align='C')
            pdf.cell(70, 10, "Phone", border=1, align='C')
            pdf.ln()

            # Table Rows
            pdf.set_font("Arial", size=12)
            if customers:
                for customer in customers:
                    pdf.cell(30, 10, str(customer[0]), border=1, align='C')
                    pdf.cell(70, 10, str(customer[2]), border=1, align='C')  # Name
                    pdf.cell(70, 10, str(customer[5]), border=1, align='C')  # Phone
                    pdf.ln()
            else:
                pdf.cell(0, 10, "No customer data found.", ln=True)

            # --- Booking Details Page ---
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "Booking Details Report", ln=True, align="C")
            pdf.ln(10)

            # Table Header
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(30, 10, "Booking ID", border=1, align='C')
            pdf.cell(50, 10, "Customer ID", border=1, align='C')
            pdf.cell(50, 10, "Room", border=1, align='C')
            pdf.cell(50, 10, "Bill", border=1, align='C')
            pdf.ln()

            # Table Rows
            pdf.set_font("Arial", size=12)
            cursor.execute("SELECT * FROM booking")
            bookings = cursor.fetchall()
            if bookings:
                for booking in bookings:
                    pdf.cell(30, 10, str(booking[0]), border=1, align='C')
                    pdf.cell(50, 10, str(booking[2]), border=1, align='C')
                    pdf.cell(50, 10, str(booking[1]), border=1, align='C')
                    pdf.cell(50, 10, str(booking[12]), border=1, align='C')
                    pdf.ln()
            else:
                pdf.cell(0, 10, "No booking data found.", ln=True)

            # --- Employee Attendance Page ---
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "Employee Attendance Report", ln=True, align="C")
            pdf.ln(10)

            # Table Header
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(60, 10, "Employee ID", border=1, align='C')
            pdf.cell(50, 10, "Date", border=1, align='C')
            pdf.cell(40, 10, "Status", border=1, align='C')
            pdf.ln()

            # Table Rows
            pdf.set_font("Arial", size=12)
            cursor.execute("SELECT * FROM attendance")
            attendance = cursor.fetchall()
            if attendance:
                for record in attendance:
                    pdf.cell(60, 10, str(record[1]), border=1, align='C')
                    pdf.cell(50, 10, str(record[2]), border=1, align='C')
                    pdf.cell(40, 10, str(record[3]), border=1, align='C')
                    pdf.ln()
            else:
                pdf.cell(0, 10, "No attendance data found.", ln=True)

            # Save the final PDF
            pdf.output("hotel_management_report.pdf")
            conn.close()

            messagebox.showinfo("Success", "Report generated successfully as 'hotel_management_report.pdf'!")

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {str(e)}")

        pdf.output("hotel_management_report.pdf")
        conn.close()

        os.startfile("hotel_management_report.pdf")  #opening the pdf after creation
        messagebox.showinfo("Success", "Report generated and opened successfully!")

if __name__ == "__main__":
    root = Tk()
    app = report(root)
    root.mainloop()
    
