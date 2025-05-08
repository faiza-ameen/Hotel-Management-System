import mysql.connector
import csv

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Faiza_065",
    database="hotel_management"
)
cursor = conn.cursor()

# Open the CSV file
with open(r'D:\python\project2.0\room.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Skip header row
    for row in csv_data:
        cursor.execute(
            "INSERT INTO room (floor, roomno, roomtype, status) VALUES (%s, %s, %s, %s)",
            row
        )

# Commit changes
conn.commit()

# Close connection
cursor.close()
conn.close()
print("CSV data inserted successfully!")
