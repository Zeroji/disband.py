import contextlib
from discord.http import *
from discord.http import HTTPClient as _HTTPClient
del HTTPClient


# Decorator
def switch_agent(func):
    def switcher(self, *a, **kw):
        with self.use_alt_agent():
            yield from func(self, *a, **kw)
    return switcher


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
    def add_relationship(self, user_id, type=None):
        r = Route('PUT', '/users/@me/relationships/{user_id}', user_id=user_id)
        payload = {}
        if type is not None:
            payload['type'] = type
        return self.request(r, json=payload)

    def remove_relationship(self, user_id):
        return self.request(Route('DELETE', '/users/@me/relationships/{user_id}', user_id=user_id))

    @switch_agent
    def send_request(self, username, discriminator):
        r = Route('POST', '/users/@me/relationships')
        payload = {'username': username, 'discriminator': int(discriminator)}
        return self.request(r, json=payload)
