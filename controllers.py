# Módulo para manejar la lógica de la aplicación

from database import get_session
from models import Task

class TaskController:
    def __init__(self):
        self.session = get_session()

    def add_task(self, title, description, completed=False):
        new_task = Task(title=title, description=description, completed=completed)
        self.session.add(new_task)
        self.session.commit()

    def get_tasks(self):
        return self.session.query(Task).all()

    def mark_task_completed(self, title):
        task = self.session.query(Task).filter(Task.title == title).first()
        if task:
            task.completed = True
            self.session.commit()

    def delete_task(self, title):
        task = self.session.query(Task).filter(Task.title == title).first()
        if task:
            self.session.delete(task)
            self.session.commit()