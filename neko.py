import sys
import discord
import scraping

TOKEN = 'NjY5MTEwNjExMDQ0NTk3Nzcx.XibE4w.KsXhFpmx3FMo_oM7pndTROI2ayI'

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

    if message.content == '/neko':
        await message.channel.send('にゃーん')


    if message.content.startswith('/dq-monster'):
        monster_name = message.content.lstrip('/dq-monster')
        monster_name = monster_name.replace(' ','')
        monster_name = monster_name.replace('　','')
        await url = scraping.get_zukan_url(monster_name)
        await message.channel.send(scraping.get_habitat_from_zukan(url))
        await message.channel.send(url)

# run
client.run(TOKEN)
