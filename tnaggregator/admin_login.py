from os import abort
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import abort



class administrator(ModelView):
    def is_accessible(self):
        if current_user.is_admin == True:
            return current_user.is_authenticated
        else:
            return abort(404)    
   
        