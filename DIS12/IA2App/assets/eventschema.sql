DROP TABLE IF EXISTS events;

CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT NOT NULL,
    private TEXT NOT NULL,
    details TEXT NOT NULL,
    host TEXT NOT NULL,
    dj TEXT NOT NULL,
    start-date DATE NOT NULL,
    end_date DATE NOT NULL
);
