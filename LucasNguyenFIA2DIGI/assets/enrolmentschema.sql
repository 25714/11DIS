DROP TABLE IF EXISTS enrolment;

CREATE TABLE enrolment (
    course_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    PRIMARY KEY (course_id, user_id)
);
