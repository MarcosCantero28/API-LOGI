from flask_restful import Resource, marshal_with, abort
from dao.tarifario_dao import TarifarioDAO
from schemas.tarifario_schema import tarifarioFields, tarifario_args

class Tarifarios(Resource):
    @marshal_with(tarifarioFields)
    def get(self):
        tarifarios = TarifarioDAO.getTarifarios()
        return tarifarios
    
    @marshal_with(tarifarioFields)
    def post(self):
        args = tarifario_args.parse_args()
        tarifario = TarifarioDAO.post(args)
        tarifarios = TarifarioDAO.getTarifarios()
        return tarifarios
