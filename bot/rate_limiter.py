"""Rate limiting functionality for the Discord bot"""

import time
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from config import Config

class RateLimiter:
    def __init__(self):
        # Store user usage data: {user_id: {'tier': str, 'usage': [(timestamp, count), ...]}}
        self.user_data: Dict[int, Dict] = {}
    
    def get_user_tier(self, user_id: int) -> str:
        """Get the tier for a user (default: free)"""
        if user_id not in self.user_data:
            self.user_data[user_id] = {
                'tier': Config.DEFAULT_TIER,
                'usage': []
            }
        return self.user_data[user_id]['tier']
    
    def set_user_tier(self, user_id: int, tier: str) -> bool:
        """Set the tier for a user"""
        if tier not in Config.RATE_LIMITS:
            return False
        
        if user_id not in self.user_data:
            self.user_data[user_id] = {
                'tier': tier,
                'usage': []
            }
        else:
            self.user_data[user_id]['tier'] = tier
        return True
    
    def _clean_old_usage(self, user_id: int):
        """Remove usage records older than 1 hour"""
        current_time = datetime.now()
        cutoff_time = current_time - timedelta(hours=1)
      
