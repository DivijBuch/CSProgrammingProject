import os
import sqlite3
import pyfiglet
from colorama import Fore, Style, init
import time
import random

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
    print("3. View songs")
    print("4. Create, save, view playlists")
    print("5. Exit")
    option = int(input("Enter an option: "))
    if option == 1:
        accountcreation()
    elif option == 2:
        editdetails()
    elif option == 3:
        songs()
    elif option == 4:
        playlistcreation()
    else:
        print("Thank you for using OCRTunes. Goodbye!")


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
            new_favorite_artist = str(input("Who is your new favorite artist: "))
            cursor.execute('UPDATE users SET favourite_artist = ? WHERE name = ?', (new_favorite_artist, username))
            conn.commit()
            new_favorite_genre = str(input("What is your new favorite genre: "))
            cursor.execute('UPDATE users SET favourite_genre = ? WHERE name = ?', (new_favorite_genre, username))
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

def songs():
    clear_terminal()
    cursor.execute('SELECT title, artist, length_seconds FROM songs ORDER BY title ASC')
    rows = cursor.fetchall()
    for row in rows:
        time.sleep(0.5)
        print(f"Title: {row[0]}, Artist: {row[1]}, Length(seconds): {row[2]}")
    time.sleep(2)
    view_song_choice = int(input("Press 1 to return to the main menu or 2 to exit the program."))
    
    if view_song_choice == 1:
        menu()
    else:
        clear_terminal()
        print("Thank you for using OCRTunes. Goodbye!")
        time.sleep(1)
        exit()


def playlistcreation():
    clear_terminal()
    print("Sign in to create/save/view a playlist")
    username = str(input("What is your user name: "))
    cursor.execute('SELECT name FROM users')
    rows = cursor.fetchall()
    names = [row[0] for row in rows]
    if username in names:
        password = str(input("What is your password: "))
        cursor.execute('SELECT user_password FROM users WHERE name = ?', (username,))
        stored_password = cursor.fetchone()[0]
        if password == stored_password:
            print("1. Create a new playlist")
            print("2. View existing playlists")
            playlist_option = int(input("Enter an option: "))
            if playlist_option == 1:
                create_playlist(username)
            elif playlist_option == 2:
                playlistname = str(input("Enter the name of the playlist you want to view: "))
                view_playlists(username, playlistname)
            else:
                print("Invalid option. Returning to main menu.")
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

def create_playlist(username):
    playlist_name = str(input("Enter a name for your new playlist: "))
    cursor.execute('SELECT user_id FROM users WHERE name = ?', (username,))
    user_id = cursor.fetchone()[0]
    cursor.execute('INSERT INTO playlists (playlist_name, user_id) VALUES (?, ?)', (playlist_name, user_id))
    conn.commit()

def view_playlists(username, playlist_name):
    cursor.execute('SELECT user_id FROM users WHERE name = ?', (username,))
    user_id = cursor.fetchone()[0]
    cursor.execute('SELECT playlist_name FROM playlists WHERE user_id = ?', (user_id,))
    playlists = cursor.fetchall()
    if playlists:
        print("Your playlists:")
        for playlist in playlists:
            print(playlist[0])
    else:
        print("You have no playlists.")
menu()