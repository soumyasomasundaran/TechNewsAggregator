import bs4
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import datetime

news_list = []


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
    date_time_obj= parse(pubDate[:-14])
    news_date = date_time_obj.strftime("%Y/%m/%d")
    return news_date

def do_scrape(url):
    global news_list
    news_dictionary = {}
    url = requests.get(url)
    soup = BeautifulSoup(url.content, features='xml')
    items = soup.find_all('item')
    
    for item in items:
        news_dictionary['doc_title'] = item.title.text
        news_dictionary['doc_link'] = item.link.text
        news_dictionary['doc_date'] = format_date(item.pubDate.text)
        news_list.append(news_dictionary.copy())


def scrape_rss(rss_list):
    for rss_link in rss_list:
        do_scrape(rss_link)    
    return news_list