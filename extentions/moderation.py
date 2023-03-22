import disnake
from disnake.ext import commands

class moderation(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Have People Vote For Something!")
    async def vote(self, ctx, *, tovote):
        await ctx.channel.purge(limit=1)
        message = await ctx.send(f"@everyone Vote for: {tovote}")
        await message.add_reaction('\U0001F44D')
        await message.add_reaction('\U0001F44E')
        

    @commands.slash_command(description="Bans a user from the server!")
    @commands.has_permissions(ban_members = True)
    async def ban(inter, member : disnake.Member, *, reason = None):
        await member.ban(reason = reason)
        await inter.response.send_message(f"**{member}** has been banned for **{reason}**.")

    @commands.slash_command(description="Kicks a user from the server!")
    @commands.has_permissions(kick_members=True)
    async def kick(inter, user: disnake.Member, *, reason = None):
        if not reason:
            await user.kick()
            await inter.response.send_message(f"**{user}** has been kicked for **no reason**.")
        else:
            await user.kick(reason=reason)
            await inter.response.send_message(f"**{user}** has been kicked for **{reason}**.")

def setup(bot: commands.Bot):
    bot.add_cog(moderation(bot))