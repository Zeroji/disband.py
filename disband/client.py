from discord.client import *
from discord.client import Client as _Client
from .http import HTTPClient
del Client


class Client(_Client):
    """Subclass of discord.Client adding features.
    See Client.__base__.__doc__ for more info."""

    def __init__(self, *, loop=None, **options):
        connector = options.get('connector', None)  # super().__init__ uses options.pop
        super().__init__(loop=loop, **options)
        self.http.session.close()  # closing previous session
        self.http = HTTPClient(connector, loop=self.loop)  # creating new session

    @asyncio.coroutine
    def block_user(self, user):
        if not isinstance(user, User):
            raise InvalidArgument('user argument must be a User')
        print('blocking user')
        yield from self.http.block_user(user.id)

    @asyncio.coroutine
    def unblock_user(self, user):
        if not isinstance(user, User):
            raise InvalidArgument('user argument must be a User')
        yield from self.http.unblock_user(user.id)
