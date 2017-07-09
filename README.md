disband.py
==========

[![PyPI](https://img.shields.io/pypi/v/disband.py.svg)](https://pypi.python.org/pypi/disband.py/)
[![PyPI](https://img.shields.io/pypi/pyversions/disband.py.svg)](https://pypi.python.org/pypi/disband.py/)
[![PyPI](https://img.shields.io/pypi/status/disband.py.svg)](https://pypi.python.org/pypi/disband.py/)
[![PyPI](https://img.shields.io/pypi/format/disband.py.svg)](https://pypi.python.org/pypi/disband.py/)

*It's discord.py, now with friends!*

This module is an extension of [discord.py](https://github.com/Rapptz/discord.py),
an API wrapper for Discord written in Python.

The aim of this module is to add methods and events for the undocumented
endpoints of Discord's API, for example relationships.

### Warning

This project is **not** meant to be used by bots, and doesn't guarantee
support for anything implying a bot token. It should only be used with
user tokens, which you can obtain through various methods.

Since this uses undocumented endpoints of the Discord API, some features
might give unexpected results, or break when the API changes.

> Please remember that Discord does *not* officially support "self-bots"
> in any way. You may *not* use this module to automate any kind of task
> on a user account, and Discord may ban your account if you do so.


## Installation

> This will automatically install discord.py for you. If you wish to install
> another version, or to install it yourself, please use the
> [official documentation](https://github.com/Rapptz/discord.py#installing)
> of discord.py, and then follow the steps below.

You can install disband.py via `pip`:

```
$ pip install -U disband.py
```

Alternatively, you can install it from source:

```
$ git clone https://github.com/Zeroji/disband.py
$ cd disband.py
$ pip install -U .
```

## Usage

Assuming you already use discord.py, you can simply replace

```python
import discord
```

with

```python
import disband as discord
```

> If you use `discord.__version__`, it will return the version of disband.py.
> To prevent this, disband.py has an attribute `__discord_version__` containing
> the real discord.py version (for example, 0.16.8).

## Requirements
- Python 3.4.2+
- `discord.py` library
