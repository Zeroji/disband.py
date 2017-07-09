"""Simple user blocking example.

Will block anyone saying "block me", and unblock anyone saying "unblock me"."""

import disband
client = disband.Client()


@client.event
async def on_ready():
    # client.http.alt_user_agent = ''  # Use at your own risk
    print('Client ready!')


@client.event
async def on_message(message):
    if message.content.lower() == 'block me':
        print('Blocking', message.author.name)
        await client.block_user(message.author)
    if message.content.lower() == 'unblock me':
        print('Unblocking', message.author.name)
        await client.unblock_user(message.author)

client.run(open('token').read().strip(), bot=False)
