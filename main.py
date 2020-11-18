import discord
import random
from discord.ext import commands

command_prefix = "!"
bot = commands.Bot(command_prefix=command_prefix)
token = "Nzc4Mzg4MTc4MzM5MzY0OTE1.X7RQew.znFjLmYR5OmyKCRXil2B_oAdz50"
backUpFlag = False


@bot.event
async def on_ready():
    print(f"Signed in as {bot.user.name} and ID is {bot.user.id}")
    print("----------")


@bot.command()
async def siri(ctx):
    """General call"""
    await ctx.send("How can I help?")


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


@bot.command()
async def echo(ctx, arg):
    """Echo given message"""
    await ctx.send(arg)


@bot.command()
async def dice(ctx):
    """Roll the dice"""
    await ctx.send(f"🎲 Your dice is... **{random.randint(1, 6)}**")


@bot.command()
async def coin(ctx):
    """Flip the coin"""
    flipcoin = ["face", "tail"]
    await ctx.send(f"🪙 Your coin is... **{flipcoin[random.randint(0, 1)]}**")

bot.run(token)