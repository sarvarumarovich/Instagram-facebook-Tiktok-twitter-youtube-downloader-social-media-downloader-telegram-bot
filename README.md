# 🎥 Multi-Platform Video Downloader Bot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-Latest-blue.svg)](https://core.telegram.org/bots/api)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A powerful and intelligent Telegram bot that downloads videos from multiple social media platforms including **Instagram**, **YouTube**, **TikTok**, **Facebook**, and **Twitter/X**. Features smart caching, admin management, subscription enforcement, and queue processing with modern async Python architecture.

## ✨ Key Features

### 🎯 Multi-Platform Support
- **Instagram**: Reels, Posts, IGTV, Stories, Carousel posts
- **YouTube**: Videos, Shorts with quality selection (360p/480p/720p/MP3)
- **TikTok**: Videos and short-form content
- **Facebook**: Videos and Reels from public pages
- **Twitter/X**: Videos, GIFs, and media content

### 🚀 Advanced Capabilities
- ⚡ **Smart Caching System** - Eliminates duplicate downloads
- 🎛️ **Quality Selection** - Choose video quality for YouTube content
- ⏳ **Queue Management** - Efficient request processing
- 👥 **Group Support** - Works in Telegram groups and supergroups
- 🔧 **Admin Panel** - Complete management dashboard
- 🔒 **Subscription Enforcement** - Mandatory channel subscriptions
- 📸 **Instagram Bypass Profiles** - Skip checks for specific profiles
- 📊 **Comprehensive Logging** - Detailed monitoring and error tracking
- 🛡️ **Rate Limiting Protection** - Avoids API restrictions
- 🔐 **Secure Session Management** - Safe authentication handling

## 🏗️ System Architecture

Built on a **modular architecture** with three core components:

1. **🤖 Telegram Bot (Aiogram 3.x)** - Handles user interactions and serves cached content
2. **👤 Userbot (Telethon)** - Downloads content from source platforms
3. **💾 SQLite Database** - Manages caching, users, statistics, and configurations

## 📁 Project Structure

```
downloader/
├── bot/
│   ├── handlers.py         # Message handlers and callback functions
│   ├── main.py            # Bot application core and initialization
│   └── middleware.py      # Custom middleware and filters
├── userbot/
│   └── client.py          # Telethon userbot implementation
├── db/
│   ├── database.py        # SQLite database operations
│   └── videos.db          # Database file (auto-generated)
├── logs/
│   └── bot.log            # Application logs (auto-generated)
├── config.py              # Configuration management
├── utils.py               # URL validation and utility functions
├── main.py                # Application entry point
├── setup.bat              # Windows setup script
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This documentation
```

## 🚀 Quick Setup

### Prerequisites
- Python 3.8 or higher
- Telegram account
- Basic understanding of Telegram bots

### 1. Installation

**Option A: Using setup.bat (Windows)**
```batch
setup.bat
```

**Option B: Manual installation**
```bash
# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir logs db
```

### 2. Configuration

1. **Copy the environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file with your credentials:**
   ```env
   # Telegram API credentials (from https://my.telegram.org/apps)
   API_ID=your_api_id
   API_HASH=your_api_hash
   
   # Bot token from @BotFather
   BOT_TOKEN=your_bot_token
   
   # Private storage channel ID (must be negative)
   STORAGE_CHANNEL_ID=-1001234567890
   
   # Admin user IDs (comma-separated)
   ADMIN_IDS=123456789,987654321
   
   # Session configuration
   SESSION_NAME=userbot_session
   DATABASE_PATH=./db/videos.db
   LOG_LEVEL=INFO
   ```

### 3. Required Telegram Setup

