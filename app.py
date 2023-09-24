import discord
from discord.ext import commands
from discord_key import discord_key
from fuzzywuzzy import fuzz
import csv
import re


discord_key = discord_key()
intents = discord.Intents.all()
bot = discord.Client(command_prefix="!", intents=intents)
channel = bot.get_channel(1154684336386355302)


@bot.event
async def on_ready():
    print("\033[1m\033[95mWe have logged in as {0.user}".format(bot))
    await bot.get_channel(1154684336386355302).send("_StarstreamBot is online_ 💫")
    await bot.change_presence(activity=discord.CustomActivity(name='🤖 Type "!SBB <keywords>" to call me' ,emoji='🤖'))


@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == bot.user.id:
        return

    channel = bot.get_channel(1154684336386355302)

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


@bot.event
async def on_message(message):
    if message.content.startswith("!SSB"):
        if message.author == bot.user:
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
                f"Best match i could find was:```{best_match[0]} - {best_match[1]}``` _Do you wan't more information about {best_match[0]}?_ Type 'Yes'"
            )
            await message.channel.send(answer)

        else:
            no_answer = content.replace("!ssb", "")
            await message.channel.send(
                f"I can't find anything related to: **{no_answer}**"
            )


bot.run(discord_key)
