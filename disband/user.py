from discord.user import *
from discord.user import User as _User
del User


class User(_User):
    """Subclass of discord.user.User adding features.
    See User.__base__.__doc__ for more info."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.relationships = {}
