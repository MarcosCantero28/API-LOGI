
from config.db_config import Database


class DireccionDAO:

    @staticmethod
    def getDirecciones():
        query = 'SELECT id,calle,numero_calle,pais,ciudad,latitud,longitud FROM Direccion ORDER BY id'
        results = Database.execute_query(query)
        return results if results else []
    
    @staticmethod
    def getDireccionById(id):
        query = "SELECT id, calle, numero_calle, pais, ciudad, latitud, longitud FROM Direccion WHERE id = %s"
        results = Database.execute_query(query, (id,))
        return results[0] if results else None
    
    @staticmethod
    def post(direccion):
        print(f"Insertando direccion: {direccion}", flush=True)
        
        query = """
            INSERT INTO Direccion (calle, numero_calle, pais, ciudad, latitud, longitud) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (direccion["calle"], direccion["numero_calle"], direccion["pais"],
                 direccion["ciudad"], direccion["latitud"], direccion["longitud"])
        
        print(f"Params: {params}", flush=True)
        direccion_id = Database.execute_update(query, params)
        print(f"ID retornado: {direccion_id}", flush=True)

        if direccion_id:
            inserted = DireccionDAO.getDireccionById(direccion_id)
            print(f"Direccion en BD: {inserted}", flush=True)
            return inserted
        return None
    
    @staticmethod
    def patch(direccion_id, direccion_args):
        direccion = DireccionDAO.getDireccionById(direccion_id)
        if not direccion:
            return None
            
        query = """
            UPDATE Direccion 
            SET calle = %s, numero_calle = %s, pais = %s, ciudad = %s, 
                latitud = %s, longitud = %s 
            WHERE id = %s
        """
        params = (direccion_args["calle"], direccion_args["numero_calle"], 
                 direccion_args["pais"], direccion_args["ciudad"], 
                 direccion_args["latitud"], direccion_args["longitud"], direccion_id)
        
        result = Database.execute_update(query, params)
        
        if result:
            return DireccionDAO.getDireccionById(direccion_id)
        return None
    
    @staticmethod
    def delete(direccion_id):
        direccion = DireccionDAO.getDireccionById(direccion_id)
        
        if direccion:
            query = "DELETE FROM Direccion WHERE id = %s"
            Database.execute_update(query, (direccion_id,))
            
        return direccion

