from discord.ext import commands
import discord
import logging
import os
import asyncio
from dotenv import load_dotenv
from ..settings.config import settings
from glob import glob

load_dotenv()
logging.basicConfig(level=logging.INFO)

class NebulaNexus(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=settings["app_prefix"],
            intents=discord.Intents.all(),
            help_command=None,
            description="Nebula Nexus",
        )

    async def _load_cogs(self, folder: str) -> None:
            files = glob(os.path.join(folder, '**', '*.py'), recursive=True)
            for file in files:
                await self.load_extension(os.path.normpath(file).replace(os.sep, '.')[:-3])
            
client = NebulaNexus()