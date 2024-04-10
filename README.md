# Pizza_restaurants
This API provides endpoints to manage restaurants, pizzas, and their relationships. It uses Flask as the web framework and SQLAlchemy as the ORM for interacting with the database.It allows users to perform CRUD operations on restaurants and pizzas, as well as associate pizzas with restaurants.

# Models

The application consists of three main models:
1. Restaurant: Represents a restaurant with attributes such as name and address.
2. Pizza: Represents a pizza with attributes such as name, ingredients, and price.
3. RestaurantPizza: Represents the association between restaurants and pizzas, including the price of the pizza at the restaurant.

## features
- Retrieve a list of restaurants
- Retrieve a list of pizzas
- Retrieve details of a specific restaurant including its pizzas
- Add a pizza to a specific restaurant
- Delete a restaurant along with its associated pizzas

 ## Endpoints
1. GET /restaurants 
Description: Retrieves a list of all restaurants.
Method: GET
Response: Returns a JSON array of restaurant objects, each containing the id, name, and address of the restaurant.

2. GET /pizzas
Description: Retrieves a list of all pizzas.
Method: GET
Response: Returns a JSON array of pizza objects, each containing the id, name, and price of the pizza.

3. GET /restaurants/:id 
Description: Retrieves details of a specific restaurant with its associated pizzas.
Method: GET
Response: Returns a JSON object representing the restaurant, including its id, name, address, and an array of pizzas with their details.

5. DELETE /restaurants/
Description: Deletes a specific restaurant along with its associated pizzas.
Method: DELETE
Response: Returns an empty response restaurant is deleted successfully.

6. POST /restaurant_pizzas
Description: Creates a new RestaurantPizza associated with an existing Pizza and Restaurant.
Method: POST
Request Body: JSON object with keys price (price of the restaurant pizza), pizza_id (ID of the pizza), and restaurant_id (ID of the restaurant).
Response: Returns details of the pizza that was created, including its id, name, and ingredients.

 ## Technologies used
- Flask
- SQLAlchemy
- Flask-CORS
## Set up:
- git clone the repository
- install required dependencies using pip
- Setup the database
- Start the flask server
- The server should run locally on http://127.0.0.1:5000.