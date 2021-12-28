from tnaggregator.models import Doc_table
from . import scrape_news as sp
from . import db
from .models import Doc_table
from sqlalchemy import exc
#import language_processing as lp

DOCUMENT_LIST = []


def scrape():
   global DOCUMENT_LIST
   RSS_FEED_LIST = ['https://techcrunch.com/feed/','http://feeds.feedburner.com/ProgrammableWeb','https://mashable.com/feeds/rss/tech']
   DOCUMENT_LIST = sp.scrape_rss(RSS_FEED_LIST)


def insert_doc_table():    
    for document in DOCUMENT_LIST:
        #new_doc = Doc_table(doc_title = document['title'],doc_link = document['link'],doc_date = document['date'])
        #db.session.add(new_doc)
        db.session.execute(Doc_table.__table__
                .insert()
                .prefix_with('IGNORE')
                .values(document))
        try:
            db.session.commit()
        except exc.IntegrityError:
            continue
    print("Doc Added")




scrape()
insert_doc_table()