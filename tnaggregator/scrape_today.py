import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import datetime,timezone,timedelta
import pytz

news_list = []



def make_time_aware(unaware_time):
    utc=pytz.UTC
    aware_time = unaware_time.replace(tzinfo=utc)
    return aware_time

def get_content(doc_link):
    content=''
    url = requests.get(doc_link)
    soup = BeautifulSoup(url.content,'html.parser')
    paragraphs = soup.select('p')
    for paragraph in paragraphs:  
        if 'Image Credits:' in (paragraph.text):
            continue
        content += '\n'+paragraph.text
    return content

def format_date(pubDate):
    date_time_obj= parse(pubDate)
    return date_time_obj

def do_scrape(url,last_inserted_time):
    global news_list
    last_inserted_time = make_time_aware(last_inserted_time)
    news_dictionary = {}
    url = requests.get(url)
    soup = BeautifulSoup(url.content, features='xml')
    items = soup.find_all('item')   
 
    for item in items:
        published_on = format_date(item.pubDate.text)
        if published_on > last_inserted_time:
            news_dictionary['doc_title'] = item.title.text
            news_dictionary['doc_link'] = item.link.text
            news_dictionary['doc_date'] = published_on
            news_list.append(news_dictionary.copy()) 
        else:
            continue

def scrape_rss(rss_list,last_inserted_time):
    for rss_link in rss_list:
        do_scrape(rss_link,last_inserted_time) 
    if len(news_list)<1:
        return False
    else:
        return news_list




 