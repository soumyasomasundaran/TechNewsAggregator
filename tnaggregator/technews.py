from . import scrape_news as sp
#import database_actions as db
#import language_processing as lp

DOCUMENT_LIST = []

#scrape websites

def scrape():
   global DOCUMENT_LIST
   RSS_FEED_LIST = ['https://techcrunch.com/feed/','http://feeds.feedburner.com/ProgrammableWeb','https://mashable.com/feeds/rss/tech']
   DOCUMENT_LIST = sp.scrape_rss(RSS_FEED_LIST)
   print(DOCUMENT_LIST)
   return DOCUMENT_LIST


scrape()
#insert_doc_table()
#extract_all_entities()