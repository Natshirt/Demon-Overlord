import discord
import sys, os

# core imports
from DemonOverlord.core.util.config import CommandConfig, BotConfig, DatabaseConfig, APIConfig, RelationshipConfig
from DemonOverlord.core.util.command import Command

class DemonOverlord(discord.Client):

    __slots__ = (
        "config", "commands", "database", "api"
    )

    def __init__(self, argv):
        workdir = os.path.dirname(os.path.abspath(__file__))
        confdir = os.path.join(workdir, "../config")

        # set the main bot config
        self.config = BotConfig(self, confdir, argv)
        self.commands = CommandConfig(confdir)
        self.database = DatabaseConfig()
        self.api = APIConfig(self.config)
        self.relationships = RelationshipConfig(self.database)

        super().__init__()

    async def on_ready(self):
        print("====== CONNECTED SUCCESSFULLY ======")
        print(f'Connected as: {self.user.name}')

    async def on_message(self, message:discord.Message):
        if message.author != self.user and message.content.startswith(self.config.mode["prefix"]):
            command = Command(self, message)
            await command.exec()

    