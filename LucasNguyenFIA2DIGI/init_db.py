import sqlite3

connection = sqlite3.connect(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\LucasNguyenFIA2DIGI\schooldatabase.db')

with open(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\LucasNguyenFIA2DIGI/assets/studentsschema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO students (StudentId, Name, Password, YearLevel, TutorCode) VALUES (?, ?, ?, ?, ?)",
            ('25714', 'Lucas Nguyen', '12345', '11', 'S06')
            )


connection.commit()
connection.close()

connection = sqlite3.connect(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\LucasNguyenFIA2DIGI/schooldatabase.db')

with open(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS/LucasNguyenFIA2DIGI/assets/staffschema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO staff (StaffId, TutorCode, StaffName, Username, Password, HouseLeader) VALUES (?, ?, ?, ?, ?, ?)",
            ('DMF',None,'David Fenwick','d.fenwick', '12345', '1')
            )

cur.execute("INSERT INTO staff (StaffId, TutorCode, StaffName, Username, Password, HouseLeader) VALUES (?, ?, ?, ?, ?, ?)",
            ('ANS', 'M07', 'Andrew Smith', 'a.smith', '12345', '0')
            )


connection.commit()
connection.close()

connection = sqlite3.connect(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS/LucasNguyenFIA2DIGI/schooldatabase.db')

with open(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS/LucasNguyenFIA2DIGI/assets/eventsschema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Events (StudentId, SetBy, ConfirmedBy, Details, ImageProof, HousePoints, EventDate) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('25714', 'ANS', 'DMF', 'Lucas saved a homeless child', 'https://stpauls4-my.sharepoint.com/:v:/g/personal/25714_stpauls_qld_edu_au/EcjXyd_iM7tEkDgWdO8KoA8BlhRITs440R5HsJ_q24PCTA?e=Dlz3fE', '10', '2022-09-07')
            )
connection.commit()
connection.close()
