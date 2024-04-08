from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    location = db.Column(db.String(100))  
    
    @validates('name')
    def validate_name(self, key, name):
        if not name.strip():
            raise ValueError("Restaurant name cannot be empty")
        return name
    
    restaurantpizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)

    def __repr__(self):
        return f'<Restaurant {self.name} at {self.location}>'
    
class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantpizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    
    @validates('price')
    def validate_price(self, key, price):
        if not 1 <= price <= 30:
            raise ValueError("Price must be between 1 and 30")
        return price

    restaurant = db.relationship('Restaurant', backref='restaurantpizzas')
    pizza = db.relationship('Pizza', backref='restaurantpizza')

    def __repr__(self):
        return f'<RestaurantPizza for Restaurant ID: {self.restaurant_id}, Pizza ID: {self.pizza_id}>'


class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    toppings = db.Column(db.String)
    price = db.Column(db.Integer)

    restaurantpizzas = db.relationship('RestaurantPizza', backref='pizza', lazy=True)

    def __repr__(self):
        return f'<Pizza {self.name} with toppings: {self.toppings}>'
