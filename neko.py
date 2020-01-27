import sys
import discord
import scraping
import calculate

TOKEN = 'NjY5MTEwNjExMDQ0NTk3Nzcx.Xiwyww.9spDULBb_wqOgsUyWtSfqhXexmk'

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
        url = scraping.get_zukan_url(monster_name)
        if url is None:
            await message.channel.send('そんなモンスターはいねぇ')
        else:
            habitat_list = scraping.get_habitat_from_zukan(url)
            habitat_str = ''
            for i in range(len(habitat_list)):
                habitat_str += habitat_list[i] + '\n'
            await message.channel.send(habitat_str)
            await message.channel.send(url)

    if message.content.lower() == '/yohou':
        dic = calculate.get_forecast()
        await message.channel.send('---聖守護者-------------------\n' +
                                   '冥骸魔レギルラッゾ　' + dic['inuhone'] + '\n' +
                                   '紅殻魔スコルパイド　' + dic['sasori']  + '\n' +
                                   '翠将鬼ジェルザーク　' + dic['hage']  + '\n' +
                                   '\n' +
                                   '---防衛軍---------------------\n' +
                                   '　　残り' + dic['time_to_next'] + '分\n' +
                                   dic['current_group'] + '　<-　Now!\n' +
                                   dic['next_group'] + '\n' +
                                   dic['next_next_group'])

# run
client.run(TOKEN)
