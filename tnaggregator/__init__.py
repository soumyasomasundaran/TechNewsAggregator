from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME  = 'technews' 
password = 'Minimum$15'
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{password}@localhost/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
from .views import views
from .models import Doc_table,Entity_table
app.register_blueprint(views,url_prefix= '/')
    


