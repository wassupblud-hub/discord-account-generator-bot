import discord
from discord.ext import commands
import asyncio
import os
from config import Config
from bot.commands import setup_commands

# Configure bot intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guilds')
    
    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'Command is on cooldown. Try again in {error.retry_after:.2f} seconds.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing required argument. Use `!help` for command usage.')
    else:
        await ctx.send(f'An error occurred: {str(error)}')

# Setup commands
setup_commands(bot)

if __name__ == '__main__':
    # Get bot token from environment variable
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print('Error: DISCORD_BOT_TOKEN environment variable not set')
        exit(1)
    
    # Run the bot
    bot.run(token)
