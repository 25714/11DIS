DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email UNIQUE TEXT NOT NULL,
    password TEXT NOT NULL,
    dob DATE NOT NULL
);
