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
@example('.ud getme')
def ud_search(bot, trigger):
    query = trigger.group(2)
    url = 'http://api.urbandictionary.com/v0/define?term=%s' %(query)
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    try:
      definition = data['list'][0]['definition']
    except KeyError:
      bot.say('Something went wrong brah')
    except IndexError:
      bot.say('No results, do you even spell brah?')
    except UnicodeError:
      bot.say('(╯°□°）╯︵ ┻━┻) ASCII ONLY!!!!')
    else:
      thumbsup = data['list'][0]['thumbs_up']
      thumbsdown = data['list'][0]['thumbs_down']
      udoutput = "Definition; %s >> Up %s Down %s" % (definition,thumbsup,thumbsdown)
      bot.reply(udoutput)
