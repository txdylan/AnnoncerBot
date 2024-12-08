import discord
import asyncio
import logging
import os
from dotenv import load_dotenv

# Load the bot token from a .env file for security
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # Make sure to store the token in a .env file

# Suppress INFO logs from the discord library
logging.getLogger('discord').setLevel(logging.WARNING)

# Define the required intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

# Create a client instance with intents
client = discord.Client(intents=intents)

# Event when the bot is ready
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
    # Get the channel by ID (replace with your actual channel ID)
    channel = await client.fetch_channel(Channel ID)  # Channel ID

    # Start an asynchronous task to handle terminal input
    asyncio.create_task(handle_terminal_input(channel))

# Function to handle terminal input
async def handle_terminal_input(channel):
    while True:
        # Use asyncio to non-blocking wait for input
        message = await asyncio.to_thread(input, "Enter message to send to Discord (type 'exit' to stop): ")

        if message.lower() == 'exit':
            print("Exiting bot...")
            await client.close()  # Close the bot connection
            break
        
        if message:
            # Send the message to the channel
            await channel.send(message)
            print(f"Sent message: {message}")
        else:
            print("No message entered. Try again.")

# Run the bot using the token
client.run(TOKEN)  # Token is securely loaded from the .env file
