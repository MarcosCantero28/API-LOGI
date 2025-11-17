from flask_restful import Resource, marshal_with, abort
from dao.warehouse_dao import  warehouseDAO
from schemas.warehouse_schema import warehouseFields, warehouse_args


class Warehouses(Resource):

    @marshal_with(warehouseFields)
    def get(self):
        warehouses = warehouseDAO.get()
        return warehouses
    
    @marshal_with(warehouseFields)
    def post(self):
        args = warehouse_args.parse_args()
        warehouse = warehouseDAO.post(args)
        warehouses = warehouseDAO.get()

        return warehouses
    

