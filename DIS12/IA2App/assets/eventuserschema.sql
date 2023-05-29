DROP TABLE IF EXISTS eventuser;

CREATE TABLE eventuser (
    event_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,


    FOREIGN KEY (event_id) REFERENCES events(event_id)
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    PRIMARY KEY (event_id, user_id)

);
