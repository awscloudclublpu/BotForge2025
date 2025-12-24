from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.hybrid_group("moderate")
    async def moderate(self, ctx):
        """Moderation commands group."""
        pass
    
    @moderate.command(name="kick")
    async def kick(self, ctx, member: discord.Member):
        """Kick a member from the server."""
        await member.kick()
        await ctx.send(f"{member.name} has been kicked from the server.")
    
    @moderate.command(name="ban")
    async def ban(self, ctx, member: discord.Member):
        """Ban a member from the server."""
        await member.ban()
        await ctx.send(f"{member.name} has been banned from the server.")

    @moderate.command(name="unban")
    async def unban(self, ctx, member: discord.User):
        """Unban a member from the server."""
        await ctx.guild.unban(member)
        await ctx.send(f"{member.name} has been unbanned from the server.")

    #pip install pymongo
    
async def setup(bot):
    await bot.add_cog(Moderation(bot))