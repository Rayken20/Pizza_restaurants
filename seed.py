from faker import Faker
from random import randint, choice
from app import create_app
from models import db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurantpizza import RestaurantPizza

fake = Faker()

# Create Flask app
app = create_app()

with app.app_context():
    # Delete existing data
    db.drop_all()
    db.create_all()

    # Set to keep track of used restaurant names
    used_restaurant_names = set()

    # Seed Restaurants
    for _ in range(20):
        restaurant_name = fake.company()
        # Ensure unique restaurant name
        while restaurant_name in used_restaurant_names:
            restaurant_name = fake.company()

        used_restaurant_names.add(restaurant_name)

        restaurant = Restaurant(
            name=restaurant_name,
            address=fake.address()
        )
        db.session.add(restaurant)

    # Set to keep track of used pizza names
    used_pizza_names = set()

    # Seed Pizzas
    for _ in range(30):
        pizza_name = fake.word()
        # Ensure unique pizza name
        while pizza_name in used_pizza_names:
            pizza_name = fake.word()

        used_pizza_names.add(pizza_name)

        pizza = Pizza(
            name=pizza_name,
            ingredients=', '.join(fake.words(5)),  # Generate random ingredients
            price=randint(5, 30)
        )
        db.session.add(pizza)

    # Seed Restaurant Pizzas
    restaurants = Restaurant.query.all()
    pizzas = Pizza.query.all()
    for restaurant in restaurants:
        for _ in range(randint(1, 5)):
            restaurant_pizza = RestaurantPizza(
                restaurant=restaurant,
                pizza=choice(pizzas),
                price=randint(5, 30)
            )
            db.session.add(restaurant_pizza)

    # Commit changes to the database
    db.session.commit()

print("Data seeded successfully!")
