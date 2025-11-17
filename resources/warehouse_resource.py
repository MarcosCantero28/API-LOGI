from flask_restful import Resource, marshal_with, abort
from dao.warehouse_dao import  warehouseDAO
from schemas.warehouse_schema import warehouseFields, warehouse_args


class warehouse(Resource):


    @marshal_with(warehouseFields)
    def getById(self, id):
        warehouse = warehouseDAO.getById(id)
        if not warehouse:
            abort(404, "Warehouse not found")
        return warehouse

    @marshal_with(warehouseFields)
    def patch(self,id):
        args = warehouse_args.parse_args()
        warehouse = warehouseDAO.patch(id,args)
        if not warehouse:
            abort(404, "Warehouse not found")
        return warehouse
    @marshal_with(warehouseFields)
    def delete(self,id):
        warehouse = warehouseDAO.delete(id)
        if not warehouse:
            abort(404,"Warehouse not found")
        return warehouse

