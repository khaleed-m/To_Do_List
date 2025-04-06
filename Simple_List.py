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

cursor.execute("SELECT * FROM users")
rows=cursor.fetchall()
for i in rows:
    print(i)


conn.close()

conn=sqlite3.connect("my_database.db")
cursor=conn.cursor()

cursor.execute("INSERT INTO users(name,age)VALUES(?,?)",("Alexis",42))
conn.commit()
conn.close()

conn=sqlite3.connect("my_database.db")
cursor=conn.cursor()

cursor.execute("SELECT * FROM users")
rows=cursor.fetchall()
for i in rows:
    print(i)
    