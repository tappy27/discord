import requests
from bs4 import BeautifulSoup
import re

def get_zukan_url(monster_name):
    r = requests.get('https://dragon-quest.jp/ten/monster/zukan/')
    soup = BeautifulSoup(r.content, 'html.parser')

    #get tag
    tag = soup.find('a', text=re.compile(monster_name))
    if tag is None:
        return None

    #generate url
    url = 'https://dragon-quest.jp/ten/monster/zukan/' + tag.get('href')    

    return url

def get_habitat_from_zukan(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    #get tags
    tags = soup.find_all('a', href=re.compile('https://dragon-quest.jp/ten/map/'))
    if tags is None:
        return '生息地記載無し'

    #extract data from tags
    habitat_list = []
    for i in range(len(tags)):
        if tags[i].string == 'アストルティア5大陸':
            break
        habitat_list.append(tags[i].string)

    return habitat_list

def get_map_url(map_name):
    url_table = ['https://dragon-quest.jp/ten/map/fild/',
                'https://dragon-quest.jp/ten/map/fild_r/',
                'https://dragon-quest.jp/ten/map/fild_t/',
                'https://dragon-quest.jp/ten/map/fild_n/',
                'https://dragon-quest.jp/ten/map/ver4/',
                'https://dragon-quest.jp/ten/map/ver5/',
                'https://dragon-quest.jp/ten/map/house/',
                'https://dragon-quest.jp/ten/map/off/']

    #get map url
    tag = None
    for url in url_table:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        tag = soup.find('a', text=re.compile(map_name))
        if tag is not None:
            break

    if tag is None:
        return None
    
    return tag.get('href')

def get_map_image(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    #get tags
    tags = soup.find_all('img', src=re.compile('../../images/'))
    if tags is None:
        return 'マップ画像なし'

    #get image from tags
    image_urls = []
    for tag in tags:
        image_urls.append(url + '/../' + tag.get('src'))

    return image_urls

"""
#以下、極限をスクレイピングするコード書こうと思ったけど、ダルくなって途中でやめたやつ
#あ行か行...ごとのページに不完全なものがあったから無理だった
def get_zukan_url(monster_name):

    #get source
    if re.match('[\u3041-\u304A]|[\u30A1-\u30AA]|\u3094|\u30F4', monster_name[0]): #あ行
        r = requests.get('https://xn--10-yg4a1a3kyh.jp/a_mon/dq10_monster_lg_a.html')
    elif re.match('[\u304B-\u3054]|[\u30AB-\u30B4]', monster_name[0]): #か行
        r = requests.get('https://xn--10-yg4a1a3kyh.jp/a_mon/dq10_monster_lg_ka.html')
    elif re.match('[\u3055-\u305E]|[\u30B5-\u30BE]', monster_name[0]): #さ行
        r = requests.get('https://xn--10-yg4a1a3kyh.jp/a_mon/dq10_monster_lg_sa.html')
    elif re.match('[\u305F-\u3069]|[\u30BF-\u30C9]', monster_name[0]): #た行
        r = requests.get('https://xn--10-yg4a1a3kyh.jp/a_mon/dq10_monster_lg_ta.html')
    elif re.match('[\u306A-\u306E]|[\u30CA-\u30CE]', monster_name[0]): #な行
        r = requests.get('https://xn--10-yg4a1a3kyh.jp/a_mon/dq10_monster_lg_na.html')
    elif re.match('[\u306F-\u307D]|[\u30CF-\u30DD]', monster_name[0]): #は行
        r = requests.get('https://xn--10-yg4a1a3kyh.jp/a_mon/dq10_monster_lg_ha.html')
    elif re.match('[\u307E-\u3082]|[\u30DE-\u30E2]', monster_name[0]): #ま行
        r = requests.get('https://xn--10-yg4a1a3kyh.jp/a_mon/dq10_monster_lg_ma.html')
    elif re.match('[\u3083-\u3088]|[\u30E3-\u30E8]', monster_name[0]): #や行
        r = requests.get('https://xn--10-yg4a1a3kyh.jp/a_mon/dq10_monster_lg_ya.html')
    elif re.match('[\u3089-\u308D]|[\u30E9-\u30ED]', monster_name[0]): #ら行
        r = requests.get('https://xn--10-yg4a1a3kyh.jp/a_mon/dq10_monster_lg_ra.html')
    elif re.match('[\u308E-\u3093]|[\u30EE-\u30F3]', monster_name[0]): #わ行
        r = requests.get('https://xn--10-yg4a1a3kyh.jp/a_mon/dq10_monster_lg_wa.html')
    else:
        print("ひらがな,カタカナ以外が入力されました")

    soup = BeautifulSoup(r.content, 'html.parser')

    #get tag
    tag = soup.find('a', text=re.compile(monster_name))
    if tag is None:
        return None

    #generate url
    url = 'https://xn--10-yg4a1a3kyh.jp/' + tag.get('href')[3:]

    return url


def get_monster_info_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    #get habitat
    tag = soup.find('h2', text=re.compile('の出現地域'))
    while tag.get('name') == 'a':
        tag = tag.nextSibling
        print(tag.get('name')) 
    print(tag.get('name'))
"""
