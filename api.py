from flask import Flask
from flask_restful import Api
from resources.user_resource import User
from resources.users_resource import Users
from resources.cotizaciones_resource import cotizaciones
from resources.cotizacion_resource import cotizacion
from resources.cotizacion_detallada_resource import CotizacionDetallada
from resources.direcciones_resource import Direcciones
from resources.direccion_resource import Direccion
from resources.warehouses_resource import Warehouses
from resources.warehouse_resource import warehouse
from resources.tarifarios_resource import Tarifarios
from resources.tarifario_resource import Tarifario
from resources.costoEstimado_resource import CostoEstimado
from resources.opcionesEnvio_resource import OpcionesEnvio
from resources.envios_resource import Envios
from resources.envio_resource import Envio


import sys

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

api= Api(app)


api.add_resource(User,'/api/users/<int:id>')
api.add_resource(Users, '/api/users/')   

api.add_resource(cotizaciones, '/api/cotizaciones/')
api.add_resource(cotizacion, '/api/cotizaciones/<int:id>')

api.add_resource(CotizacionDetallada, '/api/cotizaciones/<int:id>/detallada')

api.add_resource(Direcciones, '/api/direcciones/')
api.add_resource(Direccion, '/api/direcciones/<int:id>')

api.add_resource(Warehouses, '/api/warehouses/')
api.add_resource(warehouse, '/api/warehouses/<int:id>')

api.add_resource(Tarifarios, '/api/tarifarios/')
api.add_resource(Tarifario, '/api/tarifarios/<int:id>')

api.add_resource(CostoEstimado, '/api/calcularCostoEstimado/')
api.add_resource(OpcionesEnvio, '/api/opcionesEnvio/')

api.add_resource(Envios, '/api/envios/')
api.add_resource(Envio, '/api/envios/<int:id>')

@app.route('/')
def home():
    return '<h1>Flask REST API con MySQL</h1>'

#if(__name__ == '__main__'):
#    app.run(debug=True)