from flask import Flask
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://ba00038f27c785:bbe2d1da@eu-cdbr-west-02.cleardb.net/heroku_c48b175565e2cfa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "tHISiSAsUPERKEY"
app.config['SQLALCHEMY_POOL_RECYCLE'] = 50

db = SQLAlchemy(app)
login_manager =LoginManager()
admin = Admin()


db.init_app(app)
login_manager.init_app(app)
admin.init_app(app)

from .admin_login import administrator
from .models import doc_table,entity_table,user_table,rss_table

admin.add_view(administrator(user_table, db.session))
admin.add_view(administrator(rss_table, db.session))
admin.add_link(MenuLink(name='Home Page', url='/', category='Links'))

from .views import views
from .auth import auth

app.register_blueprint(views,url_prefix= '/')
app.register_blueprint(auth,url_prefix= '/')



db.create_all() 
db.session.commit()

login_manager.login_view = "auth.login"
@login_manager.user_loader
def load_user(id):
    return user_table.query.get(int(id))


