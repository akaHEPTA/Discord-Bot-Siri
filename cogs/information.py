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

    key = "KEY_REMOVED"
    address = "https://api.openweathermap.org/data/2.5/weather?q=New Westminster, Ca&appid="
    # address = "https://api.openweathermap.org/data/2.5/weather?q=Seoul, KR&appid="

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
        data = requests.get(self.address + self.key).json()

        embed = discord.Embed(
            title="🗺 Weather Information",
            description="📍 " + data["name"],
            color=0xc0c0c0
        )
        embed.set_thumbnail(url="https://openweathermap.org/img/wn/" + data["weather"][0]["icon"] + "@2x.png")

        embed.add_field(name='Weather Detail', value=str(data["weather"][0]["description"]).capitalize(), inline=False)
        embed.add_field(name='Temperature', value=str(round(data["main"]["temp"] - 273)) + "°C", inline=False)
        embed.add_field(name='Feels like', value=str(round(data["main"]["feels_like"] - 273)) + "°C", inline=False)
        embed.add_field(name='Lowest', value=str(round(data["main"]["temp_min"] - 273)) + "°C", inline=False)
        embed.add_field(name='Highest', value=str(round(data["main"]["temp_max"] - 273)) + "°C", inline=False)

        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url_as(format="png"))

        await ctx.send(embed=embed)
        # await ctx.send("⚠ **준비중인 기능입니다**")


def setup(bot):
    bot.add_cog(Information(bot))
