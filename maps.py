import requests
from bs4 import BeautifulSoup
import re

def get_map_url(map_name):
    url_table = ['https://dragon-quest.jp/ten/map/fild/',
                'https://dragon-quest.jp/ten/map/fild_r/',
                'https://dragon-quest.jp/ten/map/fild_t/',
                'https://dragon-quest.jp/ten/map/fild_n/',
                'https://dragon-quest.jp/ten/map/ver4/',
                'https://dragon-quest.jp/ten/map/ver5/',
                'https://dragon-quest.jp/ten/map/house/',
                'https://dragon-quest.jp/ten/map/off/',
                'https://dragon-quest.jp/ten/update/ver5_1/']

    #get map url
    tag = None
    for url in url_table:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        tag = soup.find('a', text=re.compile(map_name))
        if tag is not None:
            break

    url = tag.get('href')
    try:
        requests.get(url)
    except:
        print('error: 不適切なurlにアクセス')
        return None
    
    return url

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
