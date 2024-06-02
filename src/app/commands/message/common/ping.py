import discord

from discord.ext import commands

class PingPrefixCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.reply(content=f"Hello {ctx.author} my ping is {self.client.latency}ms")

    
async def setup(client: commands.Bot):
    await client.add_cog(PingPrefixCommand(client))
