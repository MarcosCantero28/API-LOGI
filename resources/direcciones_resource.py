from flask_restful import Resource, marshal_with, abort
from dao.direccion_dao import  DireccionDAO
from schemas.direccion_schema import direccionFields,direccion_args

class Direcciones(Resource):
    @marshal_with(direccionFields)
    def get(self):
        direcciones = DireccionDAO.getDirecciones()
        return direcciones
    
    @marshal_with(direccionFields)
    def post(self):
        args = direccion_args.parse_args()
        direccion = DireccionDAO.post(args)
        direcciones = DireccionDAO.getDirecciones()
        return direcciones
    

