from flask_restful import Resource, marshal_with, abort
from dao.user_dao import UserDAO
from schemas.user_schema import userFields, user_args

#Metodos CRUD para varios usuarios

class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserDAO.getUsers()
        return users

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserDAO.post(args)
        users = UserDAO.getUsers()
        return users, 201