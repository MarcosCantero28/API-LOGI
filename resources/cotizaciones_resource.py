from flask_restful import Resource, marshal_with, abort
from dao.cotizaciones_dao import  CotizacionDAO
from schemas.cotizacion_schema import cotizacionFields, cotizacion_args


class cotizaciones(Resource):
    @marshal_with(cotizacionFields)
    def get(self):
        cotizaciones = CotizacionDAO.getCotizaciones()
        return cotizaciones
    @marshal_with(cotizacionFields)
    def post(self):
        args =  cotizacion_args.parse_args()
        cotizacion = CotizacionDAO.post(args)
        cotizaciones = CotizacionDAO.getCotizaciones()
        return cotizaciones
    
    
