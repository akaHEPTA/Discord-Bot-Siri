from datetime import datetime
from pytz import timezone
import requests
import json
import model.data


import discord
from discord.ext import commands


class Information(commands.Cog):
    """Inform you a useful data"""
    def __init__(self, bot):
        self.bot = bot

    key = "9ceb35e3f59caee12c59235d1b190e0d"
    address = "https://api.openweathermap.org/data/2.5/weather?q=New Westminster, Ca&appid="

    @commands.command(name='time', aliases=['clock', '시간'])
    async def time(self, ctx):
        """Show time of cities in various timezones"""
        fmt = "%Y-%m-%d %H:%M:%S"
        kst = datetime.now(timezone('Asia/Seoul'))
        pst = datetime.now(timezone('Canada/Pacific'))
        embed = discord.Embed(
            title="🌎 World Clock",
            color=0xc0c0c0
        )
        embed.add_field(
            name="Seoul, Republic of Korea (KST/UTC+9)",
            value=kst.strftime(fmt),
            inline=False
        )
        embed.add_field(
            name="Vancouver, Canada (PST/UTC-8)",
            value=pst.strftime(fmt),
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {ctx.author}",
            icon_url=ctx.author.avatar_url_as(format="png")
        )
        await ctx.send(embed=embed)

    @commands.command(name="stock")
    async def stock(self, ctx):
        """Show stock market data"""
        await ctx.send("⚠ **준비중인 기능입니다**")

    @commands.command(namㄷ="weather")
    async def weather(self, ctx):
        """Show weather of cities"""
        # data = requests.get(self.address + self.key).json()
        # # data: model.data = json.loads(jsondata)
        #
        # temp: float = data.temp - 273
        # embed = discord.Embed(
        #     title="🌤 Weather",
        #     color=0xc0c0c0
        # )
        # embed.add_field(name='🌡 Temperature', value=str(temp) + " °C")
        # embed.set_footer(
        #     text=f"Requested by {ctx.author}",
        #     icon_url=ctx.author.avatar_url_as(format="png")
        # )
        # await ctx.send(embed=embed)
        await ctx.send("⚠ **준비중인 기능입니다**")


def setup(bot):
    bot.add_cog(Information(bot))
