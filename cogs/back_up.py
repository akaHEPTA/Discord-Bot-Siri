import discord
from discord.ext import commands


class BackUp(commands.Cog):
    """Control automatic chat backup system"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='backup')
    @commands.guild_only()
    async def backup(self, ctx):
        """Control chat backup system, requires permission"""
        await ctx.send(f"⚠ **Access Denied** | Admin Permission Required")


def setup(bot):
    bot.add_cog(BackUp(bot))
