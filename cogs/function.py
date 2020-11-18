import discord
from discord.ext import commands


class Function(commands.Cog):
    """Offer simple functions """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['clean', '청소'])
    async def clear(self, ctx):
        """Remove recent 100 messages"""
        await ctx.channel.purge(limit=100)

    @commands.command(aliases=['메아리', '에코'], hidden=True)
    async def echo(self, ctx, *, message: str):
        """Echo given message"""
        await ctx.channel.purge(limit=1)
        await ctx.send(message)

    @commands.command(aliases=['시리야'])
    async def siri(self, ctx):
        """General call"""
        await ctx.send("How can I help?")


def setup(bot):
    bot.add_cog(Function(bot))
