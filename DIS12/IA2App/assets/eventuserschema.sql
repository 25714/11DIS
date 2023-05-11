DROP TABLE IF EXISTS eventuser;

CREATE TABLE eventuser (
    event_id INTEGER NOT NULL,
    user_id INTEGER PRIMARY KEY,


    FOREIGN KEY (event_id) REFERENCES event(event_id)
    FOREIGN KEY (user_id) REFERENCES user(user_id)
    PRIMARY KEY (event_id, user_id)

);
