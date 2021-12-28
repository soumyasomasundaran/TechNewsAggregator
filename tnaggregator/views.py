from flask import Blueprint, render_template
#from . import technews
views = Blueprint('views',__name__)

@views.route('/')
def index():

    return render_template('index.html')