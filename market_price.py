import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_drop_rank():
    url = 'http://www.d-quest-10.com/ranking/usual/default_1.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    normal_rank=[]
    for i in range(10):
        tag = soup.find('span', text= str(i+1) + '位').find_next('a')
        normal_rank.append(tag.text)

    url = 'http://www.d-quest-10.com/ranking/sozai/default_1.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rare_rank=[]
    for i in range(10):
        tag = soup.find('span', text= str(i+1) + '位').find_next('a')
        rare_rank.append(tag.text)

    return(normal_rank, rare_rank)


# make lists of items, exhibit_nums, prices, graphs, and update_dates.
# then export these lists to csv 
def update_data(data_dict, url):

    items = []
    exhibit_nums = []

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tags_item = soup.select('table > tr > td:nth-of-type(1) > a:nth-of-type(2)')
    tags_exhibit_num = soup.select('table > tr > td:nth-of-type(3)')

    for i, j in zip(tags_item, tags_exhibit_num[2:-2]):
        items.append(i.text)
        exhibit_nums.append(j.text)

    for tag, item, exhibit_num in zip(tags_item, items, exhibit_nums):

        data_dict['item'].append(item)
        data_dict['num'].append(exhibit_num)

        if exhibit_num == '不可':
            data_dict['price'].append('-')
            data_dict['graph'].append('-')
            data_dict['date'].append(('-'))
        else:
            tags_price = []
            max_cnt = 15
            cnt = 0
            while tags_price == [] and cnt < max_cnt:
                r_price = requests.get('http://bazaar.d-quest-10.com/' + tag.get('href'))
                soup_price = BeautifulSoup(r_price.content, 'html.parser')
                tags_price = soup_price.select('p > table > tr > td:nth-of-type(3)')
                cnt += 1
            if cnt == max_cnt:
                data_dict['price'].append('更新失敗')
            else:
                data_dict['price'].append(tags_price[1].text)

            tags_date = []
            cnt = 0
            while tags_date == [] and cnt < max_cnt:
                r_price = requests.get('http://bazaar.d-quest-10.com/' + tag.get('href'))
                soup_price = BeautifulSoup(r_price.content, 'html.parser')
                tags_date = soup_price.select('p > table > tr > td:nth-of-type(1)')
                cnt +=1
            if cnt == max_cnt:
                data_dict['date'].append('更新失敗')
            else:
                data_dict['date'].append(tags_date[1].text)

            tags_div = None
            cnt = 0
            while tags_div == None and cnt < max_cnt:
                r_price = requests.get('http://bazaar.d-quest-10.com/' + tag.get('href'))
                soup_price = BeautifulSoup(r_price.content, 'html.parser')
                tags_div = soup_price.find('div', text='[最安値]')
                cnt += 1
            if cnt == max_cnt:
                data_dict['graph'].append('更新失敗')
            else:
                img = tags_div.find_next('img')
                data_dict['graph'].append(img['src'].replace('\n',''))
        print(item, exhibit_num, data_dict['price'][-1], data_dict['date'][-1])

    return data_dict

def update_csv():
    data_dict = {'item':[], 'price':[], 'num':[], 'date':[], 'graph':[]}
    urls = ['http://bazaar.d-quest-10.com/list/o_material/pop_2.html',
            'http://bazaar.d-quest-10.com/list/o_supply_item/pop_2.html']
    for url in urls:
        data_dict = update_data(data_dict, url)
    
    df = pd.DataFrame.from_dict(data_dict)
    df.to_csv('souba.csv', encoding='utf_8_sig')
