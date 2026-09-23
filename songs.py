import sqlite3

conn = sqlite3.connect('OCRtunes.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS songs (song_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, artist TEXT, genre TEXT, length_seconds INTEGER)')

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Flashing Lights', 'Kanye West', 'RAP', 237),
)
conn.commit()

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('24K Magic', 'Bruno Mars', 'Pop', 226),
)
conn.commit()

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Starboy', 'The Weeknd', 'R&B', 230),
)
conn.commit()
conn.close()