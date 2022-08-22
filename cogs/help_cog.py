import discord.ext
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
Music
!play - Plays a selected song from youtube
!queue - Displays the current songs in queue
!skip - Skips the current song being played
!pause - Pauses music
!resume - Resumes music
!disconnect - Disconnect bot from VC

Moderation
!hello - Welcome the bot
!clear - Clear chat messages, by default 10 messages
!mute - Prevent user from writing and speaking
!kick - Kick a user from the server
!ban - Ban a user from the server
!unban - Unban a user on the server
"""
        self.text_channel_list = []

    # Assist words
    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content.lower()
        help_words = ["узнать информацию о сервере", "что умеет бот", "команды севера"]

        if msg in help_words:
            await message.channel.send(f"{message.author.mention}, введи !help")

    # Command !help using discord.Embed
    @commands.command(name = "help", help = "Displays all the available commands", usage = "help")
    async def help(self, ctx):
        embed = discord.Embed(
            color = 4575,
            title = "!help - displays all the available commands",
            description = self.help_message
        )
        embed.set_image(url = "https://i.imgur.com/Mv3Sskk.png")
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Help(bot))