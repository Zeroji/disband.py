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
