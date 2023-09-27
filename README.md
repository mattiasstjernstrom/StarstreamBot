# 💫🤖 StarstreamBot!


#### Video Demo:  https://youtu.be/QPLI4aW0dNk
#### Description:
_StarstreamBot_ is a "dictionary bot" built in Python as a hobby project. The bot is based on the Levenshtein distance algorithm and works like this: it takes a string that you, as a user, search for and compares it with the string in the database. The higher the similarity, the more likely the user means that specific part of the dictionary. This algorithm also allows for some degree of misspelling and the inclusion of words that might not be in the dictionary but can still find the correct word.

Currently, I have a test word-list containing Python's built-in functions, syntax, and error messages for testing purposes.

## Setup:
* Make a bot at [Discord developer portal](https://discord.com/developers/applications/)
* Copy ``channel-ID`` and ``Bot_token``
* Make a file named: ``discord_key.py`` (or use dotenv) and use copy this:
```py
def discord_key():
    return "<discord_key>"
```
* Change ``channel_id`` in app.py
* Invite bot to your channel
* Run ``app.py`` ➡️ Happy botting!

## Criteria for the course

- [x] What will your software do? What features will it have? How will it be executed?
    > * A Discord dictionary-bot
    > * Features: Ask the bot for words and sentences and get explanations
    > * As a Discord bot, but it will also have a ``Stand Alone Mode``
- [x] What new skills will you need to acquire? What topics will you need to research?
    > * Using frameworks, using modules
    > * How to execute a Discord Bot, how to make a dictionary with some "IQ", i need to research algorithms that fits in my task
- [ ] If working with one or two classmates, who will do what?
    > I'm lone coder 🧑‍💻
- [x] In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to accomplish less in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? A better outcome? The best outcome?
    > A good outcome for my project would be if some kind of algorithm can predict similarity between to strings so i can pull the right explanation from database
- [x] Create a Video, max three minutes
- [x] Upload to youtube
- [x] Submit to ``Google-forms``
- [x] Make ``Readme.md`` _(this file)_
- [x] Submit to Github ``submit50 cs50/problems/2022/python/project`` 
- [x] Done! 🥳


## Author:
- Mattias Stjernström, 2023