DROP TABLE IF EXISTS songs_fave;

CREATE TABLE songs_fave (
    user_id TEXT NOT NULL,
    song_id INTEGER PRIMARY KEY AUTOINCREMENT,


    FOREIGN KEY (user_id) REFERENCES users(user_id)
    FOREIGN KEY (song_id) REFERENCES songs(song_id)
    PRIMARY KEY (user_id, song_id)

);
