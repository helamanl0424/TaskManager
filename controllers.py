from repositories import create_task, get_all_tasks, update_task, delete_task


def add_task(title, description):
    # Add a new task to the database
    # Check if the title and description are not just whitespace
    if title.strip() and description.strip():
        # If valid, create the task using the repository function
        create_task(title, description)
    else:
        # Raise an error if either title or description is empty
        raise ValueError("Title and description cannot be empty.")


def list_tasks():
    # Retrieve all tasks from the database
    # This function calls the repository to get all tasks and return them
    return get_all_tasks()


def remove_task(task_id):
    # Remove a task based on its ID
    # Check if the task ID is provided (not None or empty)
    if task_id:
        # If valid, delete the task using the repository function
        delete_task(task_id)
    else:
        # Raise an error if task ID is not provided
        raise ValueError("Task ID is required for deletion.")


def edit_task(task_id, title, description):
    # Update an existing task's title and description based on its ID
    # Check if the task ID is provided and both title and description are not just whitespace
    if task_id and title.strip() and description.strip():
        # If valid, update the task using the repository function
        update_task(task_id, title, description)
    else:
        # Raise an error if any field is invalid or empty
        raise ValueError("Task ID, title, and description cannot be empty.")
