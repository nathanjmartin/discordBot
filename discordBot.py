#discord bot for my servers

import discord
import time

TOKEN = 'NDY0Nzk1Mzk5NjIyODg1Mzg2.DiEU3g.Sz6sawcjd0OPVOeNMvJhiRK_Gmo'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bot'):
        msg = 'All commands include: \n\n!sup - hits u with the sup bitch\n!time - hits you with the time\n!content - shows u what its really all about\n!fuck will hit deep\n!join on\n!leave'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!sup'):
        msg = 'Sup Bitch? {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!time'):
        msg = time.asctime(time.localtime(time.time()))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!content'):
        msg = 'CONTENNNNNNTTT {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!fuck'):
        msg = 'No, fuk u {0.author.mention} u suck'.format(message)
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


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')

client.run(TOKEN)
