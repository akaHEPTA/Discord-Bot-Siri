import discord
from discord.ext import commands


class Function(commands.Cog):
    """Offer simple functions """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear", aliases=['clean', '청소'])
    async def clear(self, ctx):
        """Remove recent 100 messages"""
        await ctx.channel.purge(limit=100)

    @commands.command(name="echo", aliases=['에코'])
    async def echo(self, ctx, *, message: str):
        """Echo given message"""
        await ctx.channel.purge(limit=1)
        await ctx.send(message)

    @commands.command(name="siri", aliases=['시리야'])
    async def siri(self, ctx):
        """General call"""
        await ctx.send("How can I help?")

    @commands.command(name="birthday", hidden=True)
    @commands.is_owner()
    async def birthday(self, ctx):
        await ctx.send("My birthday is November 17th, 2020. Thank you so much, dad! <@311874744674811904>")

    @commands.command(name="timer")
    async def timer(self, ctx):
        """"""
        await ctx.send("⚠ **준비중인 기능입니다**")


def setup(bot):
    bot.add_cog(Function(bot))
