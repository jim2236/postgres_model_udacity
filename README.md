## Purpose of the Sparkify Data and Analytical Goals <br>
The startup Sparkify has library of song data and a collection of logs files of recent user activities.  Users can select from a catalog of songs and listen through a streaming service.  Access to songs and listening activities are captured in log files organized by date.   Management wants to analyze user activity in listening to songs to identify patterns in user listening activities and their preferences.  The goal of the analyses is to identify opportunities to mature their content and deliver offerings. <br>

## Database Schema <br>
The schemas of the songs and log files are not optimal to support analytics efforts.  Song data exists in song files that hold information about a single song and those files exist in a series of folders and subfolders.  Logs events are captured in log files by date in a single directory.  Some data appears in both files while some data fields are have no values.  All data files are in JSON format.  The data has not been normalize to a reasonable degree and any analysis would likely yield low quality results.  We have developed a star database schema to support efficient analytics for management with Fact and Dimension tables.  The Fact table, Songplays, captures data from song play activity by users. The Dimension tables include those tables and content required to support the Fact table: Users, Songs, Artists and Time <br>

**Fact Table** <br>
- songplays - SERIAL<br>
- songplay_id - SERIAL <br>
- start_time -BIGINT <br> 
- user_id - INTEGER <br> 
- level - VARCHAR(20)  <br>
- song_id - VARCHAR(18) <br>
- artist_id - VARCHAR(18)  <br>
- session_id - INTEGER <br>
- location VARCHAR(100)  <br>
- user_agent VARCHAR(150)  <br>

**Dimension Tables** <br>
- users <br>
- user_id - INTEGER <br> 
- first_name - VARCHAR(20) CHECK(LENGTH(TRIM(”first_name”)) > 0) <br> 
- last_name - VARCHAR(20) CHECK(LENGTH(TRIM”(last_name”)) > 0) <br>
- gender VARCHAR(1) <br>
- level - VARCHAR(20) <br>

**songs** <br>
- song_id - VARCHAR(18) <br>
- title - VARCHAR(80) UNIQUE NOT NULL CHECK(LENGTH(TRIM”title”)) > 0) <br>
- artist_id - VARCHAR(18)  <br>
- year - INTEGER <br>
- duration - FLOAT  <br>

**artists** <br>
- artist_id - VARCHAR(18) <br>  
- name - VARCHAR(100) UNIQUE NOT NULL CHECK(LENGTH(TRIM”name”)) > 0) <br>
- location - VARCHAR(30) <br>  
- latitude - VARCHAR(20) <br>
- longitude - VARCHAR(20)  <br>

**time** <br>
- start_time - DATE <br>
- hour - INTEGER <br>
- day - INTEGER <br>
- week - INTEGER <br>
- month - INTEGER <br>
- year - INTEGER <br>
- weekday - INTEGER <br>

## ELT Pipeline <br>
We created an ETL pipeline to transfer data from the songs and log files to the tables in the star schema.  The ETL process first extracts data from the song files, traversing the existing folder structure, and creates a Pandas dataframe to build the Songs table and the Artists table.  Values are extracted from the dataframe and copied into lists to populate the Songs and Artists tables. <br>

The ETL process then traverses the folder structure for the log data and creates a second Pandas dataframe.  The Time table is populated from this data selecting only those records logged from the NextSong web page.  The timestamp data was recorded in integer format representing milliseconds and is converted to a useable time format and time elements.  The respective data fields are selected from the log data dataframe to populate the Users table. <br>

The Songplays table is populated by selecting the song ID and artist ID from the songs and artists table, and then selecting the matching song title, artist name and song duration time. <br>
