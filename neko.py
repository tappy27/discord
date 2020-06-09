import sys
import math
import pandas as pd
import discord

import monster
import maps
import forecast
import market_price

#TOKEN = 'your-token'

#bot research room
#TOKEN = 'NjY5MTEwNjExMDQ0NTk3Nzcx.XtNiGg.O36UP4Eu3ie11N86kgu8mQ6-XE4'

#rururunpow room
TOKEN = 'NzE2NTYzOTc4NDEwNzg2ODc2.XtNnIw.jG9UyIQcGxRaPNApYo2AnsFS-hA'

client = discord.Client()


# when log in
@client.event
async def on_ready():
    print('ログイン完了')

# when message from other bots
@client.event
async def on_message(message):
    if message.author.bot:
        return

# --------------------------------------------
# commands
# --------------------------------------------
    if message.content == ('/logout'):
        await client.logout()
        await sys.exit()

    if message.content.lower() == '/neko':
        await message.channel.send('にゃーん')
    
    if 'よくね？' in message.content.lower():
        await message.channel.send('https://cdn.discordapp.com/attachments/620381321973465089/692667162866876437/yokune.jpg')

    if message.content.lower() == '/tappy':
        await message.channel.send('tappyがやりたいこと' + '\n'
                                   '聖守護者（犬骨以外）' + '\n'
                                   '常闇' + '\n'
                                   '防衛軍' + '\n'
                                   '盗む金策' + '\n'
                                   '細胞' + '\n'
                                   '輝晶獣' + '\n'
                                   'コインボス (ドラゴン, 帝国三将軍, ゴレオン, ゲルニック, Sキラーマシン)')

    if message.content.lower() == '/miso':
        dic = forecast.get_forecast()
        await message.channel.send('さそりいきませんか？？' + '\n'
                                   '今日は ' + dic['sasori'] + ' です')

    if message.content.lower() in ['/sijimi', '/shijimi', '/sizimi', '/shizimi']:
        dic = forecast.get_forecast()
        await message.channel.send('ゴリラいきませんか？？' + '\n'
                                   '今日は ' + dic['gorilla'] + ' です')
    
    if message.content.lower() == '/peso':
        await message.channel.send('資産運用頑張ります')

    if message.content.lower().startswith('/tenbai'):
        price_str = message.content.lower().replace('/tenbai', '')
        price_str = price_str.replace(' ','')
        price_str = price_str.replace('　','')
        try:
            price = int(price_str)
        except:
            await message.channel.send('数字を入力してくれ')
        sell_price = math.ceil(price/95*100)
        buy_price = math.floor(price/100*95)
        await message.channel.send(price_str + 'G で利益が出るボーダー\n\n' +
                                   '売値　' + str(sell_price) + 'G　以上\n' +
                                   '買値　' + str(buy_price) + 'G　以下')

    if message.content.lower() == '/kira':
        await message.channel.send('https://dragon-quest.jp/ten/images/marason/ver5_1.gif')

    if message.content.lower().startswith('/monster'):
        monster_name = message.content.lower().replace('/monster', '')
        monster_name = monster_name.replace(' ','')
        monster_name = monster_name.replace('　','')
        url = monster.get_zukan_url(monster_name)
        if url is None:
            await message.channel.send('そんなモンスターはいねぇ')
        else:
            habitat_list = monster.get_habitat(url)
            habitat_str = ''
            for i in range(len(habitat_list)):
                habitat_str += habitat_list[i] + '\n'
            try:
                await message.channel.send(habitat_str)
                await message.channel.send(url)
            except:
                await message.channel.send('そんなモンスターはいねぇ')

    if message.content.lower().startswith('/map'):
        map_name = message.content.lower().replace('/map', '')
        map_name = map_name.replace(' ','')
        map_name = map_name.replace('　','')
        url = maps.get_map_url(map_name)
        if url is None:
            await message.channel.send('そんな場所はねぇ')
        else:
            image_list = maps.get_map_image(url)
            image_str = ''
            for i in range(len(image_list)):
                image_str += image_list[i] + '\n'
            else:
                await message.channel.send(image_str)
                await message.channel.send(url)

    if message.content.lower() == '/yohou':
        dic = forecast.get_forecast()
        await message.channel.send('---聖守護者-------------------\n'+
                                   '冥骸魔レギルラッゾ　' + dic['inuhone'] +'\n'+
                                   '紅殻魔スコルパイド　' + dic['sasori']  +'\n'+
                                   '翠将鬼ジェルザーク　' + dic['hage']  +'\n'+
                                   '剛獣鬼ガルドドン　　' + dic['gorilla']  +'\n'+
                                   '\n'+
                                   '---防衛軍---------------------\n'+
                                   '　残り' + dic['time_to_next'] + '分\n'+
                                   dic['current_group'] + '　<-　Now!\n'+
                                   dic['next_group'] +'\n'+
                                   dic['next_next_group'] +'\n'+
                                   '\n'+
                                   '次回の ドラゴン→全兵団 :\n'+ 
                                   dic['next_new_start'] + ':00 - ' + dic['next_new_end'] + ':00')


    if message.content.lower().startswith('/souba'):
        item_name = message.content.lower().replace('/souba', '')
        item_name = item_name.replace(' ','')
        item_name = item_name.replace('　','')

        # /souba update
        if item_name == 'update':
            await message.channel.send('相場データベース更新中...')
            market_price.update_csv()
            await message.channel.send('更新完了')
        
        elif item_name == 'rank':
            df = pd.read_csv('souba.csv', encoding='utf_8_sig', usecols=['item','price','num','date','graph'])
            df = df.set_index('item')
            normal, rare = market_price.get_drop_rank()
            mes = '---レアドロップ----------------------\n'
            for i in range(8):
                data = df.loc[rare[i]]
                mes += str(i+1) + '位 ' + rare[i] + '　'*(10 - len(rare[i])) + data['price'] +'\n'
            mes += '\n---通常ドロップ----------------------\n'
            for i in range(8):
                data = df.loc[normal[i]]
                mes += str(i+1) + '位 ' + normal[i] + '　'*(10 - len(normal[i])) + data['price'] +'\n'
            mes += '\nデータ更新日時: ' + data['date'] + '23:00付近'
            await message.channel.send(mes)

        else:
            try:
                df = pd.read_csv('souba.csv', encoding='utf_8_sig', usecols=['item','price','num','date','graph'])
                df = df.set_index('item')
                data = df.loc[item_name]
                await message.channel.send('相場:　 ' + data['price'] +'\n'+
                                           '出品数: ' + data['num'] +'\n\n'+
                                           'データ更新日時: ' + data['date'] +'\n'+
                                           data['graph'])
            except:
                await message.channel.send('なにそれ')

# run
client.run(TOKEN)
