from flask_restful import reqparse, fields

warehouse_args = reqparse.RequestParser()
warehouse_args.add_argument('id_direccion', type=int, required=True, help="Address ID cannot be blank")

warehouseFields = {
    'id': fields.Integer,
    'id_direccion': fields.Integer
}
