from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self):
        super().__init__()
    
    @commands.hybrid_group(name="greet")
    async def greet(self, ctx):
        pass

    @greet.command(name="hello")
    async def hello(self, ctx, message: str):
        await ctx.send(f"Hello! You said: {message}")

async def setup(bot):
    await bot.add_cog(Greetings())
#Why async def setup(bot):
#This is required for loading cogs in discord.py v2.0 and above.
