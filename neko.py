import sys
import discord
import scraping
import calculate

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
        url = scraping.get_zukan_url(monster_name)
        if url is None:
            await message.channel.send('そんなモンスターはいねぇ')
        else:
            await message.channel.send(scraping.get_habitat_from_zukan(url))
            await message.channel.send(url)

    if message.content.lower() == '/yohou':
        dic = calculate.get_forecast()
        
        await message.channel.send('冥骸魔レギルラッゾ　　紅殻魔スコルパイド　　翠将鬼ジェルザーク\n' +
            '　'*4 + dic['inuhone'] + '　'*11 + dic['sasori'] + '　'*10 + dic['hage'] + '\n\n' +
            ' '*11 + '現在' + ' '*36 + '次回(' + dic['time_to_next'] + '分後)' + ' '*20 + '次々回(1時間' + dic['time_to_next'] + '分後)\n' +
            dic['current_group'] + '　'*5 + dic['next_group'] + '　'*5 + dic['next_next_group'])
# run
client.run(TOKEN)
