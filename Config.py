"""Configuration settings for the Discord bot"""

class Config:
    # Rate limiting configuration (generations per hour)
    RATE_LIMITS = {
        'free': 10,
        'pro': 100,
        'premium': float('inf')  # Unlimited
    }
    
    # Default user tier
    DEFAULT_TIER = 'free'
    
    # Username generation settings
    USERNAME_PREFIX = 'Engaged-alt'
    USERNAME_SUFFIX_LENGTH = 6  # For random numbers
    
    # Password generation settings
    PASSWORD_LENGTH = 16
    PASSWORD_WORDS = [
        'apple', 'beach', 'cloud', 'dream', 'eagle', 'flame', 'green', 'happy',
        'ice', 'jump', 'king', 'light', 'moon', 'night', 'ocean', 'peace',
        'quick', 'river', 'stone', 'tiger', 'unity', 'voice', 'wind', 'youth',
        'zero', 'brave', 'charm', 'dance', 'energy', 'focus', 'grace', 'hope',
        'inspire', 'joy', 'kind', 'love', 'magic', 'nature', 'open', 'power'
    ]
    
    # Bot settings
    EMBED_COLOR = 0x00ff00  # Green
    ERROR_COLOR = 0xff0000  # Red
