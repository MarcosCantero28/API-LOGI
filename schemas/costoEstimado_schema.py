from flask_restful import reqparse, fields

costoEstimado_args = reqparse.RequestParser()
costoEstimado_args.add_argument('id_direccion_destino', type=int, required=True, help="Destination address ID cannot be blank")
costoEstimado_args.add_argument('peso_kg', type=float, required=True, help="Weight in kg cannot be blank")
costoEstimado_args.add_argument('volumen_unidad', type=float, required=True, help="Volume per unit cannot be blank")
costoEstimado_args.add_argument('id_tipo_envio', type=int, required=True, help="Shipping type ID cannot be blank")

costoEstimadoFields = {
    'id_direccion_destino': fields.Integer,
    'peso_kg': fields.Float,
    'volumen_unidad': fields.Float,
    'id_tipo_envio': fields.Integer,
    'costo_estimado': fields.Float
}
