from discord.enums import try_enum
from .enums import RelationshipType
from .user import User


class Relationship:
    """A relationship between two users."""

    def __init__(self, state, data):
        self._state = state
        self.type = try_enum(RelationshipType, data['type'])
        self.user = User(**data['user'])
