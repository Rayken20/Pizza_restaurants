from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


# class Pizza(db.Model, SerializerMixin):
#     __tablename__ = 'pizzas'

#     serialize_rules = ('-restaurants.pizzas',)

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, unique=True)
#     toppings = db.Column(db.String)
#     price = db.Column(db.Integer)

#     restaurants = db.relationship('RestaurantPizza', backref='pizza', lazy=True)

#     def __repr__(self):
#         return f'<Pizza {self.name} with toppings: {self.toppings}>'
