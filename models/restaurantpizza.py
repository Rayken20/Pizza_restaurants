from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)



# class RestaurantPizza(db.Model, SerializerMixin):
#     __tablename__ = 'restaurantpizzas'

#     serialize_rules = ('-restaurant.restaurantpizzas', '-pizza.restaurantpizzas',)

#     id = db.Column(db.Integer, primary_key=True)
#     price = db.Column(db.Integer)
#     restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
#     pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    
    
#     @validates('price')
#     def validate_price(self, key, price):
#         if not 1 <= price <= 30:
#             raise ValueError("Price must be between 1 and 30")
#         return price

#     restaurant = db.relationship('Restaurant', backref='restaurantpizzas')
#     pizza = db.relationship('Pizza', backref='restaurantpizza')

#     def __repr__(self):
#         return f'<RestaurantPizza for Restaurant ID: {self.restaurant_id}, Pizza ID: {self.pizza_id}>'
