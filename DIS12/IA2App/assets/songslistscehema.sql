DROP TABLE IF EXISTS songslist;

CREATE TABLE songs_list (
    event_id TEXT NOT NULL,
    song_id INTEGER PRIMARY KEY AUTOINCREMENT,


    FOREIGN KEY (event_id) REFERENCES events(event_id)
    FOREIGN KEY (song_id) REFERENCES songs(song_id)
    PRIMARY KEY (event_id, song_id)

);
