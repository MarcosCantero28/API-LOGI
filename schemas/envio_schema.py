from flask_restful import reqparse, fields

# Request parser para crear envío
envio_post_args = reqparse.RequestParser()
envio_post_args.add_argument('codigo_postal', type=str, required=True, help="Postal code cannot be blank")
envio_post_args.add_argument('id_tipo_envio', type=int, required=True, help="Shipping type ID cannot be blank")
envio_post_args.add_argument('direccion_destino', type=str, required=True, help="Destination address cannot be blank")
envio_post_args.add_argument('localidad', type=str, required=True, help="Locality cannot be blank")
envio_post_args.add_argument('provincia', type=str, required=True, help="Province cannot be blank")
envio_post_args.add_argument('peso_kg', type=float, required=True, help="Weight in kg cannot be blank")
envio_post_args.add_argument('volumen_unidad', type=float, required=True, help="Volume per unit cannot be blank")
envio_post_args.add_argument('nombre_receptor', type=str, required=True, help="Receiver name cannot be blank")
envio_post_args.add_argument('dni_receptor', type=str, required=True, help="Receiver DNI cannot be blank")
envio_post_args.add_argument('id_estado_envio', type=int, required=False)  # Opcional, por defecto será 1 (Pendiente)

# Request parser para actualizar envío
envio_put_args = reqparse.RequestParser()
envio_put_args.add_argument('direccion_destino', type=str, required=False)
envio_put_args.add_argument('localidad', type=str, required=False)
envio_put_args.add_argument('provincia', type=str, required=False)
envio_put_args.add_argument('pais', type=str, required=False)
envio_put_args.add_argument('nombre_receptor', type=str, required=False)
envio_put_args.add_argument('dni_receptor', type=str, required=False)
envio_put_args.add_argument('id_estado_envio', type=int, required=False)

# Campos de respuesta para un envío
envioFields = {
    'id': fields.Integer,
    'codigo_postal': fields.String,
    'tipo_envio_nombre': fields.String,
    'tipo_envio_descripcion': fields.String,
    'direccion_destino': fields.String,
    'localidad': fields.String,
    'provincia': fields.String,
    'peso_kg': fields.Float,
    'volumen_unidad': fields.Float,
    'estado_nombre': fields.String,
    'nombre_receptor': fields.String,
    'dni_receptor': fields.String,
    'costo_total': fields.Float,
    'fecha_creacion': fields.DateTime(dt_format='iso8601'),
    'fecha_actualizacion': fields.DateTime(dt_format='iso8601')
}

# Campos de respuesta simplificada (solo ID al crear)
envioCreateFields = {
    'id': fields.Integer,
    'message': fields.String
}
