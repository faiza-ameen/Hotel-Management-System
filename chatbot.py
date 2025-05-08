from tkinter import *
from tkinter import ttk, Canvas
from tkinter import messagebox

import mysql.connector

class chatbot:
    def __init__(self,root):
        self.root = root
        self.root.title("Employee Assistant")
        self.root.geometry("500x600+550+130")
        self.root.resizable(False, False)
        self.frame = Frame(self.root, bg="black", width= 600, height= 700)
        self.frame.place(x = 0, y=0)

        self.chat_box = Text(self.frame, bg = "black", fg = "white", font=("Arial", 12), wrap=WORD)
        self.chat_box.place(x=10, y=10,width=480,height=480)
        self.chat_box.insert(END, "Bot: Hello! How can I help you?\n")

        self.entry = Entry(self.frame,insertbackground="white", font=("Arial", 12), bg="black", fg = "white")
        self.entry.place(x=10,y=500, width=380, height=40)

        self.send_btn = Button(self.frame,text="Send", font=("Arial", 12), command=self.chat, bg="black", fg = "white")
        self.send_btn.place(x=400, y=500, width=80, height=40)

    def fetch_available_rooms(self):
        try:
            con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Faiza_065",
            database="hotel_management"
            )
            cur = con.cursor()
            cur.execute("SELECT roomno, roomtype FROM room WHERE status = 'available'")
            rows = cur.fetchall()
            con.close()
            return rows
        except:
            return["Error! Can't fetch data from database"]

    def chat(self):
        input = self.entry.get()
        self.chat_box.insert(END, f"You: {input}\n")
        self.entry.delete(0,END)

        reply = self.generate_response(input)
        self.chat_box.insert(END, f"Bot: {reply}\n")

    def generate_response(self, user_input):
        user_input = user_input.lower()

        if any(word in user_input for word in ["hi", "hello", "hey", "good morning", "good evening"]):
            return "Good day! Thank you for contacting our hotel. How may I assist you today?"

        elif any(word in user_input for word in ["bye", "goodbye", "see you", "later"]):
            return "Thank you for choosing our hotel. We look forward to serving you again. Have a great day!"

        elif "book" in user_input or "reservation" in user_input:
            return ("You can book a room directly through our website, by phone, or here at the front desk. "
                    "May I assist you with a booking now?")

        elif "cancel" in user_input or "cancellation" in user_input:
            return ("We're sorry to hear you wish to cancel. You can cancel your reservation by contacting us directly, "
                    "or through the platform you booked with. Please let me know if you need help.")

        elif "available" in user_input or "availability" in user_input:
            rooms = self.fetch_available_rooms()
            if "sorry" in rooms:
                return rooms[0]
            if not rooms:
                return "At the moment, there are no rooms available. We apologize for the inconvenience."

            room_lines = ""
            for i in range(0, len(rooms), 3):
                row = [f"Room {room[0]} ({room[1]})" for room in rooms[i:i+3]]
                room_lines += ", ".join(row) + "\n"

            return "Currently available rooms are:\n" + room_lines + "\nWould you like me to assist with a booking?"

        elif "check-in" in user_input:
            return ("Our check-in time starts from 2:00 PM onwards. "
                    "Early check-in may be accommodated based on room availability.")

        elif "check-out" in user_input:
            return ("Check-out time is before 12:00 PM noon. "
                    "Late check-out requests are subject to availability and may incur additional charges.")

        elif "breakfast" in user_input:
            return ("Yes, we offer complimentary breakfast for all our guests. "
                    "Breakfast is served from 7:00 AM to 10:30 AM in our main restaurant.")

        elif "parking" in user_input:
            return ("Yes, we offer free parking facilities for our guests. "
                    "Parking is available on-site and is subject to availability.")

        elif "wifi" in user_input or "internet" in user_input:
            return ("Yes, complimentary Wi-Fi is available throughout the hotel for all guests.")

        elif "restaurant" in user_input or "dining" in user_input:
            return ("Our main restaurant is open from 7:00 AM to 10:00 PM. "
                    "We serve breakfast, lunch, and dinner with a variety of local and international dishes.")

        elif "payment" in user_input or "pay" in user_input:
            return ("We accept various payment methods including cash, debit cards, credit cards (Visa, MasterCard), and mobile payments.")

        elif "services" in user_input or "facilities" in user_input or "amenities" in user_input:
            return ("We offer services like:\n"
                    "- 24/7 Room Service\n"
                    "- Swimming Pool\n"
                    "- Spa & Wellness Center\n"
                    "- Business Center\n"
                    "- Airport Shuttle (upon request)\n"
                    "- Laundry and Dry Cleaning\n"
                    "Please let me know if you would like more details on any service.")

        elif "thank" in user_input:
            return "You're most welcome! It’s our pleasure to assist you."

        else:
            return ("I'm here to help with reservations, services, and any queries about your stay. "
                    "Could you please clarify your question?")
        
if __name__ == "__main__":
    root  = Tk()
    app = chatbot(root)
    root.mainloop()

