DROP TABLE IF EXISTS songs_fave;

CREATE TABLE songs_fave (
    user_id INTEGER NOT NULL,
    song_id INTEGER NOT NULL,


    FOREIGN KEY (user_id) REFERENCES users(user_id)
    PRIMARY KEY (user_id, song_id)

);
