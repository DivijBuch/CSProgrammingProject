import sqlite3

conn = sqlite3.connect('OCRtunes.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS songs (song_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, artist TEXT, genre TEXT, length_seconds INTEGER)')

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Flashing Lights', 'Kanye West', 'Rap', 237),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('I Wonder', 'Kanye West', 'Rap', 243),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Bound 2', 'Kanye West', 'R&B', 229),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Stronger', 'Kanye West', 'Rap', 311),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Starboy', 'The Weeknd', 'R&B', 230),
)


cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Blinding Lights', 'The Weeknd', 'R&B', 200),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Timeless', 'The Weeknd', 'Rap', 256),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Save your tears', 'The Weeknd', 'R&B', 215),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Cruel Summer', 'Taylor Swift', 'Pop', 178),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Lover', 'Taylor Swift', 'Pop', 221),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Shake It Off', 'Taylor Swift', 'Pop', 219),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Love Story', 'Taylor Swift', 'Pop', 236),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Chest Pain', 'Malcom Todd', 'Pop', 200),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Roomates', 'Malcom Todd', 'R&B', 314),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Earrings', 'Malcom Todd', 'R&B', 151),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Sweet Boy', 'Malcom Todd', 'R&B', 180),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Fancy', 'Drake', 'Rap', 319),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Passionfruit', 'Drake', 'Rap', 298),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Headlines', 'Drake', 'Rap', 235),
)

cursor.execute(
    'INSERT INTO songs (title, artist, genre, length_seconds) VALUES (?, ?, ?, ?)',
    ('Classic', 'Drake', 'Rap', 179),
)

conn.commit()
conn.close()