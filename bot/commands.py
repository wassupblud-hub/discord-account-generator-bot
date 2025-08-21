"""Discord bot commands for account generation"""

import discord
from discord.ext import commands
from discord import app_commands
from bot.rate_limiter import RateLimiter
from bot.generator import AccountGenerator
from config import Config

# Initialize components
rate_limiter = RateLimiter()
generator = AccountGenerator()

def setup_commands(bot):
    """Setup all bot commands"""
    
    @bot.tree.command(name='generate', description='Generate random accounts with usernames and passwords')
    @app_commands.describe(count='Number of accounts to generate (1-50)')
    async def generate_account(interaction: discord.Interaction, count: int = 1):
        """Generate one or more accounts"""
        user_id = interaction.user.id
        
        # Validate count
        if count < 1 or count > 50:
            await interaction.response.send_message('❌ Count must be between 1 and 50.', ephemeral=True)
            return
        
        # Check rate limit
        can_generate, error_message = rate_limiter.can_generate(user_id, count)
        if not can_generate:
            embed = discord.Embed(
                title='❌ Rate Limit Exceeded',
                description=error_message,
                color=Config.ERROR_COLOR
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
