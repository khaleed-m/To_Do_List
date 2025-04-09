import sqlite3
conn=sqlite3.connect("tasks.db")
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY,
    task TEXT,
    status TEXT
)""")
conn.commit()



# Add tasks
# View tasks
# complete tasks
# Delete tasks

def add_task():
    task=input("Enter task: ").strip()
    if task:
        cursor.execute("INSERT INTO tasks(task,status) VALUES(?,?)",
                       (task,"pending"))
        conn.commit()
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty")
        