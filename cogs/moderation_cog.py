import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, message, before, after):
        if message.author.bot == True:
            return
        fmt = "{0.author}Corrected his message:\n{0.content} -> {1.content}"
        await before.channel.send(fmt.format(before, after))

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        fmt = "{0.author} has deleted the message: {0.content}"
        await message.channel.send(fmt.format(message))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, id=820590048906051626)
        await member.add_roles(role)

    @commands.command(name = "hello", help = "Welcome the bot") 
    async def hello(self, ctx):
        author = ctx.message.author
        await ctx.send( f" { author.mention } Hi, I am discord bot BotyaraRandom" )

    @commands.command(name = "clear", help = "Clear chat messages, by default 10 messages", usage = "clear <amount=10>")
    async def clear(self, ctx, amount: int = 10):
        if amount > 50:
            await ctx.send("You can't clear more than 50 messages")
            return
        else:
            await ctx.channel.purge(limit = amount)
            await ctx.send(f"Was deleted {amount} messages...")

    @commands.command(name = "mute", help = "Prevent user from writing and speaking", usage = "mute <@member>")
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, member: discord.Member):
        muted_role = ctx.guild.get_role(820591334561153074)
        await member.add_roles(muted_role)

        author = ctx.message.author
        await ctx.send(f"{author.mention} gave the role of mute {member}")

    @commands.command(name = "kick", help = "Kick user from the server", usage = "kick <@user> <reason=None>")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete(delay = 1)

        await member.send(f"You were kicked from the server")
        await ctx.send(f"{member.mention} was kicked from the server!")
        await member.kick(reason = reason)

    @commands.command(name = "ban", help = "Ban a user from the server", usage = "ban <@user> <reason=None>")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await member.send(f"You’ve been banned from this server")
        await ctx.send(f"{member.mention} was banned from this server")
        await member.ban(reason = reason)

    @commands.command(name = "unban", help = "Unban a user on the server", usage = "unban <@user>")
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split("#")
        for banned_entry in banned_users:
            user = banned_entry.user
            if(user.name, user.discriminator) == (member_name, member_disc):
                await ctx.guild.unban(user)
                await ctx.send(member_name + " was unbanned!")
                return
        await ctx.send(member + " wasn't found")

def setup(bot):
    bot.add_cog(Moderation(bot))