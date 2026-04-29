#task.py

class Task:
    def __init__(self, id_tarea, nombre, descripcion=None,
            activa=1, id_estado=None, id_categoria=None):
        self.id_tarea = id_tarea
        self.nombre = nombre
        self.descripcion = descripcion
        self.activa = activa
        self.id_estado = id_estado
        self.id_categoria = id_categoria

    
    


