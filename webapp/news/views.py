from flask import Blueprint, render_template

from webapp.news.models import News

blueprint = Blueprint('news', __name__)

@blueprint.route("/tproger")
def index():
    title = 'Новости Python'
    news_list = News.query.order_by(News.title).all()
    return render_template('news/index.html', page_title=title, news_list=news_list)

@blueprint.route("/")
def start():
    title = 'Pet project'
    return render_template('news/start.html', page_title=title)