import requests

from pyquery import PyQuery as pq
import re

url = 'https://ssr1.scrape.center'
html = requests.get(url).text

doc = pq(html)
items = doc('.el-card').items()


with open('movies.txt', 'w', encoding='utf-8') as file:
    file.write(
        "============================================================\n")
    for item in items:
        name = item.find('a > h2').text()
        categories = [item.text() for item in item.find(
            '.categories button span').items()]
        published_at = item.find('.info:contains(上映)').text()
        published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(
            1) if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
        score = item.find('p.score').text()

        file.write(
            f'name: {name}\ncategories: {categories}\npublished_at: {published_at}\nscore: {score}\n')
        file.write(
            "============================================================\n")
