"""Configuration module for the Telegram automation system."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class containing all environment variables."""
    
    # Telegram API credentials
    API_ID = int(os.getenv('API_ID', 0))
    API_HASH = os.getenv('API_HASH', '')
    
    # Bot token
    BOT_TOKEN = os.getenv('BOT_TOKEN', '')
    
    # Storage channel ID
    STORAGE_CHANNEL_ID = int(os.getenv('STORAGE_CHANNEL_ID', 0))
    
    # Session configuration
    SESSION_NAME = os.getenv('SESSION_NAME', 'userbot_session')
    YOUTUBE_BOT_USERNAME = os.getenv('YOUTUBE_BOT_USERNAME', 'SaveYoutubeBot')
    TIKTOK_BOT_USERNAME = os.getenv('TIKTOK_BOT_USERNAME', 'KeepMediaBot')
    FACEBOOK_BOT_USERNAME = os.getenv('FACEBOOK_BOT_USERNAME', 'FacebookAsBot')
    TWITTER_BOT_USERNAME = os.getenv('TWITTER_BOT_USERNAME', 'twittervid_bot')
    
    # Database configuration
    DATABASE_PATH = os.getenv('DATABASE_PATH', './db/videos.db')
    
    # Logging configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # Admin configuration
    ADMIN_IDS = [
        int(admin_id.strip()) 
        for admin_id in os.getenv('ADMIN_IDS', '0').split(',') 
        if admin_id.strip().isdigit() and admin_id.strip() != '0'
    ]
    
    @classmethod
    def validate(cls) -> bool:
        """Validate that all required configuration values are set."""
        required_fields = [
            ('API_ID', cls.API_ID),
            ('API_HASH', cls.API_HASH),
            ('BOT_TOKEN', cls.BOT_TOKEN),
            ('STORAGE_CHANNEL_ID', cls.STORAGE_CHANNEL_ID),
        ]
        
        missing_fields = []
        for field_name, field_value in required_fields:
            if not field_value or (isinstance(field_value, int) and field_value == 0):
                missing_fields.append(field_name)
        
        if missing_fields:
            print(f"Missing required configuration fields: {', '.join(missing_fields)}")
            return False
        
        return True
