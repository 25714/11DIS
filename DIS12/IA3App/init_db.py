import sqlite3

connection = sqlite3.connect(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA3App\ndjdatabase.db ')

# with open(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA3App\assets\userschema.sql') as f:
#     connection.executescript(f.read())

with open(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA3App\assets\friendschema.sql') as f:
    connection.executescript(f.read())

with open(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA3App\assets\songsfaveschema.sql') as f:
    connection.executescript(f.read())

with open(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA3App\assets\eventuserschema.sql') as f:
    connection.executescript(f.read())
#
with open(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA3App\assets\eventschema.sql') as f:
    connection.executescript(f.read())

with open(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA3App\assets\songslistscehema.sql') as f:
    connection.executescript(f.read())
#
connection.close()


