import disband

client = disband.Client()


@client.event
async def on_ready():
    print('Client ready!')


@client.event
async def on_relationship_add(relationship):
    print('New', relationship.type, ':', relationship.user.name)


@client.event
async def on_relationship_update(old, new):
    print(old.type, ':', old.user.name, 'turned into', new.type)


@client.event
async def on_relationship_remove(relationship):
    print('Removed', relationship.type, ':', relationship.user.name)

client.run(open('token').read().strip(), bot=False)
