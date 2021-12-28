from flask import Blueprint, render_template,request
from . import technews as tn
views = Blueprint('views',__name__)

@views.route('/')
def index():
    news_list = tn.fetch_news()
    return render_template('index.html',news_list = news_list)

@views.route('/summary',methods = ['POST','GET'])
def summary():
    doc_id= request.args.get('doc_id')
    summary = tn.find_summary(doc_id)
    return render_template('summary.html',summary = summary)


@views.route('/entities',methods = ['POST','GET'])
def entities():
    doc_id= request.args.get('doc_id')
    entities = tn.find_entities(doc_id)
    return render_template('entity.html',entities = entities)
