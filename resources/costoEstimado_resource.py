from flask_restful import Resource, abort, marshal_with
from dao.costoEstimado_dao import CostoEstimadoDAO
from schemas.costoEstimado_schema import costoEstimadoFields, costoEstimado_args


class CostoEstimado(Resource):

    @marshal_with(costoEstimadoFields)
    def post(self):
        args = costoEstimado_args.parse_args()
        
        costo = CostoEstimadoDAO.calcularCostoEstimado(
            args['id_direccion_destino'],
            args['peso_kg'],
            args['volumen_unidad'],
            args['id_tipo_envio']
        )
        
        if costo is None:
            abort(404, message="No se pudo calcular el costo. Verifique que la dirección tenga código postal, exista tarifa y el tipo de envío sea válido.")
        
        return {
            'id_direccion_destino': args['id_direccion_destino'],
            'peso_kg': args['peso_kg'],
            'volumen_unidad': args['volumen_unidad'],
            'id_tipo_envio': args['id_tipo_envio'],
            'costo_estimado': costo
        }



