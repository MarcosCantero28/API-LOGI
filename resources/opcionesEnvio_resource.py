from flask_restful import Resource, abort, marshal_with
from dao.opcionesEnvio_dao import OpcionesEnvioDAO
from schemas.opcionesEnvio_schema import opcionesEnvio_args, opcionesEnvioFields


class OpcionesEnvio(Resource):
    
    @marshal_with(opcionesEnvioFields)
    def post(self):
        args = opcionesEnvio_args.parse_args()
        
        resultado = OpcionesEnvioDAO.obtenerOpcionesEnvio(
            args['codigo_postal'],
            args['peso_kg'],
            args['volumen_unidad']
        )
        
        if resultado is None:
            abort(404, message="No se pudieron obtener las opciones de envío. Verifique que exista tarifa para el código postal.")
        
        return {
            'codigo_postal': args['codigo_postal'],
            'peso_kg': args['peso_kg'],
            'volumen_unidad': args['volumen_unidad'],
            'costo_base': resultado['costo_base'],
            'opciones_envio': resultado['opciones_envio']
        }
