import discord
from discord.ext import commands
from discord_key import discord_key
from fuzzywuzzy import fuzz
import csv
import re


discord_key = discord_key()
intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print("\033[1m\033[95mWe have logged in as {0.user}".format(client))
    await client.get_channel(1154684336386355302).send("_StarstreamBot is online_ 💫")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="Boten Anna - Basshunter"
        )
    )


@client.event
async def on_raw_reaction_add(payload):
    if payload.user_id == client.user.id:
        return

    channel = client.get_channel(1154684336386355302)

    if channel:
        emoji = str(payload.emoji)
        if emoji:
            await channel.send("😊💫")


key_value_dict = {}


tsv_file_path = "dict.tsv"


def read_file(filepath):
    answers = {}
    with open(filepath, "r", encoding="utf-8") as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter="\t")
        for row in tsv_reader:
            question, answer = row[0], row[1]
            answers[question] = answer
    return answers


@client.event
async def on_message(message):
    if message.content.startswith("!SSB"):
        if message.author == client.user:
            return

        content = message.content.lower()

        answers = read_file(tsv_file_path)

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

        if max_match > 50:
            answer = (
                f"Best match i could find was:\n {best_match[0]} - _{best_match[1]}_"
            )
            await message.channel.send(answer)
        else:
            no_answer = content.replace("!ssb", "")
            await message.channel.send(
                f"I can't find anything related to: **{no_answer}**"
            )


client.run(discord_key)
