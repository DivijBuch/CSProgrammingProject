import os
import sqlite3
import pyfiglet
from colorama import Fore, Back, Style, init
init(autoreset=True)

def clear_terminal():
    # Clears terminal: 'cls' for Windows, 'clear' for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')
connection = sqlite3.connect("OCRtunes.db")
cursor = connection.cursor()

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
    option = int(input("Enter an option: "))
    if option == 1:
        accountcreation()



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
        
    except sqlite3.Error as error:
        print(f"There was an error creating the account: {error}")

    connection.commit()
    connection.close()
    clear_terminal()
    menu()

menu()