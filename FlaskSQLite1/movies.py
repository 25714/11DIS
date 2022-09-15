import sqlite3
connection = sqlite3.connect('movies.db')
cursor = connection()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
    (Title TEXT, Director TEXT, Year INT)''')

connection.commit()
connection.close()
