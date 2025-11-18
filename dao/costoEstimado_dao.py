from config.db_config import Database


class CostoEstimadoDAO:

    @staticmethod
    def calcularCostoEstimado(id_direccion_destino, peso_kg, volumen_unidad, id_tipo_envio):
        
        # Paso 1: Consultar dirección y código postal
        query_destino = "SELECT id, codigo_postal FROM Direccion WHERE id = %s"
        direccion = Database.execute_query(query_destino, (id_direccion_destino,))
        
        if not direccion:
            print(f"Error: Direccion {id_direccion_destino} no existe", flush=True)
            return None
        
        codigo_postal = direccion[0].get('codigo_postal')
        if not codigo_postal:
            print(f"Error: La direccion {id_direccion_destino} no tiene codigo postal", flush=True)
            return None
        
        # Paso 2: Consultar tarifario
        query_tarifario = """
            SELECT tarifa_base, tarifa_kg_adicional, tarifa_volumen_adicional 
            FROM Tarifario 
            WHERE codigo_postal = %s
        """
        tarifario = Database.execute_query(query_tarifario, (codigo_postal,))
        
        if not tarifario:
            print(f"Error: No existe tarifa para el codigo postal {codigo_postal}", flush=True)
            return None
        
        # Paso 3: Consultar tipo de envío y su coeficiente
        query_tipo_envio = "SELECT id, nombre, coeficiente FROM TipoEnvio WHERE id = %s"
        tipo_envio = Database.execute_query(query_tipo_envio, (id_tipo_envio,))
        
        if not tipo_envio:
            print(f"Error: Tipo de envio {id_tipo_envio} no existe", flush=True)
            return None
        
        coeficiente = tipo_envio[0]['coeficiente']
        nombre_tipo_envio = tipo_envio[0]['nombre']

        # Paso 4: Calcular costo base
        tarifa = tarifario[0]
        tarifa_base = tarifa['tarifa_base']
        tarifa_kg_adicional = tarifa['tarifa_kg_adicional']
        tarifa_volumen_adicional = tarifa.get('tarifa_volumen_adicional', 0) or 0

        costo_base = (
            tarifa_base + 
            (peso_kg * tarifa_kg_adicional) +
            (volumen_unidad * tarifa_volumen_adicional)
        )
        
        # Paso 5: Aplicar coeficiente del tipo de envío
        costo_estimado = costo_base * coeficiente
        
        print(f"Costo calculado: {costo_estimado:.2f} (Base: {costo_base:.2f}, Tipo: {nombre_tipo_envio}, Coeficiente: {coeficiente})", flush=True)
        
        return costo_estimado
        

