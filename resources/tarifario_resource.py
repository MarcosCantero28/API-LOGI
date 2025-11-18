from flask_restful import Resource, marshal_with, abort
from dao.tarifario_dao import TarifarioDAO
from schemas.tarifario_schema import tarifarioFields, tarifario_args


class Tarifario(Resource):

    @marshal_with(tarifarioFields)
    def get(self, id):
        tarifario = TarifarioDAO.getById(id)
        if not tarifario:
            abort(404, "Tarifario not found")
        return tarifario

    @marshal_with(tarifarioFields)
    def patch(self, id):
        args = tarifario_args.parse_args()
        tarifario = TarifarioDAO.patch(id, args)
        if not tarifario:
            abort(404, "Tarifario not found")
        return tarifario

    @marshal_with(tarifarioFields)
    def delete(self, id):
        tarifario = TarifarioDAO.delete(id)
        if not tarifario:
            abort(404, "Tarifario not found")
        return tarifario
