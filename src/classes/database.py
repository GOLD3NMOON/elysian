from __future__ import annotations
import os
import pymongo
import discord

class Database:
    def __init__(self, guild: discord.Guild) -> None:
        self.mongo = pymongo.MongoClient(os.getenv("MONGO_URI"))
        self.guild_id = str(guild.id)
        self.collection = self.mongo["starboard"][self.guild_id]

    def _get_settings(self) -> dict:
        return self.collection.find_one({"_id": self.guild_id}) or {}

    def _update_settings(self, updates: dict):
        self.collection.update_one({"_id": self.guild_id}, {"$set": updates}, upsert=True)

    def get_setting(self, key: str, default=None):
        return self._get_settings().get(key, default)

    def set_setting(self, key: str, value):
        self._update_settings({key: value})

    def get_settings(self) -> dict:
        return self._get_settings()

    def update_settings(self, updates: dict):
        self._update_settings(updates)

    def check_channel(self, channel_id: str) -> bool:
        return self.get_setting("channel_id") == channel_id

    def set_channel(self, channel_id: str):
        self.set_setting("channel_id", channel_id)

    def get_current_channel(self) -> str | None:
        return self.get_setting("channel_id")

    def set_stars(self, stars: int):
        self.set_setting("stars", stars)

    def get_stars(self) -> int | None:
        return self.get_setting("stars")

    def set_emojis(self, emojis: list):
        self.set_setting("emojis", emojis)

    def get_emojis(self) -> list:
        return self.get_setting("emojis", [])
