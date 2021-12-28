from requests.sessions import session
from tnaggregator.models import doc_table
from . import scrape_news as sp
from . import db
from  . import language_processing as lp

DOCUMENT_LIST = []



def content_from_id(doc_id):
    doc = db.session.query(doc_table).filter_by(id=doc_id).first()
    doc_link = doc.doc_link
    content = sp.get_content(doc_link)
    return content


def find_summary(doc_id):
    content = content_from_id(doc_id)
    summary  = lp.summarize(content)
    return summary




def scrape():
   global DOCUMENT_LIST
   RSS_FEED_LIST = ['https://techcrunch.com/feed/','http://feeds.feedburner.com/ProgrammableWeb','https://mashable.com/feeds/rss/tech']
   DOCUMENT_LIST = sp.scrape_rss(RSS_FEED_LIST)


def insert_doc_table():    
    for document in DOCUMENT_LIST:
        db.session.execute(doc_table.__table__.insert().prefix_with('IGNORE').values(document))
        db.session.commit()
        

def fetch_news():
    result =  doc_table.query.all()
    news_list = [[row.doc_title,row.doc_link,row.doc_date,row.id] for row in result]
    return news_list



#scrape()
#insert_doc_table()