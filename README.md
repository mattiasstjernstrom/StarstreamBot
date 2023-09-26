# 💫🤖 StarstreamBot!


#### Video Demo:  <URL HERE>
#### Description:
_StarstreamBot_ is a "dictionary bot" built in Python as a hobby project. The bot is based on the Levenshtein distance algorithm and works like this: it takes a string that you, as a user, search for and compares it with the string in the database. The higher the similarity, the more likely the user means that specific part of the dictionary. This algorithm also allows for some degree of misspelling and the inclusion of words that might not be in the dictionary but can still find the correct word.

Currently, I have a test word-list containing Python's built-in functions, syntax, and error messages for testing purposes.

## Setup:
* Make a bot at [``Discord developer portal``](https://discord.com/developers/applications/)
* Copy ``channel-ID`` and ``Bot_token``
* Make a file named: ``discord_key.py`` (or use dotenv) and use copy this:
```py
def discord_key():
    return "<discord_key>"
```
* Change ``channel_id`` in app.py
* Invite bot to your channel
* Run ``app.py`` ➡️ Happy botting!
## Author:
- Mattias Stjernström, 2023