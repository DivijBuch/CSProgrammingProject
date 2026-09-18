import sqlite3

conn = sqlite3.connect('ocrtunes.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT, user_password, TEXT, date_of_birth NUMBER, favourite_artist TEXT, favourite_genre TEXT)')

# cursor.execute(
# 	'INSERT INTO users VALUES (?, ?, ?, ?, ?)',
# 	(1, 'Divij', '05072010', 'Kanye', 'Rap'),
# )
# conn.commit()


cursor.execute('CREATE TABLE IF NOT EXISTS songs (song_id INTEGER, title TEXT, artist TEXT, genre TEXT, length_seconds INTEGER)')

# cursor.execute(
# 	'INSERT INTO songs VALUES (?, ?, ?, ?, ?)',
# 	(1, 'Flashing Lights', 'Kanye West', 'Rap', 120),
# )
# conn.commit()



conn.commit()
conn.close()