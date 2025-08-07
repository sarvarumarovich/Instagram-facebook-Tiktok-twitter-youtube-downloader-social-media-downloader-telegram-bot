"""Utility functions for the Telegram automation system."""

import re
from typing import Optional
from urllib.parse import urlparse

class URLValidator:
    """URL validation utilities for Instagram and YouTube."""
    
    # Instagram URL patterns - more flexible to catch various formats
    INSTAGRAM_PATTERNS = [
        r'https?://(?:www\.)?instagram\.com/p/[A-Za-z0-9_-]+/?',
        r'https?://(?:www\.)?instagram\.com/reel/[A-Za-z0-9_-]+/?',
        r'https?://(?:www\.)?instagram\.com/reels/[A-Za-z0-9_-]+/?',
        r'https?://(?:www\.)?instagram\.com/tv/[A-Za-z0-9_-]+/?',
        r'https?://(?:www\.)?instagram\.com/stories/[A-Za-z0-9_.]+/\d+/?',
    ]
    
    # YouTube URL patterns
    YOUTUBE_PATTERNS = [
        r'https?://(?:www\.)?youtube\.com/watch\?v=[A-Za-z0-9_-]+',
        r'https?://(?:www\.)?youtu\.be/[A-Za-z0-9_-]+',
        r'https?://(?:www\.)?youtube\.com/shorts/[A-Za-z0-9_-]+',
        r'https?://m\.youtube\.com/watch\?v=[A-Za-z0-9_-]+',
    ]
    
    # TikTok URL patterns
    TIKTOK_PATTERNS = [
        r'https?://(?:www\.)?tiktok\.com/@[A-Za-z0-9_.]+/video/\d+',
        r'https?://(?:vm|vt)\.tiktok\.com/[A-Za-z0-9]+/?',
        r'https?://(?:www\.)?tiktok\.com/t/[A-Za-z0-9]+/?',
        r'https?://m\.tiktok\.com/v/\d+',
    ]
    
    # Facebook URL patterns
    FACEBOOK_PATTERNS = [
        r'https?://(?:www\.)?facebook\.com/[A-Za-z0-9_.]+/videos/\d+/?(?:\?.*)?',
        r'https?://(?:www\.)?facebook\.com/watch/\?v=\d+',
        r'https?://(?:www\.)?facebook\.com/reel/\d+/?(?:\?.*)?',
        r'https?://(?:www\.)?fb\.watch/[A-Za-z0-9_-]+/?(?:\?.*)?',
        r'https?://m\.facebook\.com/story\.php\?story_fbid=\d+',
        r'https?://(?:www\.)?facebook\.com/share/v/[A-Za-z0-9]+/?',
        r'https?://(?:www\.)?facebook\.com/share/r/[A-Za-z0-9]+/?(?:\?.*)?',
        r'https?://(?:www\.)?facebook\.com/share/.+',
    ]
    
    # Twitter/X URL patterns
    TWITTER_PATTERNS = [
        r'https?://(?:www\.)?twitter\.com/[A-Za-z0-9_]+/status/\d+/?(?:\?.*)?',
        r'https?://(?:www\.)?x\.com/[A-Za-z0-9_]+/status/\d+/?(?:\?.*)?',
        r'https?://mobile\.twitter\.com/[A-Za-z0-9_]+/status/\d+/?(?:\?.*)?',
        r'https?://t\.co/[A-Za-z0-9]+/?(?:\?.*)?',
        r'https?://(?:www\.)?twitter\.com/i/web/status/\d+/?(?:\?.*)?',
        r'https?://(?:www\.)?x\.com/i/web/status/\d+/?(?:\?.*)?',
        # Additional patterns for various Twitter/X formats
        r'https?://(?:www\.)?twitter\.com/[A-Za-z0-9_.-]+/status/\d+/?(?:\?.*)?(?:#.*)?',
        r'https?://(?:www\.)?x\.com/[A-Za-z0-9_.-]+/status/\d+/?(?:\?.*)?(?:#.*)?',
        r'https?://m\.twitter\.com/[A-Za-z0-9_.-]+/status/\d+/?(?:\?.*)?',
        r'https?://mobile\.x\.com/[A-Za-z0-9_.-]+/status/\d+/?(?:\?.*)?',
        # Support for business accounts and other special accounts
        r'https?://(?:www\.)?twitter\.com/[A-Za-z0-9_.-]{1,15}/status/\d+/?(?:\?.*)?(?:#.*)?',
        r'https?://(?:www\.)?x\.com/[A-Za-z0-9_.-]{1,15}/status/\d+/?(?:\?.*)?(?:#.*)?',
    ]
    
    @classmethod
    def is_instagram_url(cls, url: str) -> bool:
        """
        Check if the URL is a valid Instagram URL.
        
        Args:
            url: URL to validate
            
        Returns:
            True if valid Instagram URL, False otherwise
        """
        if not url or not isinstance(url, str):
            return False
        
        # Clean the URL
        url = url.strip()
        
        # Check against patterns
        for pattern in cls.INSTAGRAM_PATTERNS:
            if re.match(pattern, url, re.IGNORECASE):
                return True
        
        return False
    
    @classmethod
    def is_youtube_url(cls, url: str) -> bool:
        """
        Check if the URL is a valid YouTube URL.
        
        Args:
            url: URL to validate
            
        Returns:
            True if valid YouTube URL, False otherwise
        """
        if not url or not isinstance(url, str):
            return False
        
        # Clean the URL
        url = url.strip()
        
        # Check against patterns
        for pattern in cls.YOUTUBE_PATTERNS:
            if re.match(pattern, url, re.IGNORECASE):
                return True
        
        return False
    
    @classmethod
    def is_tiktok_url(cls, url: str) -> bool:
        """
        Check if the URL is a valid TikTok URL.
        
        Args:
            url: URL to validate
            
        Returns:
            True if valid TikTok URL, False otherwise
        """
        if not url or not isinstance(url, str):
            return False
        
        # Clean the URL
        url = url.strip()
        
        # Check against patterns
        for pattern in cls.TIKTOK_PATTERNS:
            if re.match(pattern, url, re.IGNORECASE):
                return True
        
        return False
    
    @classmethod
    def is_facebook_url(cls, url: str) -> bool:
        """
        Check if the URL is a valid Facebook URL.
        
        Args:
            url: URL to validate
            
        Returns:
            True if valid Facebook URL, False otherwise
        """
        if not url or not isinstance(url, str):
            return False
        
        # Clean the URL
        url = url.strip()
        
        # Check against patterns
        for pattern in cls.FACEBOOK_PATTERNS:
            if re.match(pattern, url, re.IGNORECASE):
                return True
        
        return False
    
    @classmethod
    def is_twitter_url(cls, url: str) -> bool:
        """
        Check if the URL is a valid Twitter/X URL.
        
        Args:
            url: URL to validate
            
        Returns:
            True if valid Twitter/X URL, False otherwise
        """
        if not url or not isinstance(url, str):
            return False
        
        # Clean the URL
        url = url.strip()
        
        # Check against patterns
        for pattern in cls.TWITTER_PATTERNS:
            if re.match(pattern, url, re.IGNORECASE):
                return True
        
        return False
    
    @classmethod
    def is_valid_url(cls, url: str) -> bool:
        """
        Check if the URL is a valid Instagram, YouTube, TikTok, Facebook or Twitter URL.
        
        Args:
            url: URL to validate
            
        Returns:
            True if valid URL, False otherwise
        """
        return cls.is_instagram_url(url) or cls.is_youtube_url(url) or cls.is_tiktok_url(url) or cls.is_facebook_url(url) or cls.is_twitter_url(url)
    
    @classmethod
    def get_url_type(cls, url: str) -> Optional[str]:
        """
        Get the type of URL (instagram, youtube, tiktok, facebook or twitter).
        
        Args:
            url: URL to check
            
        Returns:
            'instagram', 'youtube', 'tiktok', 'facebook', 'twitter' or None if invalid
        """
        if cls.is_instagram_url(url):
            return 'instagram'
        elif cls.is_youtube_url(url):
            return 'youtube'
        elif cls.is_tiktok_url(url):
            return 'tiktok'
        elif cls.is_facebook_url(url):
            return 'facebook'
        elif cls.is_twitter_url(url):
            return 'twitter'
        return None
    
    @classmethod
    def normalize_url(cls, url: str) -> Optional[str]:
        """
        Normalize URL by removing tracking parameters and fragments.
        
        Args:
            url: URL to normalize
            
        Returns:
            Normalized URL or None if invalid
        """
        if not cls.is_valid_url(url):
            return None
        
        try:
            url = url.strip()
            
            # For YouTube URLs, keep the necessary query parameters (v parameter)
            if cls.is_youtube_url(url):
                parsed = urlparse(url)
                if 'youtube.com' in parsed.netloc and '/watch' in parsed.path:
                    # Extract video ID from query parameters
                    from urllib.parse import parse_qs
                    query_params = parse_qs(parsed.query)
                    if 'v' in query_params:
                        video_id = query_params['v'][0]
                        return f"https://www.youtube.com/watch?v={video_id}"
                elif 'youtu.be' in parsed.netloc:
                    # Extract video ID from path
                    video_id = parsed.path.lstrip('/')
                    return f"https://www.youtube.com/watch?v={video_id}"
                # For shorts and other formats, just normalize the domain and path
                return f"https://www.youtube.com{parsed.path}"
            
            # For TikTok URLs, remove query parameters and fragments
            elif cls.is_tiktok_url(url):
                parsed = urlparse(url)
                normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                # Remove trailing slash
                normalized = normalized.rstrip('/')
                return normalized
            
            # For Facebook URLs, handle different formats
            elif cls.is_facebook_url(url):
                parsed = urlparse(url)
                # For facebook.com/watch?v= URLs, keep the v parameter
                if 'facebook.com/watch' in url and 'v=' in parsed.query:
                    from urllib.parse import parse_qs
                    query_params = parse_qs(parsed.query)
                    if 'v' in query_params:
                        video_id = query_params['v'][0]
                        return f"https://www.facebook.com/watch/?v={video_id}"
                # For other Facebook URLs, remove query parameters and fragments
                normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                normalized = normalized.rstrip('/')
                return normalized
            
            # For Twitter URLs, remove query parameters and fragments
            elif cls.is_twitter_url(url):
                parsed = urlparse(url)
                normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                normalized = normalized.rstrip('/')
                return normalized
            
            # For Instagram URLs, remove query parameters and fragments
            else:
                parsed = urlparse(url)
                normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                # Remove trailing slash
                normalized = normalized.rstrip('/')
                return normalized
                
        except Exception:
            return None
    
    @classmethod
    def extract_urls_from_text(cls, text: str) -> list[str]:
        """
        Extract all valid URLs from text.
        
        Args:
            text: Text to search for URLs
            
        Returns:
            List of found URLs
        """
        if not text:
            return []
        
        # First try to find all http/https URLs in the text using a general pattern
        general_url_pattern = r'https?://[^\s]+'
        potential_urls = re.findall(general_url_pattern, text, re.IGNORECASE)
        
        # Then check each potential URL against our specific patterns
        urls = []
        for url in potential_urls:
            # Clean up the URL (remove trailing punctuation that might be captured)
            url = url.rstrip('.,!?;:)')
            
            # Check if it's a valid social media URL
            if cls.is_valid_url(url):
                urls.append(url)
        
        # Normalize and deduplicate
        normalized_urls = []
        for url in urls:
            normalized = cls.normalize_url(url)
            if normalized and normalized not in normalized_urls:
                normalized_urls.append(normalized)
        
        return normalized_urls
    
    @classmethod
    def extract_instagram_username_from_url(cls, url: str) -> Optional[str]:
        """
        Extract Instagram username from URL if available.
        
        Args:
            url: Instagram URL
            
        Returns:
            Username without @ symbol, or None if not found or not available
        """
        if not cls.is_instagram_url(url):
            return None
        
        try:
            parsed = urlparse(url.strip())
            path_parts = parsed.path.strip('/').split('/')
            
            # Handle different Instagram URL patterns:
            # /stories/USERNAME/STORY_ID/ -> USERNAME is at index 1
            if len(path_parts) >= 2 and path_parts[0] == 'stories':
                username = path_parts[1]
                # Basic username validation
                if re.match(r'^[a-zA-Z0-9_.]{1,30}$', username):
                    return username.lower()
            
            # Post/Reel/TV URLs (/p/, /reel/, /tv/) don't contain usernames
            # so we return None for these
            
            return None
            
        except Exception:
            return None


