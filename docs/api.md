API Documentation
=================

### **DISCLAIMER**

This documentation is **not** official, and **not** affiliated in any way to
Hammer & Chisel, Inc. or Discord.

The information contained here was obtained mostly through request inspection
and gateway logging, **may be incorrect** and should only be used **at your
own risk**.

## Contents

- **[DISCLAIMER](#disclaimer)**
- [Contents](#contents)
- [Relationships](#relationships)
  + [Summary of endpoints](#summary-of-endpoints)
  + [Get relationships](#get-relationships)
  + [Send a friend request](#send-a-friend-request)
  + [Cancel a friend request](#cancel-a-friend-request)
  + [Accept a friend request](#accept-a-friend-request)
  + [Ignore a friend request](#ignore-a-friend-request)
  + [Block a user](#block-a-user)
  + [Unblock a user](#unblock-a-user)
  + [Remove a friend](#remove-a-friend)

## Relationships

Relationships can exist between two users.
There are four types of relationships: friendships, blocked users, and
incoming/outgoing friend requests.
Bots cannot have friends, but can be blocked.

Relationship types:

value | description
------|------------
1     | Friend
2     | Blocked user
3     | Friend request (incoming)
4     | Friend request (outgoing)

### Summary of endpoints

#### `/users/@me/relationships`

- **GET** - Get list of relationships
- **POST** - Send friend request to user#discriminator

#### `/users/@me/relationships/{user_id}`

- **PUT** - Create a relationship (payload: `type` = `2` or `4`)
- **PATCH** - Accept an incoming friend request
- **DELETE** - Remove a relationship (won't error if none)

### Get relationships

**GET** `/users/@me/relationships`

Returns a list of relationships. Relationship details:

field | type | description
------|------|------------
type  | int  | Relationship type
id    | ID   | ID of the user on the other end
user  | User | User on the other end

### Send a friend request

**POST** `/users/@me/relationships`

Send someone a friend request. This will add an outgoing friend request to your
relationships, and an incoming friend request to theirs.

Payload:

field         | type   | description
--------------|--------|------------
username      | string | username of the user to add
discriminator | string | discriminator of the user to add

> This will return a 400 error if the target user does not exist, or is a bot

### Cancel a friend request

**DELETE** `/users/@me/relationships/{user_id}`

Cancel an outgoing friend request. This will remove it from your relationships,
and remove the incoming friend request from theirs (if any).

### Accept a friend request

**PATCH** `/users/@me/relationships/{user_id}`

This will turn a friend request into a friendship, on both sides.

Payload: `{}`

### Ignore a friend request

**DELETE** `/users/@me/relationships/{user_id}`

This will remove an incoming friend request from your relationships, **but** it
will still appear as an outgoing friend request on the sender's end.

### Block a user

**PUT** `/users/@me/relationships/{user_id}`

This will add a user to your list of blocked users.

Payload:

field | type | description | value
------|------|-------------|------
type  | int  | Relationship status | 2 (blocked)

> Note: it is possible to send a friend request through this, by changing the
> payload `type` to `4`

### Unblock a user

**DELETE** `/users/@me/relationships/{user_id}`

This will unblock a previously blocked user.

### Remove a friend

**DELETE** `/users/@me/relationships/{user_id}`

This will remove a friendship, on both sides. Much sad.
