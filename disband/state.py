from discord.state import *
from discord.state import ConnectionState as _ConnectionState
from .user import User
del ConnectionState


class ConnectionState(_ConnectionState):
    """Subclass of discord.state.ConnectionState adding features.
    See ConnectionState.__base__.__doc__ for more info."""

    def __init__(self, dispatch, chunker, syncer, max_messages, *, loop):
        super().__init__(dispatch, chunker, syncer, max_messages, loop=loop)

    def parse_ready(self, data):
        super().parse_ready(data)
        self.user = User(**data['user'])

    def parse_relationship_add(self, data):
        # TODO
        pass

    def parse_relationship_remove(self, data):
        # TODO
        pass
