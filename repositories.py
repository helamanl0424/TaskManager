from models import Session, Task


def create_task(title, description):
    # Creates and adds a new task to the database
    session = Session()  # Start a new database session
    new_task = Task(title=title, description=description)  # Create a new Task object
    session.add(new_task)  # Add the new Task object to the session
    session.commit()  # Commit all pending transactions to write the new task to the database
    session.close()  # Close the session to release resources


def get_all_tasks():
    # Retrieves all tasks from the database
    session = Session()  # Start a new database session
    tasks = session.query(Task).all()  # Query the database for all tasks and return a list of Task objects
    session.close()  # Close the session to release resources
    return tasks  # Return the list of tasks


def update_task(task_id, title, description):
    # Updates an existing task in the database
    session = Session()  # Start a new database session
    task = session.query(Task).filter(
        Task.id == task_id).one()  # Find the task by its ID and retrieve a single instance
    task.title = title  # Update the task's title
    task.description = description  # Update the task's description
    session.commit()  # Commit the changes to the database
    session.close()  # Close the session to release resources


def delete_task(task_id):
    # Deletes a task from the database
    session = Session()  # Start a new database session
    task = session.query(Task).filter(
        Task.id == task_id).one()  # Find the task by its ID and retrieve a single instance
    session.delete(task)  # Delete the found task from the session
    session.commit()  # Commit the deletion to the database
    session.close()  # Close the session to release resources
