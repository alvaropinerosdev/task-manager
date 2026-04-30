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

    #Convertir de tarea a diccionario
    def to_dict(self):
        data = {

            "id_tarea" : self.id_tarea,
            "nombre" : self.nombre,
            "descripcion" : self.descripcion,
            "activa" : self.activa,
            "id_estado" : self.id_estado,
            "id_categoria" : self.id_categoria

        }
        return data
    
    @staticmethod
    def from_dict(data):
        return Task(
            data[0],  # id_tarea
            data[1],  # nombre
            data[2],  # descripcion
            data[3],  # activa
            data[4],  # id_estado
            data[5]   # id_categoria
        )
        


