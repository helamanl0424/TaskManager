from models import Session, Task


def create_task(title, description):
    session = Session()
    new_task = Task(title=title, description=description)
    session.add(new_task)
    session.commit()
    session.close()


def get_all_tasks():
    session = Session()
    tasks = session.query(Task).all()
    session.close()
    return tasks


def update_task(task_id, title, description):
    session = Session()
    task = session.query(Task).filter(Task.id == task_id).one()
    task.title = title
    task.description = description
    session.commit()
    session.close()


def delete_task(task_id):
    session = Session()
    task = session.query(Task).filter(Task.id == task_id).one()
    session.delete(task)
    session.commit()
    session.close()
