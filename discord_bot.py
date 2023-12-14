import discord
import os
import random
from ec2_metadata import ec2_metadata

from dotenv import load_dotenv

print(ec2_metadata.region)
print(ec2_metadata.instance_id)

load_dotenv()

client = discord.Client()
token = str(os.getenv('TOKEN'))

@client.event 
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    
    
    print(f'Message {user_message} by {username} on {channel}')

    
    if message.author == client.user:
        return 
    
    
    if channel == "discord-bot":
        if user_message.lower() == "hello world" or user_message.lower() == "drink boba?":
            await message.channel.send(f"hello")
            return 
        
        elif user_message.lower() == "what is this server for?":
            await message.channel.send(f'prototyping an automated Discord bot that can serve data from the service hosted on EC2  {username}')
            
         
        elif user_message.lower() == "tell me about your server":
            await message.channel.send(f"Your instance data is\nregion:{ec2_metadata.region}\nip address:{ec2_metadata.public_ipv4}\navailability zone:{ec2_metadata.availability_zone}\n")
            
        

client.run(token)






