from email import message
from http import client
from multiprocessing.connection import Client
import discord
import os


Intents = discord.Intents.default()

Intents.members = True

app = discord.Client(command_prefix = ">", intents = discord.Intents.all())


@app.event
async def on_message(message):

    if message.content == "시발":
        await message.channel.send(f"{message.author.name}?욕하누;")

    if message.content == "야발":
        await message.channel.send(f"{message.author.name}?욕하누;")

    if message.content == "ㅅㅂ":
        await message.channel.send(f"{message.author.name}?욕하누;")

    if message.content == "씹새끼":
        await message.channel.send(f"{message.author.name}?욕하누;")

    if message.content == "십새끼":
        await message.channel.send(f"{message.author.name}?욕하누;")

    if message.content == "ㅄ":
        await message.channel.send(f"{message.author.name}?욕하누;")

    if message.content == "ㅂㅅ":
        await message.channel.send(f"{message.author.name}?욕하누;")

    if message.content == "병신":
        await message.channel.send(f"{message.author.name}?욕하누;")

accsess_token = os.environ["BOT_TOKEN"]
app.run(access_token)
