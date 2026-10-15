import sqlite3

conn = sqlite3.connect('OCRtunes.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, user_password TEXT, date_of_birth NUMBER, favourite_artist TEXT, favourite_genre TEXT)')

cursor.execute('CREATE TABLE IF NOT EXISTS songs (song_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, artist TEXT, genre TEXT, length_seconds INTEGER)')

cursor.execute('CREATE TABLE IF NOT EXISTS playlists (playlist_id INTEGER PRIMARY KEY AUTOINCREMENT, playlist_name TEXT, user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(user_id))')

cursor.execute('CREATE TABLE IF NOT EXISTS playlist_songs (playlist_song_id INTEGER PRIMARY KEY AUTOINCREMENT, playlist_id INTEGER, song_id INTEGER, user_id INTEGER, FOREIGN KEY(playlist_id) REFERENCES playlists(playlist_id), FOREIGN KEY(song_id) REFERENCES songs(song_id), FOREIGN KEY(user_id) REFERENCES users(user_id))')


conn.commit()
conn.close()