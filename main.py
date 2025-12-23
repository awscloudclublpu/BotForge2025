import discord
from discord.ext import commands

my_intents = discord.Intents.default()
my_intents.message_content = True

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

my_bot = commands.Bot(
    command_prefix="?",
    intents=my_intents,
)

#Prefix Command
@my_bot.command(name="helloworld")
async def hello_world(ctx):
    await ctx.send("Hello, World!")

#Tree Command (Slash Command)
@my_bot.tree.command(name="byeworld")
async def byeworld(interaction: discord.Interaction):
    await interaction.response.send_message("Bye World!")

#Hybrid Command: Both slash and prefix
@my_bot.hybrid_command(name="greet")
async def greet(ctx):
    #await ctx.send("Greetings!")
    #await ctx.reply(ctx.guild.name)
    #await ctx.send(ctx.guild.id)
    #await ctx.reply(ctx.author.mention + " Greetings!")
    #await ctx.send(ctx.author.name + " Greetings!")
    #await ctx.send(ctx.author.display_name + " Greetings!")
    #await ctx.send(ctx.author.global_name)
    #await ctx.send(ctx.author.id)
    user_id = ctx.author.id
    await ctx.send(f"<@{user_id}> Greetings!")

#All Channels and Text Channels Commands
@my_bot.hybrid_command(name="allchannels")
async def allchannels(ctx):
    # server_id = ctx.guild.id
    all_channels = await ctx.guild.fetch_channels()
    for channel in all_channels:
        await ctx.send(f"- {channel.name} (ID: {channel.id})")

#Text Channels Command
@my_bot.hybrid_command(name="textchannels")
async def textchannels(ctx):
    # server_id = ctx.guild.id
    text_channels = ctx.guild.text_channels
    for channel in text_channels:
        await ctx.send(f"- {channel.name} (ID: {channel.id})")

#Combined Channels By Type Filter
@my_bot.hybrid_command(name="channelsbytype")
async def channelsbytype(ctx, type: str):
    if type.lower() == "all":
        mychannels = await ctx.guild.fetch_channels()
        for channel in mychannels:
            await ctx.send(f"- {channel.name} (ID: {channel.id})")
    elif type.lower() == "text":
        text_channels = ctx.guild.text_channels
        for channel in text_channels:
            await ctx.send(f"- {channel.name} (ID: {channel.id})")
    elif type.lower() == "voice":
        voice_channels = ctx.guild.voice_channels
        for channel in voice_channels:
            await ctx.send(f"- {channel.name} (ID: {channel.id})")
    elif type.lower() == "category":
        category_channels = ctx.guild.categories
        for channel in category_channels:
            await ctx.send(f"- {channel.name} (ID: {channel.id})")
    elif type.lower() == "stage":
        stage_channels = [ch for ch in ctx.guild.channels if isinstance(ch, discord.StageChannel)]
        for channel in stage_channels:
            await ctx.send(f"- {channel.name} (ID: {channel.id})")
    else:
        await ctx.send("Invalid channel type. Please use 'all', 'text', 'voice', 'category', or 'stage'.")

@my_bot.hybrid_command(name="sendtochannel")
async def send_to_channel(ctx, channel_id: str):
    channel = ctx.guild.get_channel(int(channel_id))
    #channel = my_bot.get_channel(channel_id)
    #print(channel)
    await channel.send("This is a message sent to the specified channel!")
    await ctx.send("Message sent to the specified channel!")
    #For prefix command, we don't need acknowledgement message
    #But for slash command, we need to send acknowledgement message

@my_bot.hybrid_command(name="channeloptions")
async def channeloptions(ctx, channel: discord.TextChannel):
    # channel = ctx.guild.get_channel(str(channel))
    #channel = my_bot.get_channel(channel_id)
    #print(channel)
    # await channel.send("This is a message sent to the specified channel!")
    # await ctx.send("Message sent to the specified channel!")
    #For prefix command, we don't need acknowledgement message
    #But for slash command, we need to send acknowledgement message
    await ctx.send(channel.name + " (ID: " + str(channel.id) + ")" + "(Position: " + str(channel.position) + ")")

####TASK
#
#
#CREATE A COMMAND WHICH WILL TAKE CHANNEL & MESSAGE AS INPUT
#AND SEND THE MESSAGE TO THE SPECIFIED CHANNEL
#BUT IF CHANNEL IS SAME AS THE CONTEXT CHANNEL, THEN SEND "NOT ALLOWED" MESSAGE
#
#
########
@my_bot.hybrid_command(name="safesend")
async def safesend(ctx, channel: discord.TextChannel, *, message: str):
    if channel.id == ctx.channel.id:
        await ctx.send("NOT ALLOWED")
    else:
        await channel.send(message)
        await ctx.send(f"Message sent to {channel.name}!")

####TASK
#
#
#CREATE A COMMAND WHICH WILL
#SEND GUILD DATA LIKE NAME, ID, MEMBER COUNT, OWNER NAME & ID
#TO THE CONTEXT CHANNEL
#
#
########
@my_bot.hybrid_command(name="guildinfo")
async def guildinfo(ctx):
    guild_name = ctx.guild.name
    guild_id = ctx.guild.id
    member_count = ctx.guild.member_count
    owner = ctx.guild.owner
    owner_name = owner.name
    owner_id = owner.id

    info_message = (
        f"Guild Name: {guild_name}\n"
        f"Guild ID: {guild_id}\n"
        f"Member Count: {member_count}\n"
        f"Owner Name: {owner_name}\n"
        f"Owner ID: {owner_id}"
    )

    await ctx.send(info_message)

####TASK
#HYBRID_GROUP COMMAND
#################################


@my_bot.event
async def on_ready():
    await my_bot.tree.sync()
    print(f"Logged in as {my_bot.user}")


if __name__ == "__main__":
    my_bot.run(TOKEN)