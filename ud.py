"""
ud.py - A communication tool to aid Europe and USA understand each other in #crude on irc.freenode.net
Copyright 2014, justFen
Licensed under the Eiffel Forum License 2.

http://justfen.com
"""

import re
from willie import web
from willie.module import commands, example
import urllib
import json

@commands('ud')
@example('.ud pussyole')
def ud_search(bot, trigger):
    query = trigger.group(2)
    url = 'http://api.urbandictionary.com/v0/define?term=%s' %(query)
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    definition = data['list'][0]['definition']
    thumbsup = data['list'][0]['thumbs_up']
    thumbsdown = data['list'][0]['thumbs_down']
    bot.reply('Definition: %s :: Upvotes: %s Downvotes: %s') % (definition,thumbsup,thumbsdown)