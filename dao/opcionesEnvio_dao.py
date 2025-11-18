from config.db_config import Database


class OpcionesEnvioDAO:

    @staticmethod
    def obtenerOpcionesEnvio(codigo_postal, peso_kg, volumen_unidad):
        # Consultar tarifario directamente con el código postal
        query_tarifario = """
            SELECT tarifa_base, tarifa_kg_adicional, tarifa_volumen_adicional 
            FROM Tarifario 
            WHERE codigo_postal = %s
        """
        tarifario = Database.execute_query(query_tarifario, (codigo_postal,))
        
        if not tarifario:
            print(f"Error: No existe tarifa para el codigo postal {codigo_postal}", flush=True)
            return None

        tarifa = tarifario[0]
        tarifa_base = tarifa['tarifa_base']
        tarifa_kg_adicional = tarifa['tarifa_kg_adicional']
        tarifa_volumen_adicional = tarifa.get('tarifa_volumen_adicional', 0) or 0

        costo_base = (
            tarifa_base + 
            (peso_kg * tarifa_kg_adicional) +
            (volumen_unidad * tarifa_volumen_adicional)
        )
        
        query_tipos_envio = "SELECT id, nombre, coeficiente, descripcion FROM TipoEnvio ORDER BY coeficiente ASC"
        tipos_envio = Database.execute_query(query_tipos_envio)
        
        if not tipos_envio:
            print("Error: No hay tipos de envío registrados en la base de datos", flush=True)
            return None
        
        opciones_envio = []
        for tipo in tipos_envio:
            costo_final = costo_base * tipo['coeficiente']
            opciones_envio.append({
                'id_tipo_envio': tipo['id'],
                'nombre': tipo['nombre'],
                'descripcion': tipo['descripcion'],
                'costo_final': round(costo_final, 2)
            })
        
        return {
            'costo_base': round(costo_base, 2),
            'opciones_envio': opciones_envio
        }
