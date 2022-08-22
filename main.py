import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'), intents = discord.Intents.all())
bot.remove_command('help')

# Notify about bot readiness
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------')

    await bot.change_presence(status = discord.Status.online, activity = discord.Game('хихи')) # Change bot status

# Load cogs
bot.load_extension("cogs.error_handler_cog")
bot.load_extension("cogs.help_cog")
bot.load_extension("cogs.moderation_cog")
bot.load_extension("cogs.music_cog")

# Connect bot
TOKEN = open( 'D:\Учеба\MOE\Discord_Bot\TOKEN.txt', 'r').readline()
bot.run(TOKEN)