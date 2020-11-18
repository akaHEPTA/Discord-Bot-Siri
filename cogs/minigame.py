import random

import discord
from discord.ext import commands


class MiniGame(commands.Cog):
    """Provide random mini-games"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='coin', aliases=['flip', 'flipcoin', '동전'])
    async def coin(self, ctx):
        """Flip a coin"""
        images = [
            "https://imgur.com/a/MqD9h8x",
            "https://imgur.com/a/LZrUZVL"
        ]
        result = random.randint(0, 1)
        embed = discord.Embed(
            title="🪙 Flip a Coin",
            color=0xc0c0c0
        )
        embed.set_thumbnail(url=images[result])
        embed.add_field(
            name="Your result is... " + ("Face!" if result == 0 else "Tail!"),
            value='\u200b',
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {ctx.author}",
            icon_url=ctx.author.avatar_url_as(format="png")
        )
        await ctx.send(embed=embed)

    @commands.command(name='dice', aliases=['roll', '주사위'])
    async def dice(self, ctx):
        """Roll the dice"""
        result = random.randint(1, 6)
        embed = discord.Embed(
            title="🎲 Roll a Dice",
            color=0xc0c0c0
        )
        embed.set_thumbnail(url="")
        embed.add_field(
            name=f"Your result is... {result}!",
            value='\u200b',
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {ctx.author}",
            icon_url=ctx.author.avatar_url_as(format="png")
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(MiniGame(bot))
