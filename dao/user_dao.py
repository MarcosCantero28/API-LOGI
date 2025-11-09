from models.user_model import UserModel
from models import db

class UserDAO:

    @staticmethod
    def getUsers():
        return UserModel.query.all()
    
    @staticmethod
    def post(user):
        user = UserModel(nombre=user["nombre"], email=user["email"], telefono = user["telefono"])
        db.session.add(user)
        db.session.commit()
        return user
    

    #Metodos para un solo usuario
    @staticmethod
    def getById(id):
        return UserModel.query.filter_by(id=id).first()
    
    @staticmethod
    def patch(user_id, user_args):
        user= UserModel.query.filter_by(id=user_id).first()
        if user:
            user.nombre = user_args["nombre"]
            user.email = user_args["email"]
            user.telefono = user_args["telefono"]
            db.session.commit()
        return user
    
    @staticmethod
    def delete(user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
        return user