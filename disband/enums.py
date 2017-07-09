from enum import Enum


class RelationshipType(Enum):
    friend = 1
    blocked = 2
    incoming_request = 3
    outgoing_request = 4
