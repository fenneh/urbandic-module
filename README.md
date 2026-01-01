# urbandic-module

Urban Dictionary module for Sopel IRC bot. Built to help Americans understand British slang in IRC channels.

## Commands

- `.ud <word>` - Get the top Urban Dictionary definition
- `.ud2 <word>` - Get the second definition (for when the first one is too spicy)

## Installation

1. Clone to your Sopel modules folder:
   - Linux: `~/.sopel/modules`
   - Windows: `%APPDATA%\sopel\modules`

2. Add to `default.cfg`:
   ```
   extra = ~/.sopel/modules
   ```

## Requirements

- Python 3.x
- Sopel IRC bot
