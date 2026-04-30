#Task_manager.py
from Task import Task
from Db import Db


class TaskManager:
    def __init__(self):
        pass

    def get_all(self):
        filas = Db.fetch_all("select * from tarea")
        tasks = [Task.from_dict(fila) for fila in filas]
        return tasks
    
