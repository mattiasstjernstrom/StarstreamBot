import discord
from discord_key import discord_key
from discord.ext import commands
from project import fuzz_ratio
from project import write_file
from datetime import datetime
import csv


intents = discord.Intents.all()
intents.message_content = True
filepath = "dict.csv"  #! Database for questions
channel_id = 1154684336386355302  #! Active bot-channel
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
            elif payload.emoji.name == "👋":
                await channel.send("👋")
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
            color=0x7E7A17,
        )

        embed.set_thumbnail(
            url="https://www.harvard.edu/wp-content/uploads/2021/02/harvard-fac-375x281.png"
        )

        embed.set_footer(
            text="Mattias Stjernström, 2023",
            icon_url="https://www.python.org/static/img/python-logo-large.c36dccadd999.png",
        )

        await bot.get_channel(channel_id).send(embed=embed)

    elif content.startswith("!ssb-commands"):
        await message.channel.send(
            "I listen to these commands:\n* !SSB <command> _- for Python Dictionary_ 🐍\n* !SSB-example _for testing purposes _🧑‍💻"
        )

    elif content.startswith("!ssb "):
        if message.author == bot.user:
            return

        find = message.content.lower().replace("!ssb ", "")
        best_match = fuzz_ratio(find)

        if best_match != None:
            embed = discord.Embed(
                title=best_match[0],
                description=best_match[1],
                color=discord.Color.dark_blue(),
            )

            embed.add_field(
                name="Syntax and/or Use", value=f"{best_match[2]}", inline=True
            )

            await bot.get_channel(channel_id).send(embed=embed)
            answer = f">>> _Wasn't **{best_match[0]}** what you were looking for?\nTry specify more and/or check spelling!_"
            await message.channel.send(answer)
            print(
                f"{message.author} asked for '{message.content}' and got '{best_match[0]}' as answer"
            )
        else:
            no_answer = content.replace("!ssb ", "")
            embed = discord.Embed(
                title="Sorry!",
                description=f"I can't find anything related to:\n**{no_answer}**",
                color=discord.Color.red(),
            )
            embed.set_footer(text="_Try specify more and/or check spelling!_")
            await bot.get_channel(channel_id).send(embed=embed)
            print(f"{message.author} asked for '{message.content}' and got no answer.")
            write_file(find)


discord_key = discord_key()
bot.run(discord_key)
