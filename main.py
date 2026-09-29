import os
import sqlite3
import pyfiglet
from colorama import Fore, Back, Style, init
import time

init(autoreset=True)

def clear_terminal():
    # Clears terminal: 'cls' for Windows, 'clear' for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')
    
conn = sqlite3.connect("OCRtunes.db")
cursor = conn.cursor()
 
def menu():
    clear_terminal()
    OCRTunesTitle = pyfiglet.figlet_format("OCRTunes")
    print(Fore.BLUE + Style.BRIGHT + OCRTunesTitle)
    print("Welcome to OCRTunes")
    print("-"*35)
    print("Menu:")
    print("1. Create new account")
    print("2. Edit details")
    print("3. Create, save, view playlists")
    print("4. Exit")
    option = int(input("Enter an option: "))
    if option == 1:
        accountcreation()
    elif option == 2:
        editdetails()
    elif option == 3:
        playlistcreation()
    else:
        print("bye")


def accountcreation():
    username=input("Please enter your chosen username and must be appropriate: ")
    password = input("Please enter a password between 8-20 characters and use some special characters e.g.&@%$: ")
    while len(password) < 8 or len(password) > 20:
        print("Password must be between 8-20 characters.")
        password = input("Please enter a password between 8-20 characters and use some special characters e.g.&@%$: ")
    dateofbirth = int(input("Please enter your date of birth in the format DDMMYYYY: "))
    favouriteartist = str(input("Please enter your favourite artist: "))
    favouritegenre = str(input("Please enter your favourite genre: "))

    try:
        cursor.execute(
            "INSERT INTO users (name, user_password, date_of_birth, favourite_artist, favourite_genre) VALUES (?,?,?,?,?)",
            (username, password, dateofbirth, favouriteartist, favouritegenre)
            )
        print("Account successfuly created")
        time.sleep(2)
        
    except sqlite3.Error as error:
        print(f"There was an error creating the account: {error}")
        time.sleep(2)

    clear_terminal()
    menu()

def editdetails():
    clear_terminal()
    username = str(input("What is your user name: "))
    cursor.execute('SELECT name FROM users')
    rows = cursor.fetchall()
    names = [row[0] for row in rows]
    if username in names:
        password = str(input("What is your password: "))
        cursor.execute('SELECT user_password FROM users WHERE name = ?', (username,))
        stored_password = cursor.fetchone()[0]
        if password == stored_password:
            newfvoriteartist = str(input("Who is your new favorite artist: "))
            cursor.execute('UPDATE users SET favourite_artist = ? WHERE name = ?', (newfvoriteartist, username))
            conn.commit()
            print("Details updated successfully.")
            time.sleep(1)
            menu()
        else:
            print("Password is incorrect")
            time.sleep(1)
            menu()
    else:
        print("Username does not exist")
        time.sleep(1)
        menu()

def playlistcreation():
    print("Playlist creation coming soon...")
    time.sleep(2)
    menu()

menu()