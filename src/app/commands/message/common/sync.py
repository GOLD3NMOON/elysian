from discord.ext import commands

import discord

class SyncCommandCog(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.command(name="sync")
    @commands.is_owner()
    async def sync_command(self, ctx: commands.Context):
        await ctx.send(content=f"Foram sicronizados {len(self.client.commands)} com sucesso!")
        await self.client.tree.sync()
        try:
            await ctx.reply(content=f"Foram sicronizados {len(self.client.commands)} com sucesso!")
        except discord.DiscordException:
            await ctx.send(content=f"Foram sicronizados {len(self.client.commands)} com sucesso!")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(SyncCommandCog(client))