from requests.sessions import session
from tnaggregator.models import doc_table, entity_table
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

def find_entities(doc_id):
    entity_rows = db.session.query(entity_table).filter_by(doc_id=doc_id).all()    
    entities = [[row.entity_name,row.entity_type,row.entity_count] for row in entity_rows]
    return entities




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

def extract_entities():
    result =  doc_table.query.all()
    for rows in result:
        entity_list = extract_fromid(rows.id)
        insert_entity(entity_list,rows.id)
       # print('*'*20)

def insert_entity(entity_list,doc_id):
    for entity_tuple in entity_list:
        entity_dictionary  = {'entity_type':entity_tuple[1],'entity_name':entity_tuple[0],'entity_count':entity_tuple[2],'doc_id':doc_id}
        db.session.execute(entity_table.__table__.insert().prefix_with('IGNORE').values(entity_dictionary))
    db.session.commit()

def extract_fromid(id):
    content = content_from_id(id)
    entities = lp.extract_entities(content)
    return entities

#scrape()
#insert_doc_table()
#extract_entities()
