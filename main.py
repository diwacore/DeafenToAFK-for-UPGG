import os
import discord
from discord.ext import commands

# Define the intents necessary for the bot to function
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.voice_states = True
intents.members = True
intents.presences = True

# Create the bot instance with the specified intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event listener for when the bot is ready and operational
@bot.event
async def on_ready():
    print('Discord bot is now online')

# Event listener for voice state updates
@bot.event
async def on_voice_state_update(member, before, after):
    # Check if the member has deafened themselves
    if not before.self_deaf and after.self_deaf:
        print('User has deafened')
        # Move the member to the AFK channel
        afk_channel = member.guild.get_channel(1231230478741274684)  # Replace with your AFK channel ID
        await member.move_to(afk_channel)

# Run the bot with your token
bot.run(os.getenv('TOKEN'))  # Replace 'YOUR_BOT_TOKEN' with your actual token
