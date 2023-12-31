import discord
import logging

from src import config
from src.clients import accounts
from src.utils import groups
from src.utils.currency import robux_price
from discord.ext import commands


class revenue(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.holder_account = accounts.RobloxAccount(config.cfg_file["group"]["holder_cookie"])
        self.group_id = config.cfg_file["group"]["group_id"]
        self.logger = logging.getLogger(__name__)

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info("Revenue cog is ready")

    @commands.command(aliases=["robux", "bal", "balance"],
                      help="Gives an overview of the groups revenue(conversion included)")
    @commands.check(config.is_whitelisted)
    async def revenue(self, ctx):
        rates = config.cfg_get("rates") or 3.5

        group_info = groups.getGroupInfo(self.group_id)
        group_summary = self.holder_account.getGroupSummary(self.group_id)

        verified_robux = group_summary['robux']
        pending_robux = group_summary['pending_robux']
        total_robux = verified_robux + pending_robux

        embedBuild = discord.Embed(
            title=f"{group_info['name']} Balance",
            description=f"**Verified Robux:** {verified_robux} (${robux_price(verified_robux, rates)})\n**Pending "
                        f"Robux:** {group_summary['pending_robux']} (${robux_price(pending_robux, rates)})\n**Total("
                        f"Pending + Verified):** {total_robux} (${robux_price(total_robux, rates)})",
            color=config.EmbedColors.SUCCESS
        )

        embedBuild.set_footer(text=f"Currency converted using rates: ${rates} / 1k (2DP)")

        await ctx.reply(embed=embedBuild)


async def setup(client):
    await client.add_cog(revenue(client))
