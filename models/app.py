from flask import Flask
from flask_migrate import Migrate
from config import db
from routes import create_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    create_routes(app)  
    return app

app = create_app()

app.json.compact = False
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(port=5005, debug=True)
