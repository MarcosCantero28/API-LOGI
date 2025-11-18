from flask_restful import Resource, marshal_with
from dao.envio_dao import EnvioDAO
from schemas.envio_schema import envio_post_args, envioFields, envioCreateFields


class Envios(Resource):
    
    @marshal_with(envioFields)
    def get(self):
        """
        Obtiene todos los envíos
        """
        return EnvioDAO.get()
    
    @marshal_with(envioCreateFields)
    def post(self):
        """
        Crea un nuevo envío
        """
        args = envio_post_args.parse_args()
        
        envio_id = EnvioDAO.post(args)
        
        if envio_id:
            return {
                'id': envio_id,
                'message': 'Envío creado exitosamente'
            }, 201
        else:
            return {
                'id': None,
                'message': 'Error al crear el envío'
            }, 400
