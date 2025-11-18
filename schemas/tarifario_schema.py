from flask_restful import reqparse, fields

tarifario_args = reqparse.RequestParser()
tarifario_args.add_argument('codigo_postal', type=str, required=True, help="Postal code cannot be blank")
tarifario_args.add_argument('tarifa_base', type=float, required=True, help="Base rate cannot be blank")
tarifario_args.add_argument('tarifa_kg_adicional', type=float, required=True, help="Additional kg rate cannot be blank")
tarifario_args.add_argument('tarifa_volumen_adicional', type=float, required=False)
tarifario_args.add_argument('zona_geografica', type=str, required=False)

tarifarioFields = {
    'id': fields.Integer,
    'codigo_postal': fields.String,
    'tarifa_base': fields.Float,
    'tarifa_kg_adicional': fields.Float,
    'tarifa_volumen_adicional': fields.Float,
    'zona_geografica': fields.String
}
