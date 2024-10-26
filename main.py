from __future__ import annotations

import asyncio
import os
import discord
import sys

from dotenv import load_dotenv

from src.core.client import App

load_dotenv()


async def main() -> None:
    discord.utils.setup_logging()
    token = os.getenv("APP_DEVELOPMENT_TOKEN") if '--dev' in sys.argv else os.getenv("APP_TOKEN")

    if token is None:
        raise Exception("Token is nescessary.")

    async with App() as app:
        await app.start(token=token, reconnect=True)

if __name__ == "__main__":
    asyncio.run(main())

