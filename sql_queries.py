# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, start_time DATE, user_id INTEGER, level VARCHAR(20), song_id VARCHAR(18), artist_id VARCHAR(18), session_id INTEGER, location VARCHAR(100), user_agent VARCHAR(150))
""")


user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id INTEGER, first_name VARCHAR(20) CHECK (LENGTH(TRIM("first_name")) > 0), last_name VARCHAR(20) CHECK(LENGTH(TRIM("last_name")) > 0), gender VARCHAR(1), level VARCHAR(20))
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR(18), title VARCHAR(80) NOT NULL CHECK(LENGTH(TRIM("title")) > 0), artist_id VARCHAR(18), year INTEGER, duration FLOAT)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR(18), name VARCHAR(100) NOT NULL CHECK(LENGTH(TRIM("name")) > 0), location VARCHAR(30), latitude VARCHAR(20), longitude VARCHAR(20))
""")
 
time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time date, hour INTEGER, day INTEGER, week INTEGER, month INTEGER, year INTEGER, weekday INTEGER)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id FROM songs s JOIN artists a ON s.artist_id = a.artist_id WHERE s.title = %s AND a.name = %s AND s.duration = %s 
""")

# QUERY LISTS

create_table_queries = [song_table_create, user_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]