from tnaggregator.models import doc_table
from . import scrape_news as sp
from . import db
#import language_processing as lp

DOCUMENT_LIST = []


def scrape():
   global DOCUMENT_LIST
   RSS_FEED_LIST = ['https://techcrunch.com/feed/','http://feeds.feedburner.com/ProgrammableWeb','https://mashable.com/feeds/rss/tech']
   DOCUMENT_LIST = sp.scrape_rss(RSS_FEED_LIST)


def insert_doc_table():    
    for document in DOCUMENT_LIST:
        db.session.execute(doc_table.__table__.insert().prefix_with('IGNORE').values(document))
        db.session.commit()
        
    print("Doc Added")




scrape()
insert_doc_table()