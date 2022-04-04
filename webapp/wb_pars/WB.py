from unittest import result
import requests

def wb():
    wb_url = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/stocks?dateFrom=2022-04-04&key=OGFmNWY3N2YtMmUzYy00MWNmLTg0ZDgtYzUxNTkwZjM4YmM0'
    result = requests.get(wb_url)
    wb = result.json()
    c = list()
    for i in wb:
        c.append(i['quantity'])
    return c[0]

if __name__ == "__main__":
    a = wb()
    print(a)