from config.db_config import Database

class UserDAO:


    @staticmethod
    def getUsers():

        query = "SELECT id, nombre, email, telefono FROM Usuarios ORDER BY id"
        results = Database.execute_query(query)
        return results if results else []
    
    @staticmethod
    def post(user):
        print(f"Insertando usuario: nombre={user['nombre']}, email={user['email']}, telefono={user['telefono']}", flush=True)
        
        query = """
            INSERT INTO Usuarios (nombre, email, telefono) 
            VALUES (%s, %s, %s)
        """
        params = (user["nombre"], user["email"], user["telefono"])
        user_id = Database.execute_update(query, params)
        
        print(f"ID retornado: {user_id}", flush=True)
        
        if user_id:
            inserted_user = UserDAO.getById(user_id)
            print(f"Usuario en BD: {inserted_user}", flush=True)
            
            return {
                "id": user_id,
                "nombre": user["nombre"],
                "email": user["email"],
                "telefono": user["telefono"]
            }
        return None

    # Metodos para un solo usuario
    @staticmethod
    def getById(id):

        query = "SELECT id, nombre, email, telefono FROM Usuarios WHERE id = %s"
        results = Database.execute_query(query, (id,))
        return results[0] if results else None
    
    @staticmethod
    def patch(user_id, user_args):

        # Verificar si el usuario existe
        user = UserDAO.getById(user_id)
        if not user:
            return None
            
        query = """
            UPDATE Usuarios 
            SET nombre = %s, email = %s, telefono = %s 
            WHERE id = %s
        """
        params = (user_args["nombre"], user_args["email"], 
                 user_args["telefono"], user_id)
        
        result = Database.execute_update(query, params)
        
        if result:
            return UserDAO.getById(user_id)
        return None
    
    @staticmethod
    def delete(user_id):

        # Obtener el usuario antes de eliminarlo
        user = UserDAO.getById(user_id)
        
        if user:
            query = "DELETE FROM Usuarios WHERE id = %s"
            Database.execute_update(query, (user_id,))
            
        return user