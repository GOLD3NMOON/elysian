from discord.ext import commands 

class Ready(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.client.user} (ID: {self.client.user.id})\n------")

async def setup(client: commands.Bot):
    await client.add_cog(Ready(client))