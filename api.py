import enum
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api,reqparse,fields,marshal_with,abort
from sqlalchemy import Enum, func
from resources.user_resource import User
from resources.users_resource import Users
from models import db
 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

api= Api(app)


api.add_resource(User,'/api/users/<int:id>')

api.add_resource(Users, '/api/users/')    

@app.route('/')
def home():
    return '<h1> Flask REST API</h1>'

if(__name__ == '__main__'):
    app.run(debug=True)