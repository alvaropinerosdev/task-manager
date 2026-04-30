import mysql.connector
from mysql.connector import Error

class Db:

    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="proyecto_1"
            )
            return connection
        except Error as tipo_error:
            print(f"Error de conexion: {tipo_error}")
            return None


    @staticmethod
    def fetch_all(query, params=None):

        conexion = Db.get_connection()
        cursor = conexion.cursor()

        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)

        dato = cursor.fetchall()
        cursor.close()
        conexion.close()

        return dato


    @staticmethod
    def execute_write(query, params=None):

        conexion = Db.get_connection()
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

