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
        msg = 'All commands include: \n\n!sup \n!time\n!content\n!fuck\n!join\n!leave'
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
        chan = message.author.voice_channel
        await client.join_voice_channel(chan)

    if message.content.startswith('!leave'):
        msg = "I'm not in a server!"
        for x in client.voice_clients:
            if(x.server is None):
                return
            else:
                return await x.disconnect()



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')

client.run(TOKEN)
