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


def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks=cursor.fetchall()
    if tasks:
        print("\n To-Do List")
        for i in tasks:
            print(f"[{i[0]}] [{i[1]}] [{i[2]}]")
    else:
        print("\n No tasks found")

def complete_task():
    view_tasks()
    try:
        task_id=int(input("\nEnter the taskID you want to mark as complete: "))
        cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?",(task_id,))
        conn.commit()
        print(f"Task {task_id} marked as Complete!")
    except ValueError:
        print("Invalid TaskID.")

def delete_task():
    view_tasks()
    try:
        task_id=int(input("\nEnter the taskID you want to delete: "))
        cursor.execute("DELETE FROM tasks WHERE id=?",(task_id,))
        conn.commit()
        print(f"Task {task_id} deleted successfully!")
    except ValueError:
        print("Invalid TaskID.")