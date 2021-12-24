from flask import Blueprint, render_template

blueprint = Blueprint('news', __name__)

@blueprint.route("/")
def index():
    title = 'Start page'
    return render_template('news/index.html', page_title=title)