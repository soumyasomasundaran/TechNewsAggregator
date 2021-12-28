from flask import Blueprint, render_template
from . import technews as tn
views = Blueprint('views',__name__)

@views.route('/')
def index():
    news_list = tn.fetch_news()
    print(news_list)
    return render_template('index.html',news_list = news_list)

