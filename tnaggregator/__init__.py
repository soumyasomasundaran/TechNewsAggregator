from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME  = 'technews.db' 

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:Minimum@15@localhost/{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .models import Doc_table,Entity_table

    app.register_blueprint(views,url_prefix= '/')


    create_database(app)
    return app

def create_database(app):
    if path.exists('tnaggregator/'+DB_NAME):
        db.create_all(app = app)
        print("Database Created")
