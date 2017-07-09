Library Documentation
=====================

### **DISCLAIMER**

This library is **based on** discord.py, but modifies some behaviors which
makes it **not necessarily compliant** with Discord's library guidelines.
Misusing, or abusing, features provided by this library can result in
**termination of your account** without notice.

## Contents

- **[DISCLAIMER](#disclaimer)**
- [Contents](#contents)
- [User-Agent switcher](#user-agent-switcher)
- [Client methods](#client-methods)
  + [Blocking users](#blocking-users)
  + [Friends](#friends)
- [Client events](#client-events)
  + [Relationships](#relationships)
- [Miscellaneous](#miscellaneous)
  + [User](#user)
  + [Relationship](#relationship)

## User-Agent switcher

**PLEASE ENSURE YOU HAVE READ AND UNDERSTAND THE [DISCLAIMER](#disclaimer).**

Some endpoints of the Discord API have methods which can't be used by bots,
or libraries. As of now (2017-07-09), Discord uses the user-agent to detect
bots and libraries. Changing it can circumvent those limitations.

Disband.py has an integrated user-agent switcher, which is already present on
all necessary methods (see `@switch_agent` in the source). By default, it is
"disabled" by setting the alternative user-agent to the original one. [At your
own risk](#disclaimer), you can edit the alternative user-agent to enable the
user-agent switcher, and to use the full set of features:

```
client.http.alt_user_agent = 'Your custom User-Agent'
```

## Client methods

Those are regular client methods, like `send_message`.

### Blocking users

##### `block_user(user)`

This function requires *[switching user-agent](#user-agent-switcher)*.  
This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine)*.

Blocks the specified **`User`**.

**Parameters:**
- **user** (**`User`**) - The user to block

##### `unblock_user(user)`

This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine)*.

Unblocks the specified **`User`**.

**Parameters:**
- **user** (**`User`**) - The user to unblock

### Friends

##### `send_friend_request(user, [discriminator])`

This function requires *[switching user-agent](#user-agent-switcher)*.  
This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine)*.

Sends a friend request to the specified User, or to the specified
username#discriminator.

**Parameters:**  
- **user** (**`User`**) - The user to send a request to
- **discriminator** - `None`

**Parameters:**
- **user** (`str`) - The username to send a request to
- **discriminator** (`int` or digits string) - Their discriminator

##### `remove_friend(user)`

This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine)*.
 
Removes a friend. Doesn't error if they weren't your friend.

**Parameters:**
- **user** (**`User`**) - The user to remove from your friends

## Client events

Those are regular events, like `on_message`.

### Relationships

##### `on_relationship_add(new)`

Called when a relationship is created.

**Parameters:**
- **new** (**`Relationship`**) - The new relationship

##### `on_relationship_update(old, new)`

Called when a relationship is updated (like accepting a request).

**Parameters:**
- **old** (**`Relationship`**) - The old relationship
- **new** (**`Relationship`**) - The new relationship

##### `on_relationship_removed(new)`

Called when a relationship is removed.

**Parameters:**
- **old** (**`Relationship`**) - The old relationship

## Miscellaneous

### User

##### `user1.get_relationship(user2)`

Returns the relationship between two users, or `None`

**Parameters:**
- **user2** (**`User`**) - Target user

##### `user.friends`

Gives a list of **`User`**s the user is friends with.

##### `user.blocked`

Gives a list of **`User`**s the user has blocked.

##### `user.incoming_request`

Gives a list of **`Relationship`**s for incoming friend requests.

##### `user.outgoing_request`

Gives a list of **`Relationship`**s for outgoing friend requests.

### Relationship

##### `relationship.type`

The relationship type, as defined by **`RelationshipType`**
(see [the API doc](api.md#relationships))

##### `relationship.user`

The `User` on the other end of the relationship.

##### `relationship.accept()`

This function requires *[switching user-agent](#user-agent-switcher)*.  
This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine)*.

Accepts an incoming friend request.

##### `relationship.remove()`

This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine)*.

Removes a relationship. Depending on its type, this is equivalent to the
following actions:

type    | action
--------|-------
friend  | Remove friend
blocked | Unblock user
incoming_request | Ignore request
outgoing_request | Cancel request
