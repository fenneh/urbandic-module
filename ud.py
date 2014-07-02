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
import sys

@commands('ud')
@example('.ud getme')
def ud_search(bot, trigger):
    query = trigger.group(2)
    if "spam" in query:
      bot.reply('Negative ghostrider')
      exit(0)
    else:
      url = 'http://api.urbandictionary.com/v0/define?term=%s' %(query)
    try:
      response = urllib.urlopen(url)
    except UnicodeError:
      bot.reply('ENGLISH MOTHERFUCKER, DO YOU SPEAK IT?')
      exit(0)
    else:
      data = json.loads(response.read())
    try:
      definition = data['list'][0]['definition']
    except KeyError:
      bot.reply('Something went wrong brah')
    except IndexError:
      bot.reply('No results, do you even spell brah?')
    else:
      thumbsup = data['list'][0]['thumbs_up']
      thumbsdown = data['list'][0]['thumbs_down']
      udoutput = "Definition; %s >> Up %s Down %s" % (definition,thumbsup,thumbsdown)
      if not "spam spam" in udoutput:
          bot.reply(udoutput)
      else:
          bot.reply('Negative ghostrider')
