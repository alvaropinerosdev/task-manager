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
    def fetch_all(consulta):

        conexion = get_connection()
        #abrir la conexion y tenerla estable
        cursor = conexion.cursor()
        cursor.execute(consulta)
        r = cursor.fetchall()
        #hacer la consulta y traerla
        cursor.close()
        conexion.close()
        #cerrar todo
        return r
    

