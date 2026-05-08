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
    def fetch_all(query, params=None, cursor=None, conexion=None ):

        conexion = Db.get_connection()
        if conexion is None:
            return None
            
        cursor = conexion.cursor()
        
        try:

            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)

            return cursor.fetchall()
            

        except Error as tipo_error:
            print(f"Error en conexion: {tipo_error}")
            return None

        finally:
            if cursor is not None:
                cursor.close()
            
            if conexion:
                conexion.close()



    @staticmethod
    def execute_write(query, params=None, cursor= None, conexion= None):

        conexion = Db.get_connection()

        if conexion is None:
            return None
        
        cursor = conexion.cursor()

        try:
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)

            conexion.commit()

            affected = cursor.rowcount

            return affected

        except Error as tipo_error:
            print(f"Error en conexion: {tipo_error}")
            return None
        
        finally:
            if cursor is not None:
                cursor.close()
            if conexion:
                conexion.close()

        
    
    @staticmethod
    def execute_read(query, params=None, fetchone=False, cursor=None, conexion=None):

        conexion = Db.get_connection()

        if conexion is None:
            return None
        
        cursor = conexion.cursor()

            
        try:
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)

            if fetchone:
                return cursor.fetchone()

            else:
                return cursor.fetchall()

            
        finally:
            if cursor is not None:
                    cursor.close()
            if conexion:
                conexion.close()
