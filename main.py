import asyncio
import os

from src.classes.client import client
from dotenv import load_dotenv

load_dotenv()

async def main():
    await client._load_cogs("src/app")
    await client.start(os.getenv("app_token"))

asyncio.run(main())