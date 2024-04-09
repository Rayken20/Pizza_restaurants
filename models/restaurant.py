from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from models import db

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    address = db.Column(db.String(100))  
    
    @validates('name')
    def validate_name(self, key, name):
        if not name.strip():
            raise ValueError("Restaurant name cannot be empty")
        return name
    
    restaurantpizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)

    def __repr__(self):
        return f'<Restaurant {self.name} at {self.address}>'
