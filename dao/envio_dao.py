from config.db_config import Database
from dao.opcionesEnvio_dao import OpcionesEnvioDAO


class EnvioDAO:

    @staticmethod
    def post(envio):
        """
        Crea un nuevo envío en la base de datos
        Calcula automáticamente el costo_total usando OpcionesEnvioDAO
        """
        # Paso 1: Calcular el costo total usando OpcionesEnvioDAO
        resultado_costo = OpcionesEnvioDAO.obtenerOpcionesEnvio(
            envio['codigo_postal'],
            envio['peso_kg'],
            envio['volumen_unidad']
        )
        
        if not resultado_costo:
            print(f"Error: No se pudo calcular el costo para el código postal {envio['codigo_postal']}", flush=True)
            return None
        
        # Buscar el costo_final para el tipo de envío seleccionado
        costo_total = None
        for opcion in resultado_costo['opciones_envio']:
            if opcion['id_tipo_envio'] == envio['id_tipo_envio']:
                costo_total = opcion['costo_final']
                break
        
        if costo_total is None:
            print(f"Error: Tipo de envío {envio['id_tipo_envio']} no encontrado", flush=True)
            return None
        
        
        id_estado_envio = envio.get('id_estado_envio')
        if id_estado_envio is None:
            id_estado_envio = 1  

        pais = envio.get('pais')
        if pais is None:
            pais = "Argentina" 
        
        query_estado = "SELECT nombre FROM EstadoEnvio WHERE id = %s"
        estado = Database.execute_query(query_estado, (id_estado_envio,))
        
        if not estado:
            print(f"Error: Estado de envío {id_estado_envio} no existe", flush=True)
            return None
        
    
        query_insert = """
            INSERT INTO Envio (
                codigo_postal, 
                id_tipo_envio, 
                direccion_destino,
                localidad,
                provincia,
                pais,
                peso_kg, 
                volumen_unidad, 
                id_estado_envio,
                nombre_receptor, 
                dni_receptor, 
                costo_total
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        pais = envio.get('pais', 'Argentina')  # Por defecto Argentina
        
        params = (
            envio['codigo_postal'],
            envio['id_tipo_envio'],
            envio['direccion_destino'],
            envio['localidad'],
            envio['provincia'],
            pais,
            envio['peso_kg'],
            envio['volumen_unidad'],
            id_estado_envio,
            envio['nombre_receptor'],
            envio['dni_receptor'],
            costo_total
        )
        
        result = Database.execute_update(query_insert, params)
        
        if result:
            print(f"Envío creado exitosamente con ID: {result}, Costo total: {costo_total}", flush=True)
            return result
        else:
            print("Error al crear el envío", flush=True)
            return None
    
    @staticmethod
    def get():
        """
        Obtiene todos los envíos con información completa
        """
        query = """
            SELECT 
                e.id,
                e.codigo_postal,
                e.id_tipo_envio,
                te.nombre AS tipo_envio_nombre,
                te.descripcion AS tipo_envio_descripcion,
                e.direccion_destino,
                e.localidad,
                e.provincia,
                e.pais,
                e.peso_kg,
                e.volumen_unidad,
                e.id_estado_envio,
                ee.nombre AS estado_nombre,
                e.nombre_receptor,
                e.dni_receptor,
                e.costo_total,
                e.fecha_creacion,
                e.fecha_actualizacion
            FROM Envio e
            INNER JOIN TipoEnvio te ON e.id_tipo_envio = te.id
            INNER JOIN EstadoEnvio ee ON e.id_estado_envio = ee.id
            ORDER BY e.fecha_creacion DESC
        """
        return Database.execute_query(query)
    
    @staticmethod
    def get_by_id(id_envio):
        """
        Obtiene un envío específico por su ID
        """
        query = """
            SELECT 
                e.id,
                e.codigo_postal,
                e.id_tipo_envio,
                te.nombre AS tipo_envio_nombre,
                te.descripcion AS tipo_envio_descripcion,
                e.direccion_destino,
                e.localidad,
                e.provincia,
                e.pais,
                e.peso_kg,
                e.volumen_unidad,
                e.id_estado_envio,
                ee.nombre AS estado_nombre,
                e.nombre_receptor,
                e.dni_receptor,
                e.costo_total,
                e.fecha_creacion,
                e.fecha_actualizacion
            FROM Envio e
            INNER JOIN TipoEnvio te ON e.id_tipo_envio = te.id
            INNER JOIN EstadoEnvio ee ON e.id_estado_envio = ee.id
            WHERE e.id = %s
        """
        result = Database.execute_query(query, (id_envio,))
        return result[0] if result else None
    
    @staticmethod
    def put(id_envio, envio):
        """
        Actualiza un envío existente (dirección, receptor, estado, etc)
        """
        # Construir dinámicamente la consulta UPDATE según los campos proporcionados
        campos_actualizar = []
        valores = []
        
        if 'direccion_destino' in envio and envio['direccion_destino'] is not None:
            campos_actualizar.append("direccion_destino = %s")
            valores.append(envio['direccion_destino'])
        
        if 'localidad' in envio and envio['localidad'] is not None:
            campos_actualizar.append("localidad = %s")
            valores.append(envio['localidad'])
        
        if 'provincia' in envio and envio['provincia'] is not None:
            campos_actualizar.append("provincia = %s")
            valores.append(envio['provincia'])
        
        if 'pais' in envio and envio['pais'] is not None:
            campos_actualizar.append("pais = %s")
            valores.append(envio['pais'])
        
        if 'nombre_receptor' in envio and envio['nombre_receptor'] is not None:
            campos_actualizar.append("nombre_receptor = %s")
            valores.append(envio['nombre_receptor'])
        
        if 'dni_receptor' in envio and envio['dni_receptor'] is not None:
            campos_actualizar.append("dni_receptor = %s")
            valores.append(envio['dni_receptor'])
        
        if 'id_estado_envio' in envio and envio['id_estado_envio'] is not None:
            campos_actualizar.append("id_estado_envio = %s")
            valores.append(envio['id_estado_envio'])
        
        if not campos_actualizar:
            print(f"Error: No hay campos para actualizar en el envío {id_envio}", flush=True)
            return False
        
        valores.append(id_envio)
        
        query = f"""
            UPDATE Envio 
            SET {', '.join(campos_actualizar)}
            WHERE id = %s
        """
        
        result = Database.execute_update(query, tuple(valores))
        
        if result:
            print(f"Envío {id_envio} actualizado exitosamente", flush=True)
            return True
        else:
            print(f"Error al actualizar el envío {id_envio}", flush=True)
            return False
    
    @staticmethod
    def delete(id_envio):
        """
        Elimina un envío por su ID
        """
        query = "DELETE FROM Envio WHERE id = %s"
        result = Database.execute_update(query, (id_envio,))
        
        if result:
            print(f"Envío {id_envio} eliminado exitosamente", flush=True)
            return True
        else:
            print(f"Error al eliminar el envío {id_envio}", flush=True)
            return False

