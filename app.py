import discord
from discord_key import discord_key
from discord.ext import commands
from fuzzywuzzy import fuzz
import csv
import re
from datetime import datetime


intents = discord.Intents.all()
intents.message_content = True
filepath = "dict.csv"  #! Database for questions
channel_id = 1154684336386355302 #! Active bot-channel
bot = discord.Client(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("\033[1m\033[95mWe have logged in as {0.user}".format(bot))
    print(f"{datetime.now()}")
    await bot.get_channel(channel_id).send("_StarstreamBot is online_ 💫")
    await bot.change_presence(
        activity=discord.CustomActivity(
            name='🤖 Type "!SBB <keywords>" to call me', emoji="'🤖"
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
                print(f"🤖 {payload.member} skickade en bot i {payload.channel.name}! 🤖")
            elif payload.emoji:
                await channel.send("😊💫")


@bot.event
async def on_disconnect():
    print(f"Disconnect at {datetime.now()}")


def read_file(filepath):
    answers = {}
    with open(filepath, "r", encoding="utf-8") as file:
        filereader = csv.reader(file, delimiter=";")
        next(filereader, None)  # Skip first line in file, if needed
        line_count = 0
        for row in filereader:
            line_count += 1

            if len(row) >= 3:
                question, answer, syntax = row[0], row[1], row[2]
                answers[question] = f"{answer}", f"{syntax}"
            else:
                print(f"Ignorerar raden: {line_count}\nFel på databasformat!")

    return answers


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    if content == "!ssb":
        await message.channel.send(
            f"Hi, i'm StarstreamBot! 👋 \n* To activate me use: _!SSB <command>_\n* Use: _!SSB-commands_ to see my commands!"
        )
    
    elif content.startswith("!thiswascs50p"):
        embed = discord.Embed(
        title="CS50:Python",
        description="This was CS50P, thanks for watching!",
        color=0x7e7a17,
        )
        
        embed.set_thumbnail(
        url="https://www.harvard.edu/wp-content/uploads/2021/02/harvard-fac-375x281.png"
        )
        
        embed.set_footer(text="Mattias Stjernström, 2023",icon_url="https://www.python.org/static/img/python-logo-large.c36dccadd999.png")

        await bot.get_channel(channel_id).send(embed=embed)
    
    elif content.startswith("!ssb-commands"):
        await message.channel.send("I listen to these commands:\n* !SSB <command> _-for Python Dictionary_\n* !SSB-example _for testing purposes_")


    elif content.startswith("!ssb "):
        if message.author == bot.user:
            return

        content = message.content.lower()

        answers = read_file(filepath)

        best_match = ("", "")
        max_match = 0

        for question, (answer, syntax_use) in answers.items():
            pattern_question = fuzz.token_set_ratio(content, question, syntax_use)
            match_pattern = fuzz.token_set_ratio(content, answer, syntax_use)

            if pattern_question > max_match:
                best_match = (question, answer, syntax_use)
                max_match = pattern_question

            if match_pattern > max_match:
                best_match = (question, answer, syntax_use)
                max_match = match_pattern

        if max_match > 50:  #! Accuracy, default is 50
            embed = discord.Embed(
                title=best_match[0],
                description=best_match[1],
                color=discord.Color.dark_blue(),
            )

            embed.add_field(name="Syntax and/or Use", value=f"{best_match[2]}", inline=True)

            await bot.get_channel(channel_id).send(embed=embed)
            answer = (
                f">>> _Wasn't **{best_match[0]}** what you were looking for?\nTry specify more and/or check spelling!_"
            )
            await message.channel.send(answer)
            print(f"{message.author} asked for '{message.content}' and got '{best_match[0]}' as answer")


        else:
            no_answer = content.replace("!ssb", "")
            await message.channel.send(
                f"I can't find anything related to: **{no_answer}**"
            )
            print(f"{message.author} asked for '{message.content}' and got no answer.")



discord_key = discord_key()
bot.run(discord_key)
