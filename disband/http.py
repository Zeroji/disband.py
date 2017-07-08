from discord.http import *
from discord.http import HTTPClient as SuperHTTPClient
del HTTPClient


class HTTPClient(SuperHTTPClient):
    """Subclass of discord.http.HTTPClient adding features.
    See HTTPClient.__base__.__doc__ for more info."""

    def __init__(self, connector=None, *, loop=None):
        super().__init__(connector, loop=loop)
