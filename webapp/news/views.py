from flask import Blueprint, render_template

from webapp.news.models import News

blueprint = Blueprint('news', __name__)

@blueprint.route("/")
def index():
    title = 'Start page'
    news_list = News.query.order_by(News.title).all()
    return render_template('news/index.html', page_title=title, news_list=news_list)