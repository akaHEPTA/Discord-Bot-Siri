import os

import discord
from discord.ext import commands
import discord.utils

BOT_PREFIX = "$"
bot = commands.Bot(command_prefix=BOT_PREFIX, description='Virtual Assistant for Server 2.0')
token = "Nzc4Mzg4MTc4MzM5MzY0OTE1.X7RQew.znFjLmYR5OmyKCRXil2B_oAdz50"


if __name__ == '__main__':
    for file in os.listdir('cogs'):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")


@bot.event
async def on_ready():
    print(f'\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted!')
    await bot.change_presence(activity=discord.Game(name='훌륭한 봇이 되는 법 101'))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("⚠ **Missing Required Argument**")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("⚠ **Bad Argument**")
    else:
        embed = discord.Embed(title="⚠ Error", description=f"```{error}```", color=0xFF0000)
        await ctx.send(embed=embed)


@bot.command(name="load", hidden=True)
@commands.is_owner()
async def load_commands(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"⚠ **Successfully load the extension, \"{extension}\"**")


@bot.command(name="unload", hidden=True)
@commands.is_owner()
async def unload_commands(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"⚠ **Successfully unload the extension, \"{extension}\"**")


@bot.command(name="reload", hidden=True)
@commands.is_owner()
async def reload_commands(ctx, extension=None):
    if extension is None:
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                bot.unload_extension(f"cogs.{file[:-3]}")
                bot.load_extension(f"cogs.{file[:-3]}")
        await ctx.send("⚠ **Successfully reloads every extension**")
        print("⚠ **Successfully reloads every extension**")
    else:
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"⚠ **Successfully reload the extension, \"{extension}\"**")


bot.run(token, bot=True, reconnect=True)
