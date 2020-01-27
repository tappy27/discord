import sys
import discord
import monster
import maps
import forecast

TOKEN = 'your-token'

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


    if message.content.lower().startswith('/monster'):
        monster_name = message.content.lower().lstrip('/monster')
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
            await message.channel.send(habitat_str)
            await message.channel.send(url)

    if message.content.lower().startswith('/map'):
        map_name = message.content.lower().lstrip('/map')
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
            if image_str == '':
                print(url + 'にimage無し')
                await message.channel.send('そんな場所はねぇ')
            else:
                await message.channel.send(image_str)
                await message.channel.send(url)

    if message.content.lower() == '/yohou':
        dic = forecast.get_forecast()
        await message.channel.send('---聖守護者-------------------\n' +
                                   '冥骸魔レギルラッゾ　' + dic['inuhone'] + '\n' +
                                   '紅殻魔スコルパイド　' + dic['sasori']  + '\n' +
                                   '翠将鬼ジェルザーク　' + dic['hage']  + '\n' +
                                   '\n' +
                                   '---防衛軍---------------------\n' +
                                   '　残り' + dic['time_to_next'] + '分\n' +
                                   dic['current_group'] + '　<-　Now!\n' +
                                   dic['next_group'] + '\n' +
                                   dic['next_next_group'])

# run
client.run(TOKEN)
