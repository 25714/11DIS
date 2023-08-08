DROP TABLE IF EXISTS friend;

CREATE TABLE friend (
    user_id_1 INTEGER NOT NULL,
    user_id_2 INTEGER NOT NULL,



    FOREIGN KEY (user_id_1) REFERENCES users(user_id)
    FOREIGN KEY (user_id_2) REFERENCES users(user_id)
    PRIMARY KEY (user_id_1, user_id_2)

);
