from flask import Flask, current_app, make_response, jsonify, request, g
# from flask_cors import CORS
from restaurant import Restaurant, Pizza, RestaurantPizza, db

def create_routes(app: Flask) -> None:
    @app.route('/', methods=['GET'])
    def index():
        return "Index for restaurant/pizza API"

    @app.route('/restaurants', methods=['GET'])
    def get_restaurants():
        restaurants = Restaurant.query.all()
        restaurants_data = [{'id': restaurant.id, 'name': restaurant.name, 'location': restaurant.location} for restaurant in restaurants]
        return jsonify(restaurants_data)

    @app.route('/pizzas', methods=['GET'])
    def get_pizzas():
        pizzas = Pizza.query.all()
        pizzas_data = [{'id': pizza.id, 'name': pizza.name, 'toppings': pizza.toppings, 'price': pizza.price} for pizza in pizzas]
        return jsonify(pizzas_data)

    @app.route('/restaurants/<int:restaurant_id>/pizzas', methods=['GET'])
    def get_pizzas_for_restaurant(restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404
        pizzas_data = [{'id': rp.pizza.id, 'name': rp.pizza.name, 'toppings': rp.pizza.toppings, 'price': rp.price} for rp in restaurant.restaurantpizza]
        return jsonify(pizzas_data)

    @app.route('/restaurants/<int:restaurant_id>/add_pizza', methods=['POST'])
    def add_pizza_to_restaurant(restaurant_id):
        data = request.get_json()
        pizza_id = data.get('pizza_id')
        price = data.get('price')

        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404

        pizza = Pizza.query.get(pizza_id)
        if not pizza:
            return jsonify({'error': 'Pizza not found'}), 404

        
        restaurant_pizza = RestaurantPizza(restaurant=restaurant, pizza=pizza, price=price)
        db.session.add(restaurant_pizza)
        db.session.commit()

        return jsonify({'message': 'Pizza added to restaurant successfully'}), 200

    return app
