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
    print("5. Export artists songs")
    print("6. Exit")
    option = int(input("Enter an option: "))
    if option == 1:
        accountcreation()
    elif option == 2:
        editdetails()
    elif option == 3:
        songs()
    elif option == 4:
        playlistcreation()
    elif option == 5:
        export_artists_songs()
    else:
        print("Thank you for using OCRTunes. Goodbye!")

def export_artists_songs():
    artist_name = input("Enter the artist's name: ").strip()
    if not artist_name:
        print("Artist name cannot be empty.")
        return

    cursor.execute(
        'SELECT title, artist, genre, length_seconds '
        'FROM songs WHERE LOWER(TRIM(artist)) = LOWER(?) '
        'ORDER BY title',
        (artist_name,)
    )
    artist_songs = cursor.fetchall()

    if not artist_songs:
        print(f"No songs found for '{artist_name}'.")
        return

    safe_artist_name = "".join(
        character for character in artist_name
        if character.isalnum() or character in (" ", "-", "_")
    ).strip().replace(" ", "_")
    file_name = f"{safe_artist_name}_songs.txt"

    try:
        with open(file_name, "w", encoding="utf-8") as song_file:
            for title, artist, genre, length in artist_songs:
                song_file.write(
                    f"Title: {title}, Artist: {artist}, Genre: {genre}, "
                    f"Length: {length} seconds\n"
                )
    except OSError as error:
        print(f"Could not save the songs to '{file_name}': {error}")
        return

    print(f"Saved {len(artist_songs)} song(s) to '{file_name}'.")

def accountcreation():
    username=input("Please enter your chosen username and must be appropriate: ")
    password = input("Please enter a password between 8-20 characters: ")
    while len(password) < 8 or len(password) > 20:
        print("Password must be between 8-20 characters.")
        password = input("Please enter a password between 8-20 characters: ")
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
        menu()
        
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
    view_song_choice = int(input("Press 1 to return to the main menu or 2 to exit the program: "))
    
    if view_song_choice == 1:
        menu()
    else:
        clear_terminal()
        print("Thank you for using OCRTunes. Goodbye!")
        time.sleep(1)
        exit()


def playlistcreation():
    clear_terminal()
    print("Sign in to create/view a playlist")
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
            print("3. View songs in playlist")
            playlist_option = int(input("Enter an option: "))
            if playlist_option == 1:
                create_playlist(username)
            elif playlist_option == 2:
                view_playlists(username)
            elif playlist_option == 3:
                playlist_name = input("Enter the name of the playlist you want to view: ")
                view_playlist_songs(username, playlist_name)
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
    playlist_name = input("Enter a name for your new playlist: ")
    user_time_limit = int(input("Enter a time limit for your playlist(seconds): "))
    user_genre = input("Enter the genre of your playlist: ")

    cursor.execute('SELECT user_id FROM users WHERE name = ?', (username,))
    user_id = cursor.fetchone()[0]

    cursor.execute(
        'SELECT song_id, title, artist, length_seconds '
        'FROM songs WHERE LOWER(genre) = LOWER(?)',
        (user_genre,)
    )
    available_songs = cursor.fetchall()
    random.shuffle(available_songs)

    selected_songs = []
    total_length = 0

    for song in available_songs:
        if len(selected_songs) >= 5:
            break

        if total_length + song[3] <= user_time_limit:
            selected_songs.append(song)
            total_length += song[3]

    if not selected_songs:
        print("No songs fit this genre and time limit.")
        return

    cursor.execute(
        'INSERT INTO playlists (playlist_name, user_id) VALUES (?, ?)',
        (playlist_name, user_id)
    )

    playlist_id = cursor.lastrowid

    for song in selected_songs:
        cursor.execute(
            'INSERT INTO playlist_songs (playlist_id, song_id, user_id) '
            'VALUES (?, ?, ?)',
            (playlist_id, song[0], user_id)
        )

    conn.commit()

    print(f"Playlist '{playlist_name}' saved successfully.")
    print("Songs included:")

    for song in selected_songs:
        print(f"{song[1]} - {song[2]} ({song[3]} seconds)")

    print(f"Total length: {total_length} seconds")

def view_playlists(username):
    cursor.execute('SELECT user_id FROM users WHERE name = ?', (username,))
    user_id = cursor.fetchone()[0]
    cursor.execute('SELECT playlist_name FROM playlists WHERE user_id = ?', (user_id,))
    playlists = cursor.fetchall()
    if playlists:
        print("Your playlists:")
        for row in playlists:
            print(f'- {row[0]}')
            time.sleep(1)
            view_playlist_choice = int(input("Press 1 to go back to main menu, 2 to go back to create/view a playlist or 3 to exit the program: "))
            if view_playlist_choice == 1:
                menu()
            if view_playlist_choice == 2:
                playlistcreation()
            else:
                print("Thank you for using OCRTunes")
                

    else:
        print("You have no playlists.")
        time.sleep(1)
        menu()

def view_playlist_songs(username, playlist_name):
    cursor.execute(
        'SELECT playlists.playlist_id '
        'FROM playlists '
        'JOIN users ON playlists.user_id = users.user_id '
        'WHERE users.name = ? AND playlists.playlist_name = ?',
        (username, playlist_name)
    )
    playlists = cursor.fetchall()

    if not playlists:
        print(f"You do not have a playlist named '{playlist_name}'.")
        return

    cursor.execute(
        'SELECT songs.title, songs.artist, songs.length_seconds '
        'FROM playlist_songs '
        'JOIN songs ON playlist_songs.song_id = songs.song_id '
        'JOIN playlists ON playlist_songs.playlist_id = playlists.playlist_id '
        'JOIN users ON playlists.user_id = users.user_id '
        'WHERE users.name = ? AND playlists.playlist_name = ? '
        'ORDER BY songs.title',
        (username, playlist_name)
    )
    songs_in_playlist = cursor.fetchall()

    print(f"Songs in '{playlist_name}':")
    if not songs_in_playlist:
        print("This playlist has no songs.")
        return

    for title, artist, length in songs_in_playlist:
        print(f"{title} - {artist} ({length} seconds)")

menu()