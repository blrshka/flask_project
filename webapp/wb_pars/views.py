from flask import Blueprint, render_template
import requests


blueprint = Blueprint('wb', __name__, url_prefix='/wb_static')

@blueprint.route('/')
def wb():
    wb_url = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/stocks?dateFrom=2022-04-04&key=OGFmNWY3N2YtMmUzYy00MWNmLTg0ZDgtYzUxNTkwZjM4YmM0'
    result = requests.get(wb_url)
    wb = result.json()
    c = list()
    for i in wb:
        c.append(i['quantity'])
    qwe = c[0]
    return render_template('wb/wb_index.html', e=qwe)

