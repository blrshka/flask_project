from datetime import datetime
import locale
import platform

from bs4 import BeautifulSoup

from webapp.news.models import News
from webapp.db import db
from webapp.news.parsers.utils import get_html, save_news

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU')

def get_habr_snippets():
    html = get_html("https://tproger.ru/tag/python/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.findAll(class_='article')
        for news in all_news:
            title = news.find('a', class_='article__link').text
            url = news.find('a',class_='article__link')['href']
            save_news(title, url)
