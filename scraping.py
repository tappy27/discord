import requests
from bs4 import BeautifulSoup as bs
import re

def get_zukan_url(monster_name):
    r = requests.get('https://dragon-quest.jp/ten/monster/zukan/')
    soup = bs(r.content, 'html.parser')

    #get tag
    tag = soup.find('a', text=re.compile(monster_name))
    if tag is None:
        return 'そんなモンスターはいねぇ'

    #generate url
    url = 'https://dragon-quest.jp/ten/monster/zukan/' + tag.get('href')

    return url

def get_habitat_from_zukan(url):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')

    #get tags
    tags = soup.find_all('a', href=re.compile('https://dragon-quest.jp/ten/map/'))
    if tags is None:
        return '生息地記載無し'

    #extract data from tags
    habitat_list = []
    for i in range(len(tags)):
        if tags[i].string == 'アストルティア5大陸':break
        habitat_list.append(tags[i].string)

    return habitat_list
print(get_habitat_from_zukan('https://dragon-quest.jp/ten/monster/zukan/plant/12.php'))
