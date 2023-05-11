import sqlite3

connection = sqlite3.connect(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA2App\ndjdatabase.db ')

with open(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA2App\assets\userschema.sql') as f:
    connection.executescript(f.read())

with open(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA2App\assets\friendschema.sql') as f:
    connection.executescript(f.read())

connection.close()


