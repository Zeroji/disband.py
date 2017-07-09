from discord.enums import try_enum
from .enums import RelationshipType
from .user import User
import asyncio


class Relationship:
    """A relationship between two users."""

    def __init__(self, http, data):
        self._http = http
        self.type = try_enum(RelationshipType, data['type'])
        self.user = User(**data['user'])

    @asyncio.coroutine
    def accept(self):
        if self.type == RelationshipType.incoming_request:
            yield from self._http.add_relationship(self.user.id)

    @asyncio.coroutine
    def remove(self):
        yield from self._http.remove_relationship(self.user.id)
