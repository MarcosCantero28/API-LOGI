from flask_restful import Resource, abort, marshal_with
from dao.envio_dao import EnvioDAO
from schemas.envio_schema import envio_put_args, envioFields


class Envio(Resource):
    
    @marshal_with(envioFields)
    def get(self, id):
        """
        Obtiene un envío por ID
        """
        envio = EnvioDAO.get_by_id(id)
        if not envio:
            abort(404, message=f"Envío con ID {id} no encontrado")
        return envio
    
    @marshal_with(envioFields)
    def put(self, id):
        """
        Actualiza el estado de un envío
        """
        args = envio_put_args.parse_args()
        
        # Verificar que el envío existe
        envio = EnvioDAO.get_by_id(id)
        if not envio:
            abort(404, message=f"Envío con ID {id} no encontrado")
        
        # Actualizar el estado
        success = EnvioDAO.put(id, args)
        
        if success:
            return EnvioDAO.get_by_id(id)
        else:
            abort(400, message="Error al actualizar el envío")
    
    def delete(self, id):
        """
        Elimina un envío
        """
        # Verificar que el envío existe
        envio = EnvioDAO.get_by_id(id)
        if not envio:
            abort(404, message=f"Envío con ID {id} no encontrado")
        
        success = EnvioDAO.delete(id)
        
        if success:
            return {'message': f'Envío {id} eliminado exitosamente'}, 200
        else:
            abort(400, message="Error al eliminar el envío")
