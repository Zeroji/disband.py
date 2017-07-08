from discord.client import *
from discord.client import Client as SuperClient
from .http import HTTPClient
del Client


class Client(SuperClient):
    """Subclass of discord.Client adding features.
    See Client.__base__.__doc__ for more info."""

    def __init__(self, *, loop=None, **options):
        connector = options.get('connector', None)  # super().__init__ uses options.pop
        super().__init__(loop=loop, **options)
        self.http.session.close()  # closing previous session
        self.http = HTTPClient(connector, loop=self.loop)  # creating new session
