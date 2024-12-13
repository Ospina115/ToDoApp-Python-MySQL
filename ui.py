# Módulo para la interfaz gráfica

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox
from controllers import TaskController
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Título de la tarea")
        self.layout.addWidget(self.title_input)

        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Descripción de la tarea")
        self.layout.addWidget(self.description_input)

        self.add_task_button = QPushButton("Agregar Tarea")
        self.layout.addWidget(self.add_task_button)

        self.complete_task_button = QPushButton("Marcar como Completada")
        self.layout.addWidget(self.complete_task_button)

        self.delete_task_button = QPushButton("Eliminar Tarea Completada")
        self.layout.addWidget(self.delete_task_button)

        self.export_button = QPushButton("Exportar Tareas")
        self.layout.addWidget(self.export_button)

        self.import_button = QPushButton("Importar Tareas")
        self.layout.addWidget(self.import_button)

        self.controller = TaskController()

        self.add_task_button.clicked.connect(self.add_task)
        self.complete_task_button.clicked.connect(self.complete_task)
        self.delete_task_button.clicked.connect(self.delete_task)
        self.export_button.clicked.connect(self.export_tasks)
        self.import_button.clicked.connect(self.import_tasks)

        self.load_tasks()

    def add_task(self):
        title = self.title_input.text()
        description = self.description_input.text()
        if title and description:
            self.controller.add_task(title, description)
            self.load_tasks()
            self.title_input.clear()
            self.description_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un título y una descripción.")

    def load_tasks(self):
        self.task_list.clear()
        tasks = self.controller.get_tasks()
        for task in tasks:
            status = "✔️" if task.completed else "✖️"
            self.task_list.addItem(f"{status} {task.title}: {task.description}")

    def complete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            title = selected_item.text().split(":")[0][2:]  # Extraer el título
            self.controller.mark_task_completed(title)
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Error", "Por favor, seleccione una tarea para marcar como completada.")

    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item and "✔️" in selected_item.text():
            title = selected_item.text().split(":")[0][2:]  # Extraer el título
            self.controller.delete_task(title)
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Error", "Por favor, seleccione una tarea completada para eliminar.")

    def export_tasks(self):
        tasks = self.controller.get_tasks()
        with open('tasks.json', 'w') as f:
            json.dump([task.__dict__ for task in tasks], f)
        QMessageBox.information(self, "Éxito", "Tareas exportadas exitosamente.")

    def import_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                tasks_data = json.load(f)
                for task_data in tasks_data:
                    self.controller.add_task(task_data['title'], task_data['description'], task_data['completed'])
                self.load_tasks()
            QMessageBox.information(self, "Éxito", "Tareas importadas exitosamente.")
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "El archivo de tareas no se encontró.")
        except json.JSONDecodeError:
            QMessageBox.warning(self, "Error", "Error al leer el archivo de tareas.")
