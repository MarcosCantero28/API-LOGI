from flask_restful import reqparse, fields

cotizacion_args = reqparse.RequestParser()
cotizacion_args.add_argument('id_usuario', type=int, required=True, help="User ID cannot be blank")
cotizacion_args.add_argument('id_direccion_destino', type=int, required=True, help="Destination address ID cannot be blank")
cotizacion_args.add_argument('id_direccion_origen', type=int, required=True, help="Origin address ID cannot be blank")
cotizacion_args.add_argument('distancia_km', type=int, required=True, help="Distance in km cannot be blank")
cotizacion_args.add_argument('cantidad_items', type=int, required=True, help="Number of items cannot be blank")
cotizacion_args.add_argument('peso_kg', type=float, required=True, help="Weight in kg cannot be blank")
cotizacion_args.add_argument('costo_estimado', type=float, required=True, help="Estimated cost cannot be blank")
cotizacion_args.add_argument('volumen_unidad', type=float, required=True, help="Volume per unit cannot be blank")
cotizacion_args.add_argument('prioridad', type=int, required=True, help="Priority cannot be blank")

cotizacionFields = {
    'id': fields.Integer,
    'id_usuario': fields.Integer,
    'id_direccion_destino': fields.Integer,
    'id_direccion_origen': fields.Integer,
    'distancia_km': fields.Integer,
    'cantidad_items': fields.Integer,
    'peso_kg': fields.Float,
    'costo_estimado': fields.Float,
    'volumen_unidad': fields.Float,
    'prioridad': fields.Integer,
    'fecha_solicitud': fields.String,
    'fecha_actualizacion': fields.String
}
