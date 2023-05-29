DROP TABLE IF EXISTS songs_list;

CREATE TABLE songs_list (
    event_id INTEGER NOT NULL,
    song_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,

    FOREIGN KEY (event_id) REFERENCES events(event_id)
    FOREIGN KEY (song_id) REFERENCES songs(song_id)
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    PRIMARY KEY (event_id, song_id, user_id)

);
