from discord.ext import commands
import discord

from config import (

)


class VerificationBot(commands.Bot):
    def __init__(self, config):
        super().__init__(command_prefix=config.)