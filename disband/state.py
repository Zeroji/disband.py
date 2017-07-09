from discord.state import *
from discord.state import ConnectionState as _ConnectionState
from .user import User
from .relationship import Relationship
del ConnectionState


class ConnectionState(_ConnectionState):
    """Subclass of discord.state.ConnectionState adding features.
    See ConnectionState.__base__.__doc__ for more info."""

    def __init__(self, dispatch, chunker, syncer, max_messages, *, loop, http):
        super().__init__(dispatch, chunker, syncer, max_messages, loop=loop)
        self.http = http

    def parse_ready(self, data):
        super().parse_ready(data)
        self.user = User(**data['user'])
        for relationship in data['relationships']:
            self.user.relationships[relationship['id']] = Relationship(self.http, relationship)

    def parse_relationship_add(self, data):
        key = data['id']
        old = self.user.relationships.get(key)
        if old is not None:
            self.user.relationships.pop(key)
        new = Relationship(self.http, data)
        self.user.relationships[data['id']] = new
        if old is not None:
            self.dispatch('relationship_update', old, new)
        else:
            self.dispatch('relationship_add', new)

    def parse_relationship_remove(self, data):
        key = data['id']
        old = self.user.relationships.get(key)
        if old is not None:
            self.user.relationships.pop(key)
            self.dispatch('relationship_remove', old)
