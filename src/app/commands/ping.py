from __future__ import annotations

import discord
from discord.ext import commands


class PingCommand(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.hybrid_command(name="ping", description="Veja o ping da aplicação.")
    async def ping(self, ctx: commands.Context) -> None:
        async with ctx.typing():
            try:
                await ctx.send(
                    f":ping_pong:Pong, meu ping está em {round(self.client.ws.latency * 1000, 2)}ms"
                )
                return
            except:
                await ctx.send(
                    content="Ocorreu um erro ao verificar o ping\n-# Verifique se a aplicação tem as permissões para enviar mensagens."
                )


async def setup(client: commands.Bot) -> None:
    await client.add_cog(PingCommand(client))
