from repositories import create_task, get_all_tasks, update_task, delete_task


def add_task(title, description):
    if title.strip() and description.strip():
        create_task(title, description)
    else:
        raise ValueError("Title and description cannot be empty.")


def list_tasks():
    return get_all_tasks()


def remove_task(task_id):
    if task_id:
        delete_task(task_id)
    else:
        raise ValueError("Task ID is required for deletion.")


def edit_task(task_id, title, description):
    if task_id and title.strip() and description.strip():
        update_task(task_id, title, description)
    else:
        raise ValueError("Task ID, title, and description cannot be empty.")