def format_duration(seconds: int) -> str:
    """
    Format duration in seconds to human-readable format.
    
    Args:
        seconds: Duration in seconds
        
    Returns:
        Formatted duration string
    """
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes}m {remaining_seconds}s"
    else:
        hours = seconds // 3600
        remaining_minutes = (seconds % 3600) // 60
        return f"{hours}h {remaining_minutes}m"


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename by removing invalid characters.
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    # Remove invalid characters for Windows/Unix
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Remove leading/trailing spaces and dots
    filename = filename.strip(' .')
    
    # Ensure filename is not empty
    if not filename:
        filename = "unnamed_file"
    
    return filename


def extract_instagram_username(url: str) -> Optional[str]:
    """
    Extract Instagram username from URL.
    
    Args:
        url: Instagram URL
        
    Returns:
        Username without @ symbol, or None if not found
    """
    if not url or not isinstance(url, str):
        return None
    
    try:
        from urllib.parse import urlparse
        parsed = urlparse(url.strip())
        
        if 'instagram.com' not in parsed.netloc:
            return None
        
        path_parts = parsed.path.strip('/').split('/')
        
        # Handle different Instagram URL patterns:
        # /p/POST_ID/ -> No username available in these URLs
        # /reel/REEL_ID/ -> No username available in these URLs  
        # /tv/TV_ID/ -> No username available in these URLs
        # /stories/USERNAME/STORY_ID/ -> USERNAME is at index 1
        # /USERNAME/ -> USERNAME is at index 0 (profile URLs)
        
        if len(path_parts) >= 2:
            if path_parts[0] == 'stories':
                # stories/username/story_id format
                return path_parts[1].lower()
            elif path_parts[0] in ['p', 'reel', 'reels', 'tv']:
                # Post/Reel/TV URLs don't contain username
                return None
            else:
                # Could be a profile URL like /username/
                username = path_parts[0]
                # Basic username validation
                if re.match(r'^[a-zA-Z0-9_.]{1,30}$', username):
                    return username.lower()
        
        return None
        
    except Exception:
        return None
