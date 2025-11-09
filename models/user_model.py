from flask_sqlalchemy import SQLAlchemy
from models import db

class UserModel(db.Model):
    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=True)
    telefono = db.Column(db.Integer, unique=True, nullable=True)
    def __repr__(self):
        return f"User(name = {self.nombre}, Email = {self.email}, Phone = {self.telefono}))"