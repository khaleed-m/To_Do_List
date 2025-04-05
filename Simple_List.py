import sqlite3

conn=sqlite3.connect("my_database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
conn.commit()

users=[("Bob",30),("Charlie",2)]

cursor.executemany("INSERT INTO users(name,age) VALUES (? ,?)",users)
conn.commit()