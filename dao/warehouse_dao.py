

from config.db_config import Database


class warehouseDAO:

    @staticmethod
    def get():
        query = 'SELECT id,id_direccion FROM Warehouse'
        results= Database.execute_query(query)

        return results if results else []
    
    @staticmethod
    def getById(id):
        query = 'SELECT id,id_direccion FROM Warehouse WHERE id = %s'
        results = Database.execute_query(query, (id,))
        return results[0] if results else None
    
    @staticmethod
    def post(warehouse):
        query = 'INSERT INTO Warehouse(id_direccion) VALUES(%s)'
        params = (warehouse["id_direccion"],)
        warehouse_id = Database.execute_update(query, params)

        if warehouse_id:
            return warehouseDAO.getById(warehouse_id)
        return None
    
    @staticmethod
    def patch(warehouse_id, warehouse_args):
        warehouse = warehouseDAO.getById(warehouse_id)

        if not warehouse:
            return None
        
        query = """
            UPDATE Warehouse 
            SET id_direccion = %s 
            WHERE id = %s
        """
        params = (warehouse_args["id_direccion"], warehouse_id)

        result = Database.execute_update(query, params)

        if result:
            return warehouseDAO.getById(warehouse_id)
        return None
    
    @staticmethod
    def delete(warehouse_id):
        warehouse = warehouseDAO.getById(warehouse_id)
        
        if warehouse:
            query = "DELETE FROM Warehouse WHERE id = %s"
            Database.execute_update(query, (warehouse_id,))
            
        return warehouse



