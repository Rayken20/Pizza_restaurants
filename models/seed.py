from flask_sqlalchemy import SQLAlchemy
from random import randint, choice as rc
from faker import Faker

from app import app
# from pizza import Pizza
from restaurant import Restaurant, Pizza, RestaurantPizza
from config import db
# from restaurantpizza import RestaurantPizza


fake = Faker()


with app.app_context():

    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    restaurants = []
    for _ in range(20):
        r = Restaurant(
            name=fake.company(),
            location=fake.address()
        )
        restaurants.append(r)

    db.session.add_all(restaurants)
    db.session.commit()

    pizzas = []
    for _ in range(30):
        p = Pizza(
            name=fake.word(),
            toppings=fake.words(5),
            price=randint(5, 30)
        )
        pizzas.append(p)

    db.session.add_all(pizzas)
    db.session.commit()

    restaurant_pizzas = []
    for r in restaurants:
        for _ in range(randint(1, 5)):
            rp = RestaurantPizza(
                restaurant=r,
                pizza=rc(pizzas),
                price=randint(5, 30)
            )
            restaurant_pizzas.append(rp)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()
