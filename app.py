import discord
from discord.ext import commands
from discord_key import discord_key
from fuzzywuzzy import fuzz
import csv
import re


intents = discord.Intents.all()
bot = discord.Client(command_prefix="!", intents=intents)
channel = bot.get_channel(1154684336386355302)
filepath = "test_dict.csv"  #! Database for questions


@bot.event
async def on_ready():
    print("\033[1m\033[95mWe have logged in as {0.user}".format(bot))
    await bot.get_channel(1154684336386355302).send("_StarstreamBot is online_ 💫")
    await bot.change_presence(
        activity=discord.CustomActivity(
            name='🤖 Type "!SBB <keywords>" to call me', emoji="🤖"
        )
    )

    @bot.event
    async def on_raw_reaction_add(payload):
        if payload.user_id == bot.user.id:
            return

        channel = bot.get_channel(payload.channel_id)

        if channel:
            if payload.emoji.name == "🤖":
                await channel.send("Bee-bop!")  # Easter-egg
            elif payload.emoji:
                await channel.send("😊💫")


def read_file(filepath):
    answers = {}
    with open(filepath, "r", encoding="utf-8") as file:
        filereader = csv.reader(file, delimiter=",")
        for row in filereader:
            if len(row) >= 3:
                question, answer, example = row[0], row[1], row[2]
                answers[question] = f"{answer}, {example}"
            else:
                print(
                    f"Ignorerar raden: {row} eftersom den inte har tillräckligt med kolumner.\nError: Fel på databasformat!"
                )

    return answers


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    if content.startswith("!ssb-commands"):
        await message.channel.send("I listen to these commands:\n* !SSB <command>")
    
    elif content == "!ssb":
        await message.channel.send(f"Hi! 👋 \n* To activate me use: _!SSB+<command>_\n* Use: _!SSB-commands_ to see my commands!")

    elif content.startswith("!ssb"):
        if message.author == bot.user:
            return

        content = message.content.lower()

        answers = read_file(filepath)

        best_match = ("", "")
        max_match = 0

        for question, pattern in answers.items():
            pattern_question = fuzz.ratio(content, question.lower())
            match_pattern = fuzz.ratio(content, pattern.lower())

            if pattern_question > max_match:
                best_match = (question, pattern)
                max_match = pattern_question

            if match_pattern > max_match:
                best_match = (question, pattern)
                max_match = match_pattern

        if max_match > 50:  #! Accuracy, default is 50
            answer = (
                f"Best match i could find was:```{best_match[0]} - {best_match[1]}```"
            )
            # print(best_match) #? Dev-mode, remove!!!!
            await message.channel.send(answer)

        else:
            no_answer = content.replace("!ssb", "")
            # print(best_match) #? Dev-mode, remove!!!!
            await message.channel.send(
                f"I can't find anything related to: **{no_answer}**"
            )

discord_key = discord_key()
bot.run(discord_key)
