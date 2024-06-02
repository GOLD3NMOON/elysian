import discord

from discord.ext import commands
from discord import app_commands

class PingSlashCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="ping", description="Return ping from bot")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        try:
            return interaction.followup.send(content=f"Hello {ctx.author} my ping is {self.client.latency}ms")
        except:
            pass
    
async def setup(client: commands.Bot):
    await client.add_cog(PingSlashCommand(client))
