from discord.client import *
from discord.client import Client as _Client
from .enums import RelationshipType
from .http import HTTPClient
from .state import ConnectionState
del Client


class Client(_Client):
    """Subclass of discord.Client adding features.
    See Client.__base__.__doc__ for more info."""

    def __init__(self, *, loop=None, **options):
        connector = options.get('connector', None)  # super().__init__ uses options.pop
        super().__init__(loop=loop, **options)
        self.http.session.close()  # closing previous session
        self.http = HTTPClient(connector, loop=self.loop)  # creating new session
        max_messages = self.connection.max_messages  # creating new connection state
        self.connection = ConnectionState(self.dispatch, self.request_offline_members,
                                          self._syncer, max_messages, loop=self.loop)

    @asyncio.coroutine
    def block_user(self, user):
        if not isinstance(user, User):
            raise InvalidArgument('user argument must be a User')
        print('blocking user')
        yield from self.http.add_relationship(user.id, RelationshipType.blocked)

    @asyncio.coroutine
    def unblock_user(self, user):
        if not isinstance(user, User):
            raise InvalidArgument('user argument must be a User')
        yield from self.http.remove_relationship(user.id)
