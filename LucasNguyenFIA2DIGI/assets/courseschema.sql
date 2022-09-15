DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    credits INTEGER NOT NULL,
    term TEXT NOT NULL
);
