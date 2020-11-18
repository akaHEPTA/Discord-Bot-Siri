import random
import datetime
from pytz import timezone, utc

import discord
from discord.ext import commands
from discord.utils import get

BOT_PREFIX = "!"
bot = commands.Bot(command_prefix=BOT_PREFIX)
token = "Nzc4Mzg4MTc4MzM5MzY0OTE1.X7RQew.znFjLmYR5OmyKCRXil2B_oAdz50"


@bot.event
async def on_ready():
    print("----------")
    print(f"Bot Name: {bot.user.name}")
    print(f"Bot id: {bot.user.id}")
    print("Discord Version: " + discord.__version__)
    print("----------")


@bot.command()
async def backup(ctx):
    """Chat backup commands, required arguments"""
    await ctx.send(f"**⚠ Chat backup function is not implemented yet**")
    # if arg == "on":
    #     await ctx.send("**⚠️ Chat backup enabled**")
    # elif arg == "off":
    #     await ctx.send("**⚠ Chat backup disabled**")
    # elif arg == "status":
    #     messege = "on" if backUpFlag else "off"
    #     await ctx.send(f"**⚠ Chat backup is {messege} **")


@bot.command(aliases=['clean'])
async def clear(ctx):
    """Clear recent 100 messages"""
    await ctx.channel.purge(limit=100)


@bot.command()
async def siri(ctx):
    """General call"""
    await ctx.send("How can I help?")


@bot.command()
async def echo(ctx, *, message: str):
    """Echo given message"""
    await ctx.send(message)


@bot.command(pass_context=True, aliases=['flip', 'flipcoin'])
async def coin(ctx):
    """Flip a coin"""
    images = [
        "https://upload.wikimedia.org/wikipedia/en/6/6c/Toonie_-_back.png",
        "https://upload.wikimedia.org/wikipedia/en/d/d2/Toonie_-_front.png"
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


@bot.command()
async def dice(ctx):
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


@bot.command(aliases=['vancouver'])
async def time(ctx):
    """Shows time in various cities"""
    embed = discord.Embed(
        title="🌎 World Clock",
        color=0xc0c0c0
    )
    now = datetime.now()
    embed.add_field(
        name="Vancouver",
        value=f"`Vancouver {now.year}/{now.month}/{now.day} {now.hour}:{now.minute}`",
        inline=False
    )



    await ctx.send(f"`Vancouver {now.year}/{now.month}/{now.day} {now.hour}:{now.minute}`")


bot.run(token)
