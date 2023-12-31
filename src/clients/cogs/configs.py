import discord
import requests
import logging

from src import config
from src.utils.currency import isFloatOrDigit
from discord.ext import commands


class configs(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.logger = logging.getLogger(__name__)

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info("Configs cog is ready")

    @commands.command(aliases=["s"], help="Sets a config to a given value ")
    @commands.check(config.is_whitelisted)
    async def set(self, ctx, config_name, value):

        # TODO: Change this after more configs are added...
        if str(config_name).lower() == "rates":

            if not isFloatOrDigit(str(value)):
                await ctx.reply("Argument for rates must be a number!")

            try:
                config.cfg_set("rates", value)

                await ctx.reply(f"Successfully set `rates` to `{value}`")
            except Exception as e:
                self.logger.error(e)
                await ctx.reply(f"Error setting rate to `{value}`")

    @commands.command(aliases=['g'], help="Gets the config")
    @commands.check(config.is_whitelisted)
    async def get(self, ctx, config_name):

        resp = config.cfg_get(key=str(config_name))
        if not resp:
            embed = discord.Embed(
                title="Error",
                color=config.EmbedColors.ERROR,
                description="The config specified does not exist."
            )

            await ctx.reply(embed=embed, ephemeral=True)
            return

        embed = discord.Embed(
            title="Config found ",
            description=f"The config `{str(config_name)}` is `{resp}`",
            color=config.EmbedColors.SUCCESS
        )

        await ctx.reply(embed=embed)


async def setup(client):
    await client.add_cog(configs(client))
