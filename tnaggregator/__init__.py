from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:Minimum$15@localhost/technews'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "tHISiSAsUPERKEY"

db = SQLAlchemy(app)
db.init_app(app)

from .models import doc_table

  
db.create_all() 
db.session.commit()
from .views import views
app.register_blueprint(views,url_prefix= '/')



