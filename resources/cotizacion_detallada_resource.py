from flask_restful import Resource, abort
from dao.cotizaciones_dao import CotizacionDAO

class CotizacionDetallada(Resource):
    def get(self, id):
        cotizacion = CotizacionDAO.getCotizacionDetallada(id)
        if not cotizacion:
            abort(404, message="Cotizacion not found")
        return cotizacion, 200
