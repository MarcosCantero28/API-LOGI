from flask_restful import reqparse, fields

# Request parser para opciones de envío
opcionesEnvio_args = reqparse.RequestParser()
opcionesEnvio_args.add_argument('codigo_postal', type=str, required=True, help="Postal code cannot be blank")
opcionesEnvio_args.add_argument('peso_kg', type=float, required=True, help="Weight in kg cannot be blank")
opcionesEnvio_args.add_argument('volumen_unidad', type=float, required=True, help="Volume per unit cannot be blank")

# Campos para cada opción de envío
opcionEnvioFields = {
    'id_tipo_envio': fields.Integer,
    'nombre': fields.String,
    'descripcion': fields.String,
    'costo_final': fields.Float
}

# Campos de la respuesta completa
opcionesEnvioFields = {
    'codigo_postal': fields.String,
    'peso_kg': fields.Float,
    'volumen_unidad': fields.Float,
    'costo_base': fields.Float,
    'opciones_envio': fields.List(fields.Nested(opcionEnvioFields))
}
