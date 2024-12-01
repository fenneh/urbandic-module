"""
Test script for Urban Dictionary lookups
"""

import urllib.request
import json

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

def lookup_word(word, definition_index=0):
    """
    Look up a word on Urban Dictionary
    definition_index: 0 for first definition, 1 for second definition
    """
    if not word:
        return "Please provide a word to look up"
    
    url = f'http://api.urbandictionary.com/v0/define?term={word}'
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        
        try:
            definition = data['list'][definition_index]['definition']
            thumbsup = data['list'][definition_index]['thumbs_up']
            thumbsdown = data['list'][definition_index]['thumbs_down']
            
            result = f"Definition; {definition} >> Up {thumbsup} Down {thumbsdown}"
            return split_message(result)
            
        except (KeyError, IndexError):
            return ["No results found for this word"]
            
    except Exception as e:
        return [f"Error looking up word: {str(e)}"]

def test_lookup(word):
    """Test function to lookup a word and print both first and second definitions"""
    print(f"\nLooking up '{word}':")
    print("\nFirst definition:")
    for part in lookup_word(word, 0):
        print(f"[Part] {part}")
    
    print("\nSecond definition:")
    for part in lookup_word(word, 1):
        print(f"[Part] {part}")

if __name__ == "__main__":
    # Test the words
    test_words = ["mandem", "nandos"]
    
    for word in test_words:
        test_lookup(word)
