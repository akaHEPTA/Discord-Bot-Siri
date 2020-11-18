import discord
from discord.ext import commands


class Maintenance(commands.Cog):
    """Maintenance Tools"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="update", hidden=True)
    @commands.is_owner()
    async def change_presence(self, ctx, *, activity="with the API"):
        """Update bot presence"""
        await self.bot.change_presence(activity=discord.Game(name=activity))
        await ctx.send("⚠ **Successfully updates presence**")


def setup(bot):
    bot.add_cog(Maintenance(bot))
