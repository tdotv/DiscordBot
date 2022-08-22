import discord
from discord.ext import commands

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)
        author = ctx.message.author
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{author.mention}, you do not have enough rights to execute this command!")
        elif isinstance(error, commands.UserInputError):
            await ctx.send(embed = discord.Embed(
                description = f"Correct use of the command: '{ctx.prefix}{ctx.command.name}' ({ctx.command.help})\nFor example: {ctx.prefix}{ctx.command.usage}"
            ))

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))