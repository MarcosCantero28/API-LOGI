from flask_restful import reqparse, fields

direccion_args = reqparse.RequestParser()
direccion_args.add_argument('calle', type=str, required=True, help="Street cannot be blank")
direccion_args.add_argument('numero_calle', type=int, required=True, help="Street number cannot be blank")
direccion_args.add_argument('pais', type=str, required=True, help="Country cannot be blank")
direccion_args.add_argument('ciudad', type=str, required=True, help="City cannot be blank")
direccion_args.add_argument('codigo_postal', type=str, required=False)
direccion_args.add_argument('latitud', type=float, required=False)
direccion_args.add_argument('longitud', type=float, required=False)

direccionFields = {
    'id': fields.Integer,
    'calle': fields.String,
    'numero_calle': fields.Integer,
    'pais': fields.String,
    'ciudad': fields.String,
    'codigo_postal': fields.String,
    'latitud': fields.Float,
    'longitud': fields.Float
}
