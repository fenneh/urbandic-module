# urbandic-module

Python module for use with the Sopel IRC bot (formerly known as Willie) @ https://sopel.chat

# What does it do?

Simply, throw a word at it using the `.ud` command and you'll get the top definition back from http://www.urbandictionary.com/. Use `.ud2` to get the second definition.

## But whyyyy?

This was knocked together to help the yanks understand the brits in #crude on irc.freenode.net. Getme bruv.

# Version Compatibility

- Python 3.x compatible
- Works with Sopel IRC bot (formerly Willie)

# How to install?

1. Clone the python module to the modules folder for your Sopel install. This will usually be:
   - Linux: `~/.sopel/modules`
   - Windows: `%APPDATA%\sopel\modules`
2. Make sure your `default.cfg` file (Same dir) contains the line:
   - Linux: `extra = ~/.sopel/modules`
   - Windows: `extra = %APPDATA%\sopel\modules`

# Commands

- `.ud <word>` - Get the top Urban Dictionary definition
- `.ud2 <word>` - Get the second most popular definition
