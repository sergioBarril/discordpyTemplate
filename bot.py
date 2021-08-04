# bot.py
import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class BotTemplate(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix=command_prefix)

    async def on_ready(self):
        print("Bot ready!")    

client = BotTemplate(command_prefix=["."])
client.load_extension("cogs.Template")

client.run(TOKEN)