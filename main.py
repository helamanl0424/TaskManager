import tkinter as tk
from tkinter import simpledialog, messagebox, Listbox, Scrollbar, Frame
from controllers import add_task, list_tasks, remove_task, edit_task


def refresh_task_list():
    tasks_listbox.delete(0, tk.END)
    tasks = list_tasks()
    for task in tasks:
        tasks_listbox.insert(tk.END, f"{task.id}: {task.title}")


def add_task_popup():
    title = simpledialog.askstring("Add Task", "Enter task title:")
    description = simpledialog.askstring("Add Task", "Enter task description:")
    if title and description:
        add_task(title, description)
        refresh_task_list()


def delete_task_popup():
    task_id = simpledialog.askinteger("Delete Task", "Enter task ID to delete:")
    if task_id is not None:
        remove_task(task_id)
        refresh_task_list()


def update_task_popup():
    task_id = simpledialog.askinteger("Update Task", "Enter task ID to update:")
    title = simpledialog.askstring("Update Task", "Enter new title:")
    description = simpledialog.askstring("Update Task", "Enter new description:")
    if task_id is not None and title and description:
        edit_task(task_id, title, description)
        refresh_task_list()


app = tk.Tk()
app.title('Task Manager')

# Task list with scrollbar
frame = Frame(app)
scrollbar = Scrollbar(frame)
tasks_listbox = Listbox(frame, yscrollcommand=scrollbar.set, width=50, height=10)
scrollbar.config(command=tasks_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame.pack()

# Buttons for task operations
add_button = tk.Button(app, text="Add Task", command=add_task_popup)
add_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", command=delete_task_popup)
delete_button.pack(pady=5)

update_button = tk.Button(app, text="Update Task", command=update_task_popup)
update_button.pack(pady=5)

refresh_button = tk.Button(app, text="Refresh Tasks", command=refresh_task_list)
refresh_button.pack(pady=5)

refresh_task_list()  # Initial load of tasks
app.mainloop()
