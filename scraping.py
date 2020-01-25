import requests
from bs4 import BeautifulSoup as bs
import re
import jaconv

def get_zukan_url_kyokugen(monster_name):
    #r = requests.get('https://xn--10-yg4a1a3kyh.jp/dq10_monster.html')
    #soup = bs(r.content, 'html.parser')

    #get tag
    #TODO 正規表現うまくいってないからどーにかする
    print(re.compile('[\u30A1-\u30AA]'))
    if jaconv.kata2hira(monster_name[0]) == re.compile('[\u30A1-\u30AA]'): #ア行
        #r = request.get('https://xn--10-yg4a1a3kyh.jp/a_mon/dq10_monster_lg_a.html')
        return("aaaa")
    











def get_zukan_url(monster_name):
    r = requests.get('https://dragon-quest.jp/ten/monster/zukan/')
    soup = bs(r.content, 'html.parser')

    #get tag
    tag = soup.find('a', text=re.compile(monster_name))
    if tag is None:
        return None

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

print(get_zukan_url_kyokugen('アークデーモン'))