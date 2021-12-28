from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME  = 'heroku_75ce60fabbd29e1' 
password = '9b1b1f68'
app = Flask(__name__)
db = SQLAlchemy(app)
from .views import views
print("Tables created")
from .models import Doc_table,Entity_table
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://b654141abcadfd:{password}@eu-cdbr-west-02.cleardb.net/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
app.register_blueprint(views,url_prefix= '/')
    


