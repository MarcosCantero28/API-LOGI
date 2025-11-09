from flask_restful import Resource, marshal_with, abort
from dao.user_dao import UserDAO
from schemas.user_schema import userFields, user_args


class User(Resource):
    @marshal_with(userFields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserDAO.patch(id, args)
        if not user:
            abort(404, "User not found")
        return user
    
    @marshal_with(userFields)
    def get(self, id):
        user = UserDAO.getById(id)
        if not user:
            abort(404, "User not found")
        return user
    
    @marshal_with(userFields)
    def delete(self, id):
        user = UserDAO.delete(id)
        if not user:
            abort(404, "User not found")
        return user