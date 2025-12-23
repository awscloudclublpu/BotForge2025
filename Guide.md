# BotForge25 Beginner's Guide 📚

Welcome! This guide will help you understand Discord bot development from the ground up using the BotForge25 project.

## Table of Contents
1. [Understanding Discord Bots](#understanding-discord-bots)
2. [Project Setup Explained](#project-setup-explained)
3. [Code Breakdown](#code-breakdown)
4. [Command Types Explained](#command-types-explained)
5. [Discord Concepts](#discord-concepts)
6. [Step-by-Step Tutorial](#step-by-step-tutorial)
7. [Common Patterns](#common-patterns)
8. [Next Steps](#next-steps)

---

## Understanding Discord Bots

### What is a Discord Bot?
A Discord bot is an automated program that can:
- Respond to commands
- Send messages
- Manage servers
- Moderate content
- Play music
- And much more!

### How Do Bots Work?
1. **Bot Account**: You create a special bot account through Discord Developer Portal
2. **Token**: Discord gives you a secret token (like a password)
3. **Code**: Your Python code uses this token to connect to Discord
4. **Events**: The bot listens for events (messages, commands, etc.)
5. **Responses**: The bot reacts to events based on your code

---

## Project Setup Explained

### Virtual Environment
```bash
python -m venv venv
```
**What it does**: Creates an isolated Python environment so packages don't conflict with other projects.

**Why it matters**: Different projects might need different versions of libraries.

### Activating the Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```
**macOS/Linux:**
```bash
source venv/bin/activate
```
**What it does**: Switches your terminal to use the isolated environment.

### Installing Dependencies
```bash
pip install -r requirements.txt
```
**What it does**: Installs all required Python packages listed in `requirements.txt`.

### Environment Variables (.env file)
```
BOT_TOKEN=your_bot_token_here
```
**Why use .env**: Keeps secrets separate from code so you don't accidentally share them.

---

## Code Breakdown

Let's break down `main.py` section by section:

### 1. Imports
```python
import discord
from discord.ext import commands
```
**Explanation**: 
- `discord`: The main discord.py library
- `commands`: Extension that adds command functionality

### 2. Intents
```python
my_intents = discord.Intents.default()
my_intents.message_content = True
```
**What are Intents?** 
Intents tell Discord what events your bot wants to receive. Think of them as permissions for what the bot can "see."

**Common Intents:**
- `message_content`: See message text
- `members`: Access member information
- `guilds`: Access server information

**Important**: You must enable these in the Discord Developer Portal too!

### 3. Loading Environment Variables
```python
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
```
**Explanation**:
- `load_dotenv()`: Reads the `.env` file
- `os.getenv("BOT_TOKEN")`: Gets the bot token from environment variables

### 4. Bot Initialization
```python
my_bot = commands.Bot(
    command_prefix="?",
    intents=my_intents,
)
```
**Explanation**:
- `command_prefix="?"`: Prefix commands start with `?`
- `intents=my_intents`: Passes the intents we configured

### 5. The on_ready Event
```python
@my_bot.event
async def on_ready():
    await my_bot.tree.sync()
    print(f"Logged in as {my_bot.user}")
```
**Explanation**:
- Triggered when bot successfully connects to Discord
- `tree.sync()`: Registers slash commands with Discord
- Prints confirmation message

### 6. Running the Bot
```python
if __name__ == "__main__":
    my_bot.run(TOKEN)
```
**Explanation**:
- Starts the bot using your token
- Connects to Discord and keeps the bot online

---

## Command Types Explained

### Prefix Commands
```python
@my_bot.command(name="helloworld")
async def hello_world(ctx):
    await ctx.send("Hello, World!")
```
**Usage**: `?helloworld`

**How it works**:
1. User types `?helloworld`
2. Bot detects the prefix `?`
3. Matches command name `helloworld`
4. Runs the function
5. Sends response

**Key Points**:
- `ctx` (context): Contains information about who sent the command, where, etc.
- `ctx.send()`: Sends a message to the same channel

### Slash Commands
```python
@my_bot.tree.command(name="byeworld")
async def byeworld(interaction: discord.Interaction):
    await interaction.response.send_message("Bye World!")
```
**Usage**: `/byeworld`

**How it works**:
1. User types `/` and selects command from menu
2. Discord sends interaction to bot
3. Bot responds using `interaction.response`

**Key Differences**:
- Uses `interaction` instead of `ctx`
- Must use `interaction.response.send_message()`
- Appears in Discord's command menu

### Hybrid Commands
```python
@my_bot.hybrid_command(name="greet")
async def greet(ctx):
    user_id = ctx.author.id
    await ctx.send(f"<@{user_id}> Greetings!")
```
**Usage**: `?greet` OR `/greet`

**Why use hybrid?**
- Works both ways!
- Users can choose their preferred method
- Best of both worlds

---

## Discord Concepts

### Context (ctx)
The `ctx` parameter contains everything about the command:

```python
ctx.author        # The user who sent the command
ctx.guild         # The server (guild) where command was sent
ctx.channel       # The channel where command was sent
ctx.message       # The actual message (for prefix commands)
```

### Interaction
For slash commands, `interaction` provides similar information:

```python
interaction.user      # The user who used the command
interaction.guild     # The server
interaction.channel   # The channel
```

### Guild (Server)
In Discord API, servers are called "guilds":

```python
ctx.guild.name           # Server name
ctx.guild.id             # Server ID
ctx.guild.member_count   # Number of members
ctx.guild.owner          # Server owner
```

### Channels
```python
# Get all channels
all_channels = await ctx.guild.fetch_channels()

# Text channels only
text_channels = ctx.guild.text_channels

# Voice channels only
voice_channels = ctx.guild.voice_channels

# Get specific channel by ID
channel = ctx.guild.get_channel(channel_id)
```

### Channel Types
1. **Text Channels**: For text messages
2. **Voice Channels**: For voice chat
3. **Category Channels**: Organize other channels
4. **Stage Channels**: For large audio events
5. **Forum Channels**: Thread-based discussions

---

## Step-by-Step Tutorial

### Example 1: Simple Command
Let's create a command that responds with current time:

```python
from datetime import datetime

@my_bot.hybrid_command(name="time")
async def current_time(ctx):
    now = datetime.now()
    time_string = now.strftime("%H:%M:%S")
    await ctx.send(f"Current time: {time_string}")
```

**Breakdown**:
1. Import datetime module
2. Create hybrid command named "time"
3. Get current time
4. Format it as string
5. Send response

### Example 2: Command with Parameters
```python
@my_bot.hybrid_command(name="say")
async def say_command(ctx, *, message: str):
    await ctx.send(message)
```

**Breakdown**:
- `*, message: str`: Takes all text after command as one parameter
- `*` means "consume remaining arguments"
- **Usage**: `?say Hello everyone!` → Bot says "Hello everyone!"

### Example 3: Conditional Logic
```python
@my_bot.hybrid_command(name="safesend")
async def safesend(ctx, channel: discord.TextChannel, *, message: str):
    if channel.id == ctx.channel.id:
        await ctx.send("NOT ALLOWED")
    else:
        await channel.send(message)
        await ctx.send(f"Message sent to {channel.name}!")
```

**Breakdown**:
1. Takes channel and message as parameters
2. Checks if target channel is same as current channel
3. If same, denies request
4. If different, sends message to target channel
5. Confirms action

---

## Common Patterns

### Pattern 1: Mentioning Users
```python
# Method 1: Using mention property
await ctx.send(ctx.author.mention)

# Method 2: Using ID with formatting
user_id = ctx.author.id
await ctx.send(f"<@{user_id}>")
```
**Result**: @Username (clickable mention)

### Pattern 2: Formatting Messages
```python
# Multi-line message
message = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"Role: {role}"
)
await ctx.send(message)

# Using f-strings
await ctx.send(f"Welcome {user.name} to {guild.name}!")
```

### Pattern 3: Error Handling
```python
@my_bot.hybrid_command(name="kick")
async def kick_user(ctx, member: discord.Member):
    try:
        await member.kick()
        await ctx.send(f"{member.name} was kicked!")
    except discord.Forbidden:
        await ctx.send("I don't have permission to kick members!")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
```

### Pattern 4: Iterating Through Collections
```python
@my_bot.hybrid_command(name="listmembers")
async def list_members(ctx):
    members = ctx.guild.members
    member_list = "\n".join([m.name for m in members])
    await ctx.send(f"Members:\n{member_list}")
```

---

## Common Questions

### Q: What does `async` and `await` mean?
**Answer**: 
- `async`: Marks a function as asynchronous (can wait without blocking)
- `await`: Waits for something to complete before continuing
- Discord bots are asynchronous because they handle multiple things at once

### Q: Why `ctx` instead of `context`?
**Answer**: 
It's just a naming convention. You could name it anything, but `ctx` is standard in discord.py community.

### Q: What's the difference between `send()` and `reply()`?
```python
await ctx.send("Message")      # Sends normal message
await ctx.reply("Message")     # Sends message that references original
```

### Q: How do I make the bot respond only in specific channels?
```python
@my_bot.hybrid_command(name="admin")
async def admin_command(ctx):
    allowed_channel_id = 123456789  # Replace with your channel ID
    if ctx.channel.id != allowed_channel_id:
        await ctx.send("This command only works in the admin channel!")
        return
    
    # Your command logic here
    await ctx.send("Admin command executed!")
```

### Q: Can I add permissions to commands?
```python
@my_bot.hybrid_command(name="clear")
@commands.has_permissions(manage_messages=True)
async def clear_messages(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
```

---

## Debugging Tips

### Problem: Bot is offline
**Solutions**:
- Check if bot is running (`python main.py`)
- Verify token is correct
- Check internet connection

### Problem: Commands not working
**Solutions**:
- Check if you used correct prefix (`?`)
- For slash commands, wait for sync (can take time)
- Check bot has permission to send messages

### Problem: "Missing Permissions" error
**Solutions**:
- Check bot role permissions in server settings
- Ensure bot role is higher than target roles
- Verify intents are enabled in Developer Portal

### Problem: Can't see message content
**Solution**:
Enable "Message Content Intent" in:
1. Discord Developer Portal → Bot → Privileged Gateway Intents
2. Your code: `my_intents.message_content = True`

---

## Best Practices

### 1. Always Use Try-Except for User Input
```python
@my_bot.hybrid_command(name="divide")
async def divide(ctx, a: int, b: int):
    try:
        result = a / b
        await ctx.send(f"Result: {result}")
    except ZeroDivisionError:
        await ctx.send("Cannot divide by zero!")
```

### 2. Validate User Permissions
```python
@my_bot.hybrid_command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban_user(ctx, member: discord.Member):
    await member.ban()
    await ctx.send(f"{member.name} was banned!")
```

### 3. Provide Helpful Error Messages
```python
@ban_user.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to ban members!")
```

### 4. Use Type Hints
```python
async def greet(ctx, name: str, age: int):
    # Discord auto-validates types
    await ctx.send(f"Hello {name}, age {age}!")
```

---

## Next Steps

### Beginner Projects
1. **Dice Roller**: Random number generator for games
2. **Poll Bot**: Create polls with reactions
3. **Reminder Bot**: Send reminders after time delay
4. **Weather Bot**: Fetch weather from API
5. **Quote Bot**: Random inspirational quotes

### Intermediate Concepts
- Cogs (organizing commands into modules)
- Database integration (SQLite, MongoDB)
- Embeds (fancy formatted messages)
- Buttons and Select Menus
- Modal forms for user input

### Advanced Topics
- Voice channel interaction
- Auto-moderation
- Economy systems
- Music playback
- Web dashboard

---

## Resources

### Documentation
- [discord.py Official Docs](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/docs/)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)

### Community
- [discord.py Discord Server](https://discord.gg/dpy)
- [r/Discord_Bots](https://reddit.com/r/Discord_Bots)

### Tutorials
- [discord.py Guide](https://guide.pycord.dev/)
- [Real Python Discord Bot Tutorial](https://realpython.com/how-to-make-a-discord-bot-python/)

---

## Practice Exercises

### Exercise 1: Create a Calculator Command
Create a command that takes two numbers and an operation (+, -, *, /) and returns the result.

### Exercise 2: Member Counter
Create a command that shows how many members have specific roles.

### Exercise 3: Welcome Messages
Make the bot send a welcome message when a new member joins the server.

### Exercise 4: Custom Prefix
Allow server admins to set a custom prefix for your bot per server.

### Exercise 5: Reaction Roles
Let users get roles by clicking reaction emojis.

---

## Conclusion

Congratulations! You now have a solid foundation in Discord bot development. Remember:

- **Start small**: Don't try to build everything at once
- **Read errors**: Error messages tell you what's wrong
- **Test often**: Test each feature as you add it
- **Ask for help**: The Discord.py community is helpful
- **Have fun**: Bot development is creative and rewarding!

Happy coding! 🚀

---

*Last updated: December 2025*
