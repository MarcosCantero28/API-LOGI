from flask_restful import Resource, marshal_with, abort
from dao.cotizaciones_dao import  CotizacionDAO
from schemas.cotizacion_schema import cotizacionFields, cotizacion_args


class cotizacion(Resource):
    @marshal_with(cotizacionFields)
    def getById(self, id):
        cotizacion = CotizacionDAO.getById(id)
        if not cotizacion:
            abort(404, "Cotizacion not found")
        return cotizacion
    
    @marshal_with(cotizacionFields)
    def getCotizacionByUsuarioID(self, id_usuario):
        usuarioCotizacion = CotizacionDAO.getCotizacionesByUsuario(id_usuario)
        if not usuarioCotizacion:
            abort(404, "Cotizacion not found")
        return usuarioCotizacion
    

    @marshal_with(cotizacionFields)
    def patch(self, id):
        args = cotizacion_args.parse_args()
        cotizacion = CotizacionDAO.patch(id, args)
        if not cotizacion:
            abort(404, "Cotizacion not found")
        return cotizacion
    
    @marshal_with(cotizacionFields)
    def delete(self, id):
        cotizacion = CotizacionDAO.delete(id)
        if not cotizacion:
            abort(404, "Cotizacion not found")
        return cotizacion



