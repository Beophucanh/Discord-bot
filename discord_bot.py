#Import libraries for discord bot, os, and ec2 metadata. 
import discord
import os
import random
from ec2_metadata import ec2_metadata

from dotenv import load_dotenv

#To print ec2 metadata region and instance ID 
print(ec2_metadata.region)
print(ec2_metadata.instance_id)

#This to load environment from a .env file 
load_dotenv()

#Create a discord client and get token from the discord bot in the environment 
client = discord.Client()
token = str(os.getenv('TOKEN'))

#Notify that when the bot is ready and also print a message as the bot is logged in 
@client.event 
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

#Notify when a message is recieved and extract information from the message 
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    
    #Print information for received message 
    print(f'Message {user_message} by {username} on {channel}')

    #Ignore messages sent by the bot 
    if message.author == client.user:
        return 
    
    #Check if the message is in the discord server
    if channel == "discord-bot":
        #To respond to the message "hello world" or "drink boba" as all in lower case 
        if user_message.lower() == "hello world" or user_message.lower() == "drink boba?":
            #Respond for those message prompted above
            await message.channel.send(f"hello")
            return 
        #To respond for another message, specifically "what is this server for?"
        elif user_message.lower() == "what is this server for?":
            #The respond for question above
            await message.channel.send(f'prototyping an automated Discord bot that can serve data from the service hosted on EC2  {username}')
            
         #To respond for a message "tell me about your server"
        elif user_message.lower() == "tell me about your server":
            #The respond for the message above
            await message.channel.send(f"Your instance data is\nregion:{ec2_metadata.region}\nip address:{ec2_metadata.public_ipv4}\navailability zone:{ec2_metadata.availability_zone}\n")
            
        
#To run the bot with provided token from the beginning
client.run(token)






