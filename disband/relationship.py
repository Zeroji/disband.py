from discord.enums import try_enum
from .enums import RelationshipType


class Relationship:
    """A relationship between two users."""

    def __init__(self, state, data):
        self._state = state
        self.type = try_enum(RelationshipType, data['type'])
        self.user = state.store_user(data['user'])