#### Get API Credentials
1. Visit [my.telegram.org/apps](https://my.telegram.org/apps)
2. Log in with your phone number
3. Create a new application
4. Save your `API_ID` and `API_HASH`

#### Create Bot
1. Message [@BotFather](https://t.me/BotFather)
2. Use `/newbot` command
3. Follow the setup process
4. Save your bot token

#### Setup Storage Channel
1. Create a **private** Telegram channel
2. Add your bot as an **administrator**
3. Get the channel ID using [@userinfobot](https://t.me/userinfobot)
4. Ensure the ID is negative (e.g., -1001234567890)

### 4. First Run

```bash
python main.py
```

The bot will:
- Validate your configuration
- Authenticate your userbot (one-time setup)
- Initialize the database
- Start processing requests

## 📖 Usage Guide

### Private Chat Usage

1. **Start the bot:** Send `/start` to your bot
2. **Send a video URL** from any supported platform
3. **Bot automatically:**
   - Checks subscription requirements
   - Searches cache for existing video
   - Downloads if not cached
   - Delivers high-quality video

### Group Usage

1. **Add bot to group** as an administrator
2. **Send video URLs** in the group
3. **Bot processes** and replies to the original message
4. **For YouTube:** Mention the bot or reply for processing

### Supported URL Formats

| Platform | Supported URLs | Examples |
|----------|----------------|----------|
| **Instagram** | Posts, Reels, IGTV, Stories | `instagram.com/p/ABC123/`<br>`instagram.com/reel/XYZ789/` |
| **YouTube** | Videos, Shorts | `youtube.com/watch?v=ABC123`<br>`youtu.be/XYZ789` |
| **TikTok** | Videos, Short links | `tiktok.com/@user/video/123`<br>`vm.tiktok.com/ABC123/` |
| **Facebook** | Videos, Watch links | `facebook.com/watch/?v=123`<br>`fb.watch/XYZ789/` |
| **Twitter/X** | Status videos | `twitter.com/user/status/123`<br>`x.com/user/status/123` |

## 🔧 Admin Panel Features

Access via `/admin` command (admin users only):

### 📊 Statistics Dashboard
- User count and activity metrics
- Video download statistics
- Platform usage analytics
- Cache hit/miss ratios

### 👥 User Management
- View registered users
- User activity monitoring
- Broadcast messages to all users

### 🔒 Subscription Management
- Add/remove mandatory channels
- Configure subscription enforcement
- Monitor subscription compliance

### 📸 Instagram Bypass Profiles
- Add usernames to bypass subscription checks
- Manage profile-specific permissions
- Monitor bypass usage

## ⚙️ Advanced Configuration

### Environment Variables Reference

| Variable | Description | Required | Default |
|----------|-------------|----------|--------|
| `API_ID` | Telegram API ID | ✅ | - |
| `API_HASH` | Telegram API Hash | ✅ | - |
| `BOT_TOKEN` | Bot token from @BotFather | ✅ | - |
| `STORAGE_CHANNEL_ID` | Private channel for file storage | ✅ | - |
| `ADMIN_IDS` | Comma-separated admin user IDs | ✅ | - |
| `SESSION_NAME` | Userbot session filename | ❌ | `userbot_session` |
| `DATABASE_PATH` | SQLite database file path | ❌ | `./db/videos.db` |
| `LOG_LEVEL` | Logging verbosity | ❌ | `INFO` |

### Logging System

**Console Output:** Real-time formatted logs  
**File Logging:** Rotating logs in `logs/bot.log`
- Maximum file size: 10MB
- Retention period: 7 days
- Automatic rotation and cleanup

**Log Levels:**
- `DEBUG`: Detailed debugging information
- `INFO`: General information and status
- `WARNING`: Warning messages and recoverable errors
- `ERROR`: Error messages and exceptions

### Database Management

The SQLite database automatically handles:
- **Schema creation** on first run
- **URL normalization** for consistent caching
- **Duplicate prevention** through unique constraints
- **Data integrity** with foreign key relationships

**Manual cleanup example:**
```python
from db.database import Database
import asyncio

async def cleanup_old_data():
    db = Database('./db/videos.db')
    await db.cleanup_old_records(days=30)
    print("Cleanup completed")

asyncio.run(cleanup_old_data())
```

## 🛠️ Troubleshooting

### Common Issues & Solutions

#### Authentication Errors
**Error:** `"User is not authorized"`  
**Solution:**
- Restart the bot to trigger re-authentication
- Verify API_ID and API_HASH are correct
- Ensure you have access to the phone number used

#### Storage Channel Issues
**Error:** `"Cannot access storage channel"`  
**Solution:**
- Verify channel ID is negative (starts with -100)
- Ensure bot is added as channel administrator
- Check userbot has access to the channel

#### Download Failures
**Error:** Rate limiting or platform restrictions  
**Solution:**
- Wait for rate limits to reset
- Check if content is publicly accessible
- Verify platform-specific bot usernames in config

### Debug Mode

Enable detailed logging:
```env
LOG_LEVEL=DEBUG
```

This provides:
- Detailed request/response information
- Database query logs
- API call traces
- Performance metrics

## 📊 Performance Metrics

| Metric | Cached Content | New Content |
|--------|----------------|-------------|
| **Response Time** | 1-2 seconds | 30-60 seconds |
| **Bandwidth Usage** | Minimal | Platform-dependent |
| **Storage** | Telegram Cloud | Unlimited |
| **Database Size** | ~1KB per URL | Minimal footprint |

### Optimization Features
- **Smart Caching:** Prevents duplicate downloads
- **Queue Processing:** Handles concurrent requests efficiently
- **Rate Limiting:** Respects platform API limits
- **Resource Management:** Minimal memory and CPU usage

## 🔒 Security & Privacy

### Security Measures
- **Session Encryption:** Secure authentication storage
- **Admin-Only Access:** Restricted management functions
- **Input Validation:** Prevents malicious URL inputs
- **Rate Limiting:** Protects against abuse

### Privacy Considerations
- **Personal Account Usage:** Userbot uses your Telegram account
- **Data Storage:** Videos stored in your private channel
- **User Privacy:** No personal data collection beyond Telegram IDs
- **Platform Compliance:** Respects terms of service

### Best Practices
1. **Secure Environment:** Run on trusted servers only
2. **Regular Updates:** Keep dependencies up to date
3. **Access Control:** Limit admin permissions carefully
4. **Monitoring:** Regular log review for suspicious activity
5. **Backup Strategy:** Regular session and database backups

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Make your changes** with proper documentation
4. **Add tests** for new functionality
5. **Commit changes:** `git commit -m 'Add amazing feature'`
6. **Push to branch:** `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings for new functions
- Include error handling
- Update documentation as needed

## 📄 License & Legal

**Educational Purpose:** This project is intended for educational and personal use only.

**Platform Compliance:** Users must comply with:
- Instagram Terms of Service
- YouTube Terms of Service
- TikTok Terms of Service
- Facebook Terms of Service
- Twitter Terms of Service
- Telegram Terms of Service

**Disclaimer:** Users are responsible for ensuring their usage complies with all applicable laws and platform policies.

## 💡 Tips & Best Practices

### For Optimal Performance
1. **First Run:** Always authenticate userbot before first use
2. **Storage Management:** Keep storage channel private and organized
3. **Regular Monitoring:** Check logs for errors and performance issues
4. **Update Schedule:** Keep dependencies current for security patches
5. **Backup Strategy:** Regular backups of session files and database

### For Administrators
- Monitor subscription compliance regularly
- Use broadcast feature sparingly to avoid spam
- Review bypass profiles periodically
- Keep admin user list updated and secure

### For Users
- Send clean URLs without extra parameters when possible
- Be patient during peak usage times
- Report issues with specific error messages
- Respect rate limits and fair usage

---

## 📞 Support

**Having issues?** Check these resources:

1. **Log Files:** Review `logs/bot.log` for detailed error information
2. **Configuration:** Verify all required environment variables are set
3. **Permissions:** Ensure proper bot and channel permissions
4. **Documentation:** Re-read relevant sections of this README

**Need help?** Create an issue with:
- Detailed problem description
- Relevant log entries (remove sensitive information)
- Steps to reproduce the issue
- Your environment details

---

*Built with ❤️ using Python, Aiogram, and Telethon*
