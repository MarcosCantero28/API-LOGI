from config.db_config import Database


class TarifarioDAO:

    @staticmethod
    def getTarifarios():
        query = 'SELECT id, codigo_postal, tarifa_base, tarifa_kg_adicional, tarifa_volumen_adicional, zona_geografica FROM Tarifario ORDER BY id'
        results = Database.execute_query(query)
        return results if results else []
    
    @staticmethod
    def getById(id):
        query = "SELECT id, codigo_postal, tarifa_base, tarifa_kg_adicional, tarifa_volumen_adicional, zona_geografica FROM Tarifario WHERE id = %s"
        results = Database.execute_query(query, (id,))
        return results[0] if results else None
    
    @staticmethod
    def getByCodigoPostal(codigo_postal):
        query = "SELECT id, codigo_postal, tarifa_base, tarifa_kg_adicional, tarifa_volumen_adicional, zona_geografica FROM Tarifario WHERE codigo_postal = %s"
        results = Database.execute_query(query, (codigo_postal,))
        return results[0] if results else None
    
    @staticmethod
    def post(tarifario):
        print(f"Insertando tarifario: {tarifario}", flush=True)
        
        query = """
            INSERT INTO Tarifario (codigo_postal, tarifa_base, tarifa_kg_adicional, tarifa_volumen_adicional, zona_geografica) 
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (tarifario["codigo_postal"], tarifario["tarifa_base"], 
                 tarifario["tarifa_kg_adicional"], tarifario["tarifa_volumen_adicional"], 
                 tarifario["zona_geografica"])
        
        print(f"Params: {params}", flush=True)
        tarifario_id = Database.execute_update(query, params)
        print(f"ID retornado: {tarifario_id}", flush=True)

        if tarifario_id:
            inserted = TarifarioDAO.getById(tarifario_id)
            print(f"Tarifario en BD: {inserted}", flush=True)
            return inserted
        return None
    
    @staticmethod
    def patch(tarifario_id, tarifario_args):
        tarifario = TarifarioDAO.getById(tarifario_id)
        if not tarifario:
            return None
            
        query = """
            UPDATE Tarifario 
            SET codigo_postal = %s, tarifa_base = %s, tarifa_kg_adicional = %s, 
                tarifa_volumen_adicional = %s, zona_geografica = %s 
            WHERE id = %s
        """
        params = (tarifario_args["codigo_postal"], tarifario_args["tarifa_base"], 
                 tarifario_args["tarifa_kg_adicional"], tarifario_args["tarifa_volumen_adicional"], 
                 tarifario_args["zona_geografica"], tarifario_id)
        
        result = Database.execute_update(query, params)
        
        if result:
            return TarifarioDAO.getById(tarifario_id)
        return None
    
    @staticmethod
    def delete(tarifario_id):
        tarifario = TarifarioDAO.getById(tarifario_id)
        
        if tarifario:
            query = "DELETE FROM Tarifario WHERE id = %s"
            Database.execute_update(query, (tarifario_id,))
            
        return tarifario
