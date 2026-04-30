#Db.py

import mysql.connector
from mysql.connector import Error

class Db: 
    def get_connection():

        try:
            connection = mysql.connector.connect(
                    host = "localhost",
            user = "root",
                password = "root",
                database = "proyecto_1"
            )
            return connection #Se retornan los datos para poder usar la conexion fuera de la funcion.
    
        except Error as tipo_error:
            print(f"Error de conexion: {tipo_error}")
            return None #Retornamos none para indicar un error, es una forma standar de python
    
    if __name__ == "__main__":
        connection = get_connection()

        if connection:
            print("Conexion exitosa")
            connection.close()
        else: 
            print ("Fallo la conexion")
    

        #Hacer la consulta bompleta
def fetch_all(query, params=None):

    conexion = get_connection()
    cursor = conexion.cursor()

    if params is None:
        cursor.execute(query)
    else:
        cursor.execute(query, params)

    dato = cursor.fetchall()
    cursor.close()
    conexion.close()

    return dato


def execute_write(query, params=None):

    conexion = get_connection()
    cursor = conexion.cursor()

    if params is None:
        cursor.execute(query)
    else:
        cursor.execute(query, params)

    conexion.commit()
    affected = cursor.rowcount
    cursor.close()
    conexion.close()

    return affected
    

