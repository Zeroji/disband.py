import contextlib
from discord.http import *
from discord.http import HTTPClient as _HTTPClient
del HTTPClient


class HTTPClient(_HTTPClient):
    """Subclass of discord.http.HTTPClient adding features.
    See HTTPClient.__base__.__doc__ for more info."""

    def __init__(self, connector=None, *, loop=None):
        super().__init__(connector, loop=loop)
        self._user_agent = self.user_agent
        self.alt_user_agent = self.user_agent

    @contextlib.contextmanager
    def use_alt_agent(self):
        """Switch user agent to perform a request. Use at your own risk."""
        try:
            self.user_agent = self.alt_user_agent
            yield
        finally:
            self.user_agent = self._user_agent

    @switch_agent
    def block_user(self, user_id):
        r = Route('PUT', '/users/@me/relationships/{user_id}', user_id=user_id)
        payload = {'type': 2}
        return self.request(r, json=payload)

    def unblock_user(self, user_id):
        return self.request(Route('DELETE', '/users/@me/relationships/{user_id}', user_id=user_id))


# Decorator
def switch_agent(func):
    def switcher(self, *a, **kw):
        with self.use_alt_agent():
            yield from func(self, *a, **kw)
    return switcher
