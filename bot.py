import os
import random
import requests
import json
import pyjokes

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

sad_words = ['sad',
 'depressed',
 'unhappy',
 'lonely',
 'lost',
 'isolated',
 'troubled',
 'hurt']
encourage_words = ['Hang in there',
'Don\'t give up',
'Keep pushing',
'Keep fighting!',
'Stay strong.',
'Never give up.',
'Never say \'die\'.',
'Come on! You can do it!.' ]
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_qoute = json.loads(response.text)
    quote = json_qoute[0]['q'] + ' -' + json_qoute[0]['a']
    return(quote)

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to help"))
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    user = message.author
    msg = str(message.content).lower()
    if message.author == client.user:
        return
    if msg == 'quote':
        await message.channel.send(get_quote())
    if msg == 'joke':
        await message.channel.send(pyjokes.get_joke())
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(encourage_words))
    if msg == 'hello' or msg == 'help':
        await message.channel.send(f'hey {user}, I am bot')
client.run(TOKEN)