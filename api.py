import enum
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api,reqparse,fields,marshal_with,abort
from sqlalchemy import Enum, func
 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

api= Api(app)

#Modelo de datos
class UserModel(db.Model):
    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=True)
    telefono = db.Column(db.Integer, unique=True, nullable=True)

    cotizaciones = db.relationship('Cotizacion', backref='Usuarios', lazy=True)

    def __repr__(self):
        return f"User(name = {self.nombre}, Email = {self.email}, Phone = {self.telefono}))"
    
class EstadoCotizacion(enum.Enum):
    PENDIENTE='PENDIENTE'
    ACEPTADA='ACEPTADA'
    RECHAZADA='RECHAZADA'

class EstadoEnvio(enum.Enum):
    SOLICITADO='SOLICITADO'
    ASIGNADO='ASIGNADO'
    EN_CAMINO='EN CAMINO'
    ENTREGADO='ENTREGADO'
    CANCELADO='CANCELADO'
    

class Cotizacion(db.Model):

    id= db.Column(db.Integer, primary_key=True)
    origen_Latitud= db.Column(db.Float, nullable=True)
    origen_Longitud = db.Column(db.Float, nullable=True)
    destino_Latitud = db.Column(db.Float, nullable=True)
    destino_Longitud = db.Column(db.Float, nullable=True)
    peso = db.Column(db.Float, nullable=True)
    fechaCreacion = db.Column(db.DateTime,default=func.now(),nullable=True)
    estadoCotizacion = db.Column(Enum(EstadoCotizacion, name = 'cotizacion_estados'),default=EstadoCotizacion.PENDIENTE,nullable=False)

    cliente_id= db.Column(db.Integer, db.ForeignKey('UserModel.id'), nullable=False)


class Envio(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    cliente_id= db.Column(db.Integer, db.ForeignKey('UserModel.id'), nullable=False)
    mensajero_id= db.Column(db.Integer, db.ForeignKey('Mensajero.id'), nullable=False)
    fecha_solicitud = db.Column(db.DateTime, nullable=False)
    fecha_entrega_estimada = db.Column(db.DateTime, nullable=False)
    estadoEnvio=db.Column(Enum(EstadoEnvio, name='envio_estados'),default=EstadoEnvio.SOLICITADO,nullable=True)



class Mensajero(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=True)
    telefono = db.Column(db.Integer, unique=True,nullable=True)
    vehiculo = db.Column(db.String, nullable=True)
    disponible = db.Column(db.Boolean, nullable=True)




#Requerimientos que tiene que cumplir el dato a ingresar
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


cotizacion_args=reqparse.RequestParser()
cotizacion_args.add_argument('origen_Latitud',type=float, required=True, help='Latitude cannot be blank')
cotizacion_args.add_argument('origen_Longitud',type=float, required=True, help='Longitude cannot be blank')
cotizacion_args.add_argument('destino_Latitud',type=float, required=True, help='Latitude cannot be blank')
cotizacion_args.add_argument('destino_Longitud',type=float, required=True, help='Longitude cannot be blank')
cotizacion_args.add_argument('peso', type=int, required=True, help='Weight cannot be blank')


cotizacionFields={
    'id':fields.Integer,
    'origen_Latitud':fields.Float,
    'origen_Longitud':fields.Float,
    'destino_Latitud':fields.Float,
    'destino_Longitud':fields.Float,
    'peso':fields.Integer
}



#Metodos CRUD para varios usuarios

class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args["nombre"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201

#Metodos CRUD para un unico usuario
class User(Resource):
    @marshal_with(userFields)
    def get(self,id):
        user= UserModel.query.filter_by(id=id).first()
        if not user: 
            abort(404, "User not found")
        return user
    @marshal_with(userFields)
    def patch(self,id):
        args = user_args.parse_args()
        user= UserModel.query.filter_by(id=id).first()
        if not user: 
            abort(404, "User not found")
        user.name=args["nombre"]
        user.email=args["email"]
        db.session.commit()
        return user
    
    @marshal_with(userFields)
    def delete(self,id):
        user= UserModel.query.filter_by(id=id).first()
        if not user: 
            abort(404, "User not found")

        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users,201

api.add_resource(User,'/api/users/<int:id>')

api.add_resource(Users, '/api/users/')    

@app.route('/')
def home():
    return '<h1> Flask REST API</h1>'



if(__name__ == '__main__'):
    app.run(debug=True)