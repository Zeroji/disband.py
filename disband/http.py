from discord.http import *
from discord.http import HTTPClient as _HTTPClient
del HTTPClient


class HTTPClient(_HTTPClient):
    """Subclass of discord.http.HTTPClient adding features.
    See HTTPClient.__base__.__doc__ for more info."""

    def __init__(self, connector=None, *, loop=None):
        super().__init__(connector, loop=loop)

    def block_user(self, user_id):
        r = Route('PUT', '/users/@me/relationships/{user_id}', user_id=user_id)
        payload = {'type': 2}
        return self.request(r, json=payload)

    def unblock_user(self, user_id):
        return self.request(Route('DELETE', '/users/@me/relationships/{user_id}', user_id=user_id))
