DROP TABLE IF EXISTS djuser;

CREATE TABLE djuser (
    user_id INTEGER NOT NULL,
    dj_id INTEGER NOT NULL,



    FOREIGN KEY (user_id) REFERENCES users(user_id)
    FOREIGN KEY (dj_id) REFERENCES djs(dj_id)
    PRIMARY KEY (user_id, dj_id)
);
