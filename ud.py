"""
ud.py - A communication tool to aid Europe and USA understand each other in #crude on irc.freenode.net
Licensed under the Eiffel Forum License 2.
"""

import re
from sopel import web
from sopel.module import commands, example
import urllib.request
import json
import sys

def split_message(message, max_length=400):
    """Split a message into multiple parts if it exceeds max_length."""
    parts = []
    while message:
        if len(message) <= max_length:
            parts.append(message)
            break
        
        # Find the last space before max_length
        split_point = message.rfind(' ', 0, max_length)
        if split_point == -1:  # No space found, force split at max_length
            split_point = max_length
        
        parts.append(message[:split_point])
        message = message[split_point:].lstrip()
    
    return parts

@commands('ud')
@example('.ud getme')
def ud_search(bot, trigger):
    query = trigger.group(2)
    if query is None:
        bot.reply('Please provide a word to look up')
        return
    if "spam" in query:
        bot.reply('Negative ghostrider')
        return
    
    url = 'http://api.urbandictionary.com/v0/define?term={}'.format(query)
    try:
        response = urllib.request.urlopen(url)
    except UnicodeError:
        bot.reply('ENGLISH MOTHERFUCKER, DO YOU SPEAK IT?')
        return
    
    data = json.loads(response.read().decode('utf-8'))
    try:
        definition = data['list'][0]['definition']
    except (KeyError, IndexError):
        bot.reply('No results, do you even spell brah?')
        return
    
    thumbsup = data['list'][0]['thumbs_up']
    thumbsdown = data['list'][0]['thumbs_down']
    udoutput = "Definition; {} >> Up {} Down {}".format(definition, thumbsup, thumbsdown)
    
    if "spam spam" in udoutput:
        bot.reply('Negative ghostrider')
        return
        
    # Split and send message in parts if needed
    message_parts = split_message(udoutput)
    for i, part in enumerate(message_parts, 1):
        if len(message_parts) > 1:
            bot.reply('[{}/{}] {}'.format(i, len(message_parts), part))
        else:
            bot.reply(part)

@commands('ud2')
@example('.ud2 getme')
def ud_search_1(bot, trigger):
    query = trigger.group(2)
    if query is None:
        bot.reply('Please provide a word to look up')
        return
    if "spam" in query:
        bot.reply('Negative ghostrider')
        return
    
    url = 'http://api.urbandictionary.com/v0/define?term={}'.format(query)
    try:
        response = urllib.request.urlopen(url)
    except UnicodeError:
        bot.reply('ENGLISH MOTHERFUCKER, DO YOU SPEAK IT?')
        return
    
    data = json.loads(response.read().decode('utf-8'))
    try:
        definition = data['list'][1]['definition']
    except (KeyError, IndexError):
        bot.reply('No results, do you even spell brah?')
        return
    
    thumbsup = data['list'][1]['thumbs_up']
    thumbsdown = data['list'][1]['thumbs_down']
    udoutput = "Definition; {} >> Up {} Down {}".format(definition, thumbsup, thumbsdown)
    
    if "spam spam" in udoutput:
        bot.reply('Negative ghostrider')
        return
        
    # Split and send message in parts if needed
    message_parts = split_message(udoutput)
    for i, part in enumerate(message_parts, 1):
        if len(message_parts) > 1:
            bot.reply('[{}/{}] {}'.format(i, len(message_parts), part))
        else:
            bot.reply(part)
