from flask import Blueprint, render_template,request
from flask_login import login_required, current_user

from . import technews as tn


views = Blueprint('views',__name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html', user=current_user)
    

@views.route('/index')
@login_required
def index():
    news_list = tn.fetch_news()
    return render_template('index.html',news_list = news_list, user = current_user)

@views.route('/summary',methods = ['POST','GET'])
@login_required
def summary():
    doc_id= request.args.get('doc_id')
    summary = tn.fetch_summary(doc_id)
    return render_template('summary.html',summary = summary,user = current_user)


@views.route('/entities',methods = ['POST','GET'])
@login_required
def entities():
    doc_id= request.args.get('doc_id')
    entities = tn.find_entities(doc_id)
    return render_template('entity.html',entities = entities,user = current_user)


