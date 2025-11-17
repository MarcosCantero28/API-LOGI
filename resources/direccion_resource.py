from flask_restful import Resource, marshal_with, abort
from dao.direccion_dao import  DireccionDAO
from schemas.direccion_schema import direccionFields,direccion_args


class Direccion(Resource):


    @marshal_with(direccionFields)
    def getDireccionById(self, id):
        direccion = DireccionDAO.getDireccionById(id)
        if not direccion:
            abort(404, "Direccion not found")
        return direccion

    @marshal_with(direccionFields)
    def patch(self, id):
        args = direccion_args.parse_args()
        direccion = DireccionDAO.patch(id, args)
        if not direccion:
            abort(404, "Direccion not found")

    def delete(self,id):
        args = direccion_args.parse_args()

        direccion = DireccionDAO.delete(id,args)
        if not direccion:
            abort(404, "Direccion not found")