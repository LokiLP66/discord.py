import discord


TOKEN = '###BotToken###'

bot = discord.Client()


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')


bot.run(TOKEN)