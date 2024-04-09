from flask_migrate import Migrate
from models import db  
from routes import create_app
from flask import Flask

app = create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Migrate(app, db) 

if __name__ == '__main__':
    app.run(debug=True, port=5000)
