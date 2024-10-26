from __future__ import annotations

import discord
import logging
import os
import sys

from discord.ext import commands
from dotenv import load_dotenv
from glob import glob

from src.settings.config import settings

load_dotenv()
logging.basicConfig(level=logging.INFO)

class App(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=settings["app_prefix"],
            intents=discord.Intents.all(),
            help_command=None,
            description="Nebula Nexus",
        )

    async def setup_hook(self) -> None:
        await self._load_cogs("src/app")

    async def _load_cogs(self, folder: str) -> None:
            files = glob(os.path.join(folder, '**', '*.py'), recursive=True)
            for file in files:
                await self.load_extension(os.path.normpath(file).replace(os.sep, '.')[:-3])

    async def _sync_commands(self) -> None:
        synced = await self.tree.sync()
        logging.info(f"{len(synced)} commands synced successfully.")

    async def on_ready(self) -> None:
        logging.info(f"Logged in as {self.user}")
        logging.info(f"Discord.py: {discord.__version__}")
        logging.info(f"Python: {sys.version}")
        logging.info(f"Running on: {sys.platform}")

    async def on_connect(self) -> None:
        if "--sync" in sys.argv:
            await self._sync_commands()
        logging.info(f"{self.user} connected to Discord API successfully.")
