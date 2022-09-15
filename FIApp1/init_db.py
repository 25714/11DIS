import sqlite3

connection = sqlite3.connect(r'/LucasNguyenFIA2DIGI/database.db')

with open(r'/LucasNguyenFIA2DIGI/assets/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()
connection.close()

connection = sqlite3.connect(r'/LucasNguyenFIA2DIGI/database.db')

with open(r'/LucasNguyenFIA2DIGI/assets/userschema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
            ('Steven', 'Stark', 'stevenstark@gmail.com', 'IAmIronman')
            )

cur.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
            ('Steven', 'Smash', 'stevensmash@gmail.com', 'HulkSmash')
            )
connection.commit()
connection.close()

connection = sqlite3.connect(r'/LucasNguyenFIA2DIGI/database.db')

with open(r'/LucasNguyenFIA2DIGI/assets/courseschema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO courses (course_id, title, description, credits, term) VALUES (?, ?, ?, ?, ?)",
            ('1111', 'PHP 101', 'Intro in PHP', '3', 'Fall, Spring')
            )

cur.execute("INSERT INTO courses (course_id, title, description, credits, term) VALUES (?, ?, ?, ?, ?)",
            ('2222','Java 1', 'Intro to Java Programming', '4', 'Spring')
            )

cur.execute("INSERT INTO courses (course_id, title, description, credits, term) VALUES (?, ?, ?, ?, ?)",
            ('3333','ADV PHP 201', 'Advanced PHP Programming', '3', 'Fall')
            )

cur.execute("INSERT INTO courses (course_id, title, description, credits, term) VALUES (?, ?, ?, ?, ?)",
            ('4444','Angular 1', 'Intro to Angular', '3', 'Fall, Spring')
            )

cur.execute("INSERT INTO courses (course_id, title, description, credits, term) VALUES (?, ?, ?, ?, ?)",
            ('5555','Java 2', 'Advanced Java Programming', '4', 'Fall')
            )

connection.commit()
connection.close()

connection = sqlite3.connect(r'/LucasNguyenFIA2DIGI/database.db')

with open(r'/LucasNguyenFIA2DIGI/assets/enrolmentschema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO enrolment (course_id, user_id) VALUES (?, ?)",
            ('1111','1')
            )

connection.commit()
connection.close()
