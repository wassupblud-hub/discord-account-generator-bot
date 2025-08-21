"""Username and password generation functionality"""

import secrets
import string
import random
from config import Config

class AccountGenerator:
    def __init__(self):
        self.number_chars = string.digits
        self.password_words = Config.PASSWORD_WORDS
    
    def generate_username(self) -> str:
        """Generate a random username like 'Engaged-alt123456'"""
        random_number = ''.join(secrets.choice(self.number_chars) 
                               for _ in range(Config.USERNAME_SUFFIX_LENGTH))
        return f"{Config.USERNAME_PREFIX}{random_number}"
    
    def generate_password(self) -> str:
        """Generate a random password using words and numbers"""
        # Pick 2-3 random words
        num_words = secrets.randbelow(2) + 2  # 2 or 3 words
        selected_words = [secrets.choice(self.password_words) for _ in range(num_words)]
        
        # Add some random numbers
        numbers = ''.join(secrets.choice(string.digits) for _ in range(3))
        
        # Combine words with numbers and capitalize first letters
        password_parts = [word.capitalize() for word in selected_words]
        password_parts.append(numbers)
        
        return ''.join(password_parts)
    
    def generate_account(self) -> dict:
        """Generate a complete account with username and password"""
        return {
            'username': self.generate_username(),
            'password': self.generate_password()
        }
    
    def generate_multiple_accounts(self, count: int) -> list:
        """Generate multiple accounts"""
        return [self.generate_account() for _ in range(count)]
      
