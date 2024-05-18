from bs4 import BeautifulSoup
import requests
import pymongo
import datetime
base_url = 'https://www.tabnak.ir/fa/news/'
politics = 'politics'
economic = 'economic'
cultural = 'cultural'
social = 'social'
myClient = pymongo.MongoClient("mongodb://localhost:27017")
database = myClient['tabnak']


def crawler_news_tabnak():
    for i in range(100000, 113951):
        id_news = str(i)
        html = requests.get(base_url+id_news).text
        soup = BeautifulSoup(html, 'html.parser')
        try:
            tag_category = soup.find('div', class_='news_path').find_all('a')
        except AttributeError:
            continue
        tag_title = soup.find('h1', class_='Htag')
        tag_lead = soup.find('div', class_='subtitle')
        if len(tag_category) == 2 and tag_title != None and tag_lead != None:
            print("count:", i)
            news = {}
            category = tag_category[1].text.strip()
            title = tag_title.text.strip().replace('\u200c', ' ')
            lead = tag_lead.text.strip().replace('\u200c', ' ')
            news = {'title': title, "lead": lead,
                    'category': category, 'id_news': id_news}
            insert_one_mongodb(news, 'news')
            print('category:', category)
            print('title:', title)
            print('lead:', lead)


def insert_one_mongodb(my_dict, name_collection):
    my_collection = database[name_collection]
    my_collection.insert_one(my_dict)


def get_date_mongodb(name_collection):
    my_collection = database[name_collection]
    document = my_collection.find_one()
    return document


if __name__ == "__main__":
    crawler_news_tabnak()
