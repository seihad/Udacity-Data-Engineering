import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS user"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE staging_events
(

);
""")

staging_songs_table_create = ("""
""")

songplay_table_create = ("""
CREATE TABLE staging_songs
(
    songplay_id
    start_time
    user_id
    level
    song_id
    artist_id
    session_id
    location
    user_agent
);
""")

user_table_create = ("""
CREATE TABLE user
(
    user_id
    first_name
    last_name
    gender
    level
)
""")

song_table_create = ("""
CREATE TABLE song
(
    song_id
    title
    artist_id
    year
    duration
)
""")

artist_table_create = ("""
CREATE TABLE artist
(
    artist_id
    name
    location
    lattitude
    longitude
)
""")

time_table_create = ("""
CREATE TABLE time
(
    start_time
    hour
    day
    week
    month
    year
    weekday
)
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
