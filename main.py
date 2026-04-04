import discord
import os
from dotenv import load_dotenv

load_dotenv() # Loading environment variables from .env

intents = discord.Intents.default() # Using default intents
intents.presences = True
intents.guilds = True
intents.message_content = True # Enabling message content intent which should also be set in developer portal

client = discord.Client(intents=intents) # Creating a Discord client with the specified intents

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}') # Print a message when the bot is ready

@client.event
async def on_message(message):
    if message.author == client.user:
        return # Ignore messages sent by the bot itself

    if message.content == '!hello':
        if message.author.name == "johnny.nyc1":
            await message.channel.send("Hello my creator!")
        await message.channel.send('Hello! I am a RAG Bot powered by OpenAI and Anthropic.') # Respond to !hello command

client.run(os.getenv("DISCORD_TOKEN") or "") #run this bot 