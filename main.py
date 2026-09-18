import sqlite3

connection = sqlite3.connect("OCRtunes.db")

cursor = connection.cursor()

print ("Please create an account for OCRtunes to start")
username=input("Please enter your chosen username and must be appropriate: ")
password = input("Please enter a password between 8-20 characters and use some special characters e.g.&@%$: ")
while len(password) < 8 or len(password) > 20:
    print("Password must be between 8-20 characters.")
    password = input("Please enter a password between 8-20 characters and use some special characters e.g.&@%$: ")

try:
    cursor.execute("INSERT INTO users (01, username, password)")
except: 
    print("Account created successfully!")

connection.commit()
connection.close()