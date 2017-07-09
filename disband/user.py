from discord.user import *
from discord.user import User as _User
from .enums import RelationshipType
del User


class User(_User):
    """Subclass of discord.user.User adding features.
    See User.__base__.__doc__ for more info."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.relationships = {}

    def get_relationship(self, user):
        """Return a relationship with a user if any, else None."""
        return self.relationships.get(user.id)

    @property
    def friends(self):
        return [r.user for r in self.relationships.values() if r.type == RelationshipType.friend]

    @property
    def blocked(self):
        return [r.user for r in self.relationships.values() if r.type == RelationshipType.blocked]

    @property
    def incoming_requests(self):
        return [r for r in self.relationships.values() if r.type == RelationshipType.incoming_request]

    @property
    def outgoing_requests(self):
        return [r for r in self.relationships.values() if r.type == RelationshipType.outgoing_request]
