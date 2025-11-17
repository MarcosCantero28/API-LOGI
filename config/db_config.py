import mysql.connector
from mysql.connector import Error
from datetime import datetime

class Database:
    """
    Clase para manejar conexiones y operaciones con MySQL
    """
    
    # Configuración de la base de datos
    # IMPORTANTE: Modifica estos valores con tu configuración
    DB_CONFIG = {
        'host': 'localhost',
        'database': 'prueba_api',  # Cambia por el nombre de tu BD
        'user': 'root',              # Cambia por tu usuario
        'password': 'admin',              # Cambia por tu contraseña
        'port': 3306
    }
    
    @staticmethod
    def get_connection():
        """
        Obtiene una conexión a la base de datos MySQL
        
        Returns:
            connection: Objeto de conexión MySQL o None si falla
        """
        try:
            connection = mysql.connector.connect(**Database.DB_CONFIG)
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"❌ Error al conectar a MySQL: {e}")
            return None
    
    @staticmethod
    def execute_query(query, params=None):
        """
        Ejecuta una consulta SELECT y retorna los resultados
        
        Args:
            query (str): Consulta SQL a ejecutar
            params (tuple): Parámetros para la consulta
            
        Returns:
            list: Lista de diccionarios con los resultados
        """
        connection = Database.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(query, params or ())
                results = cursor.fetchall()
                cursor.close()
                connection.close()
                return results
            except Error as e:
                print(f"❌ Error ejecutando query: {e}")
                if connection.is_connected():
                    connection.close()
                return None
        return None
    
    @staticmethod
    def execute_update(query, params=None):
        connection = Database.get_connection()
        if not connection:
            print("Error: No se pudo conectar a la base de datos", flush=True)
            return None
            
        try:
            cursor = connection.cursor()
            cursor.execute(query, params or ())
            connection.commit()
            
            last_id = cursor.lastrowid
            rows_affected = cursor.rowcount
            
            print(f"Query ejecutada - Rows affected: {rows_affected}, Last ID: {last_id}", flush=True)
            
            cursor.close()
            connection.close()
            
            return last_id if last_id > 0 else True
        except Error as e:
            print(f"Error SQL: {e}", flush=True)
            if connection.is_connected():
                connection.rollback()
                connection.close()
            return None
    
    @staticmethod
    def call_procedure(procedure_name, params=None):
        connection = Database.get_connection()
        if not connection:
            print("Error: No se pudo conectar a la base de datos", flush=True)
            return None
            
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.callproc(procedure_name, params or ())
            
            results = []
            for result in cursor.stored_results():
                rows = result.fetchall()
                for row in rows:
                    for key, value in row.items():
                        if isinstance(value, datetime):
                            row[key] = value.isoformat()
                results.extend(rows)
            
            connection.commit()
            cursor.close()
            connection.close()
            
            return results if results else True
        except Error as e:
            print(f"Error ejecutando stored procedure: {e}", flush=True)
            if connection.is_connected():
                connection.rollback()
                connection.close()
            return None
    
    @staticmethod
    def test_connection():
        connection = Database.get_connection()
        if connection:
            print("✅ Conexión exitosa a MySQL")
            connection.close()
            return True
        else:
            print("❌ No se pudo conectar a MySQL")
            return False
