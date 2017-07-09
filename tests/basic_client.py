import disband

client = disband.Client()


@client.event
async def on_ready():
    print('Client ready!')

client.run(open('token').read().strip(), bot=False)
