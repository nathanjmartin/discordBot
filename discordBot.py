#discord bot for my servers

import discord
import time

TOKEN = 'TOKEN'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bot'):
        msg = 'All commands include: \n\n!sup \n!time\n!content\n!yeet\n!join\n!leave'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!sup'):
        msg = 'Sup? {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!time'):
        msg = time.asctime(time.localtime(time.time()))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!content'):
        msg = 'CONTENNNNNNTTT {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!yeet'):
        msg = 'YEEEEEEET {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!join'):
        await joinServer(message.author.voice_channel)

    if message.content.startswith('!leave'):
        await leaveServer()
            
 #methods
async def joinServer(server):
    try:
        errorMsg = 'You are not in a channel!'
        if(server == None):
            await client.send_message(message.channel, errorMsg)
        await client.join_voice_channel(server)
    except:
        print('Something went wrong!')
        
        
async def leaveServer():
    msg = "I'm not in a server!"
    for x in client.voice_clients:
        if(x.server == None):
            return msg
        else:
            return await x.disconnect()
        
async def playFile():
    pass #have not finished yet



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')

client.run(TOKEN)
