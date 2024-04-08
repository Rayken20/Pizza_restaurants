from flask_sqlalchemy import SQLAlchemy

class Config:
    # define constant variables for project 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


db = SQLAlchemy()
