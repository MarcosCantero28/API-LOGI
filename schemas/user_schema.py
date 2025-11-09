from flask_restful import reqparse, fields

user_args = reqparse.RequestParser()
user_args.add_argument('nombre',type=str, required=True,help="Name cannot be blank")
user_args.add_argument('email',type=str, required=True,help="Email cannot be blank")
user_args.add_argument('telefono',type=int, required=True,help="phone cannot be blank")

userFields = {
    'id':fields.Integer,
    'nombre':fields.String,
    'email':fields.String,
    'telefono':fields.Integer
}
