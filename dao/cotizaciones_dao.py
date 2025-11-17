from config.db_config import Database



class CotizacionDAO:

    @staticmethod
    def getCotizaciones():
        query = """SELECT id, id_usuario, id_direccion_destino, id_direccion_origen, 
                   distancia_km, cantidad_items, peso_kg, costo_estimado, 
                   volumen_unidad, prioridad, fecha_solicitud, fecha_actualizacion 
                   FROM Cotizaciones ORDER BY id"""
        results = Database.execute_query(query)
        return results if results else []
    
    @staticmethod
    def getCotizacionesByUsuario(id_usuario):
        query = """SELECT id, id_usuario, id_direccion_destino, id_direccion_origen, 
                   distancia_km, cantidad_items, peso_kg, costo_estimado, 
                   volumen_unidad, prioridad, fecha_solicitud, fecha_actualizacion 
                   FROM Cotizaciones WHERE id_usuario = %s ORDER BY id"""
        results = Database.execute_query(query, (id_usuario,))
        return results if results else []
    
    @staticmethod
    def post(cotizacion):
        print(f"Creando cotizacion para usuario: {cotizacion['id_usuario']}", flush=True)
        
        verify_usuario = Database.execute_query("SELECT id FROM Usuarios WHERE id = %s", (cotizacion["id_usuario"],))
        if not verify_usuario:
            print(f"Error: Usuario {cotizacion['id_usuario']} no existe", flush=True)
            return None
            
        verify_destino = Database.execute_query("SELECT id FROM Direccion WHERE id = %s", (cotizacion["id_direccion_destino"],))
        if not verify_destino:
            print(f"Error: Direccion destino {cotizacion['id_direccion_destino']} no existe", flush=True)
            return None
            
        verify_origen = Database.execute_query("SELECT id FROM Warehouse WHERE id = %s", (cotizacion["id_direccion_origen"],))
        if not verify_origen:
            print(f"Error: Warehouse origen {cotizacion['id_direccion_origen']} no existe", flush=True)
            return None
        
        query = """
            INSERT INTO Cotizaciones (id_usuario, id_direccion_destino, id_direccion_origen, 
                                     distancia_km, cantidad_items, peso_kg, costo_estimado, 
                                     volumen_unidad, prioridad) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (cotizacion["id_usuario"], cotizacion["id_direccion_destino"], 
                 cotizacion["id_direccion_origen"], cotizacion["distancia_km"], 
                 cotizacion["cantidad_items"], cotizacion["peso_kg"], 
                 cotizacion["costo_estimado"], cotizacion["volumen_unidad"], 
                 cotizacion["prioridad"])
        cotizacion_id = Database.execute_update(query, params)
        
        if cotizacion_id:
            print(f"Cotizacion creada con ID: {cotizacion_id}", flush=True)
            return CotizacionDAO.getById(cotizacion_id)
        return None

    @staticmethod
    def getById(id):
        query = """SELECT id, id_usuario, id_direccion_destino, id_direccion_origen, 
                   distancia_km, cantidad_items, peso_kg, costo_estimado, 
                   volumen_unidad, prioridad, fecha_solicitud, fecha_actualizacion 
                   FROM Cotizaciones WHERE id = %s"""
        results = Database.execute_query(query, (id,))
        return results[0] if results else None
    
    @staticmethod
    def patch(cotizacion_id, cotizacion_args):
        cotizacion = CotizacionDAO.getById(cotizacion_id)
        if not cotizacion:
            return None
            
        query = """
            UPDATE Cotizaciones 
            SET id_usuario = %s, id_direccion_destino = %s, id_direccion_origen = %s, 
                distancia_km = %s, cantidad_items = %s, peso_kg = %s, 
                costo_estimado = %s, volumen_unidad = %s, prioridad = %s 
            WHERE id = %s
        """
        params = (cotizacion_args["id_usuario"], cotizacion_args["id_direccion_destino"], 
                 cotizacion_args["id_direccion_origen"], cotizacion_args["distancia_km"], 
                 cotizacion_args["cantidad_items"], cotizacion_args["peso_kg"], 
                 cotizacion_args["costo_estimado"], cotizacion_args["volumen_unidad"], 
                 cotizacion_args["prioridad"], cotizacion_id)
        
        result = Database.execute_update(query, params)
        
        if result:
            return CotizacionDAO.getById(cotizacion_id)
        return None
    
    @staticmethod
    def delete(cotizacion_id):
        cotizacion = CotizacionDAO.getById(cotizacion_id)
        
        if cotizacion:
            query = "DELETE FROM Cotizaciones WHERE id = %s"
            Database.execute_update(query, (cotizacion_id,))
            
        return cotizacion
    
    @staticmethod
    def getCotizacionDetallada(cotizacion_id):
        result = Database.call_procedure('obtenerCotizacionDetallada', (cotizacion_id,))
        return result[0] if result else None