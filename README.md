# BotForge25 🤖

A beginner-friendly Discord bot built with discord.py that demonstrates various command types and server management features.

## 📋 Overview

BotForge25 is an educational Discord bot project designed to help beginners learn Discord bot development. It showcases different command types (prefix, slash, and hybrid commands) and provides examples of interacting with Discord servers, channels, and members.

## ✨ Features

### Command Types
- **Prefix Commands**: Traditional commands using `?` prefix
- **Slash Commands**: Modern Discord slash commands
- **Hybrid Commands**: Commands that work both as prefix and slash commands

### Bot Capabilities
- Simple greeting commands (Hello World, Bye World, Greet)
- Channel listing (all channels, text channels, by type)
- Targeted message sending to specific channels
- Safe message sending with channel validation
- Server information display (name, ID, member count, owner details)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- A Discord account
- Basic knowledge of Python

### Installation

1. **Clone or download this repository**
   ```bash
   cd BotForge25
   ```

2. **Create a virtual environment**
   
   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your bot token**
   - Create a `.env` file in the project root
   - Add your Discord bot token:
     ```
     BOT_TOKEN=your_bot_token_here
     ```

5. **Run the bot**
   ```bash
   python main.py
   ```

## 🔑 Getting Your Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section and click "Add Bot"
4. Under "TOKEN", click "Reset Token" and copy it
5. Enable "MESSAGE CONTENT INTENT" under Privileged Gateway Intents
6. Go to OAuth2 → URL Generator
7. Select scopes: `bot` and `applications.commands`
8. Select bot permissions: `Send Messages`, `Read Messages/View Channels`, etc.
9. Copy the generated URL and use it to invite the bot to your server

## 📖 Available Commands

| Command | Type | Description | Usage |
|---------|------|-------------|-------|
| `?helloworld` | Prefix | Simple hello world response | `?helloworld` |
| `/byeworld` | Slash | Goodbye message | `/byeworld` |
| `?greet` or `/greet` | Hybrid | Personalized greeting with mention | `?greet` |
| `?allchannels` | Hybrid | Lists all server channels | `?allchannels` |
| `?textchannels` | Hybrid | Lists text channels only | `?textchannels` |
| `?channelsbytype` | Hybrid | Lists channels by type | `?channelsbytype text` |
| `?sendtochannel` | Hybrid | Sends message to specified channel | `?sendtochannel 123456789` |
| `?channeloptions` | Hybrid | Shows channel details | `?channeloptions #general` |
| `?safesend` | Hybrid | Sends message to channel with validation | `?safesend #general Hello!` |
| `?guildinfo` | Hybrid | Displays server information | `?guildinfo` |

### Channel Types for `channelsbytype` command:
- `all` - All channels
- `text` - Text channels only
- `voice` - Voice channels only
- `category` - Category channels only
- `stage` - Stage channels only

## 🛠️ Project Structure

```
BotForge25/
├── main.py              # Main bot code
├── requirements.txt     # Python dependencies
├── steps.txt           # Setup instructions
├── .env                # Environment variables (create this)
├── README.md           # This file
└── Guide.md            # Beginner's guide
```

## 📚 Learning Resources

For a detailed beginner's guide on understanding the code and Discord bot concepts, check out [Guide.md](Guide.md).

## 🤝 Contributing

This is an educational project. Feel free to:
- Add new commands
- Improve existing functionality
- Fix bugs
- Enhance documentation

## ⚠️ Important Notes

- Never share your bot token publicly
- Always add `.env` to your `.gitignore` file
- Test commands in a private server first
- Enable required intents in the Discord Developer Portal

## 📝 License

This project is open source and available for educational purposes.

## 🐛 Troubleshooting

**Bot not responding?**
- Check if MESSAGE CONTENT INTENT is enabled
- Verify your bot token is correct
- Ensure the bot has proper permissions in your server

**Slash commands not showing?**
- Wait a few minutes after starting the bot (Discord syncs globally)
- Check if `await my_bot.tree.sync()` is running in `on_ready` event

**Import errors?**
- Make sure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

## 📞 Support

For more detailed explanations and tutorials, refer to:
- [Guide.md](Guide.md) - Comprehensive beginner's guide
- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/docs/)

---

Happy Bot Building! 🚀
