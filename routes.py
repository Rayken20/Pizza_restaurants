from flask import Flask, jsonify, request
from flask_cors import CORS
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurantpizza import RestaurantPizza
from models import db

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')
    db.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        return "Index for restaurant/pizza API"

    @app.route('/restaurants', methods=['GET'])
    def get_restaurants():
        restaurants = Restaurant.query.all()
        restaurants_data = [{'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address} for restaurant in restaurants]
        return jsonify(restaurants_data)

    @app.route('/pizzas', methods=['GET'])
    def get_pizzas():
        pizzas = Pizza.query.all()
        pizzas_data = [{'id': pizza.id, 'name': pizza.name, 'price': pizza.price} for pizza in pizzas]
        return jsonify(pizzas_data)

    @app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
    def get_restaurant_with_pizzas(restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404
        
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': []
        }

        for restaurant_pizza in restaurant.restaurantpizzas:
            pizza_data = {
                'id': restaurant_pizza.pizza.id,
                'name': restaurant_pizza.pizza.name,
                'ingredients': restaurant_pizza.pizza.ingredients
            }
            restaurant_data['pizzas'].append(pizza_data)

        return jsonify(restaurant_data)

    @app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
    def delete_restaurant(restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404
        
       
        for restaurant_pizza in restaurant.restaurantpizzas:
            db.session.delete(restaurant_pizza)

        
        db.session.delete(restaurant)
        db.session.commit()

        return '', 204

    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
        data = request.get_json()
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

       
        pizza = Pizza.query.get(pizza_id)
        if not pizza:
            return jsonify({'error': 'Pizza not found'}), 404

        
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404

        
        restaurant_pizza = RestaurantPizza(restaurant=restaurant, pizza=pizza, price=price)
        db.session.add(restaurant_pizza)
        db.session.commit()

       
        pizza_data = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }
        return jsonify(pizza_data), 201

    return app
