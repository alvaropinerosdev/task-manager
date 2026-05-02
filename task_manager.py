# Task_manager.py
from Task import Task
from Db import Db


class TaskManager:
    def __init__(self):
        pass

    def get_all(self):
        filas = Db.fetch_all("select * from tareas")
        tasks = [Task.from_dict(fila) for fila in filas]
        return tasks
    
    def get_by_id(self, id_tarea):
        data = Db.execute_read(
            "select * from tareas where id_tarea = %s",
            (id_tarea,)
        )

        if not data:
            return None

        task = Task.from_dict(data[0])
        return task
    
    def add(self, nombre, descripcion, activa, id_estado, id_categoria):
        if nombre is None:
            return None
        else:
            query = "INSERT INTO tareas (nombre, descripcion, activa, id_estado, id_categoria) VALUES (%s, %s, %s, %s, %s)"
            params = (nombre, descripcion, activa, id_estado, id_categoria)
            return Db.execute_write(query, params)
                
    def delete(self, id_tarea):
        if id_tarea is not None:
            data = self.get_by_id(id_tarea)

            if not data:
                return False
            
            else:
                query = "DELETE FROM tareas WHERE id_tarea = %s;"
                params = (id_tarea,)
                Db.execute_write(query, params)
                return True