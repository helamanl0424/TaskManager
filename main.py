import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, Frame, ttk
from controllers import add_task, list_tasks, remove_task, edit_task


# Define a custom dialog class for adding and editing tasks
class TaskDialog(tk.Toplevel):
    def __init__(self, parent, title=None, task=None):
        super().__init__(parent)
        self.transient(parent)
        self.title(title)

        self.task = task
        self.result = None

        body = tk.Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+{}+{}".format(parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))

        self.initial_focus.focus_set()
        self.wait_window(self)

    # Layout the body of the dialog, including input fields for task title and description
    def body(self, master):
        tk.Label(master, text="Title:").grid(row=0)
        self.title_entry = tk.Entry(master)
        self.title_entry.grid(row=0, column=1)

        tk.Label(master, text="Description:").grid(row=1)
        self.description_entry = tk.Entry(master)
        self.description_entry.grid(row=1, column=1)

        # Prefill fields if editing an existing task
        if self.task:
            self.title_entry.insert(0, self.task.title)
            self.description_entry.insert(0, self.task.description)

        return self.title_entry

    # Add control buttons and define their behavior
    def buttonbox(self):
        box = tk.Frame(self)

        submit_btn = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        submit_btn.pack(side=tk.LEFT, padx=5, pady=5)
        cancel_btn = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        cancel_btn.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    # Define action for OK button which includes validation and destruction of the dialog
    def ok(self, event=None):
        self.result = (self.title_entry.get(), self.description_entry.get())
        self.destroy()

    # Cancel and close the dialog
    def cancel(self, event=None):
        self.destroy()


# Function to refresh the list of tasks displayed in the main application window
def refresh_task_list():
    tasks_listbox.delete(0, tk.END)
    tasks = list_tasks()
    for task in tasks:
        tasks_listbox.insert(tk.END, f"{task.id}: {task.title}, {task.description}")


# Define popup for adding new tasks using the custom dialog
def add_task_popup():
    result = show_task_dialog(app, "Add Task")
    if result:
        title, description = result
        try:
            add_task(title, description)
            refresh_task_list()
        except ValueError as e:
            messagebox.showerror("Error", str(e))


# Define popup for updating existing tasks
def update_task_popup():
    selected = tasks_listbox.curselection()
    if selected:
        selected_id = int(tasks_listbox.get(selected[0]).split(':')[0])
        task = next((t for t in list_tasks() if t.id == selected_id), None)
        result = show_task_dialog(app, "Update Task", task)
        if result:
            title, description = result
            try:
                edit_task(selected_id, title, description)
                refresh_task_list()
            except ValueError as e:
                messagebox.showerror("Error", str(e))


# Define popup for deleting tasks
def delete_task_popup():
    selected = tasks_listbox.curselection()
    if selected:
        selected_id = int(tasks_listbox.get(selected[0]).split(':')[0])
        try:
            remove_task(selected_id)
            refresh_task_list()
        except ValueError as e:
            messagebox.showerror("Error", str(e))


# Helper function to display the TaskDialog and return the result
def show_task_dialog(parent, title, task=None):
    dialog = TaskDialog(parent, title, task)
    return dialog.result


# Set up the main application window
app = tk.Tk()
app.title('Task Manager')

# Set up the main frame and scrollbar for task list
frame = Frame(app)
scrollbar = Scrollbar(frame)
tasks_listbox = Listbox(frame, yscrollcommand=scrollbar.set, width=50, height=10)
scrollbar.config(command=tasks_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame.pack()

# Add buttons for task operations
add_button = tk.Button(app, text="Add Task", command=add_task_popup)
add_button.pack(pady=5)

update_button = tk.Button(app, text="Update Task", command=update_task_popup)
update_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", command=delete_task_popup)
delete_button.pack(pady=5)

refresh_button = tk.Button(app, text="Refresh Tasks", command=refresh_task_list)
refresh_button.pack(pady=5)

# Initial refresh of the task list and start the main application loop
refresh_task_list()
app.mainloop()
