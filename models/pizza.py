from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from models import db

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    ingredients = db.Column(db.String)
    price = db.Column(db.Integer) 
    

    restaurantpizzas = db.relationship('RestaurantPizza', backref='pizza', lazy=True)

    def __repr__(self):
        return f'<Pizza {self.name} with ingredients: {self.ingredients},  price: {self.price}>'
