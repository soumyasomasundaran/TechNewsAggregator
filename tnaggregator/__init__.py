from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME  = 'heroku_c48b175565e2cfa' 
password = 'bbe2d1da'
app = Flask(__name__)
db = SQLAlchemy(app)
from .views import views
from .models import Doc_table, Entity_table
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://ba00038f27c785:{password}@eu-cdbr-west-02.cleardb.net/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
app.register_blueprint(views,url_prefix= '/')
    


