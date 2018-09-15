
import discord
from discord.ext import commands

TOKEN = 'TOKEN'

description = '''FenrirBot | For the Horde!'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def raid():
    """will display our current raiding schedule."""
    await bot.say("We'll be raiding every Monday & Wednesday at 9:00PM EST")

@bot.command()
async def pug():
    """will give you the URL to invite temporary members to the Discord Server."""
    await bot.say("Invite PUG members using: REVOKED LINK")

@bot.command()
async def hello():
    """FenrirBot will respond back."""
    await bot.say("Hello, Champion!")

@bot.command()
async def officers():
    """will tell  you who the guild officers are."""
    await bot.say("<@!156603893441101824>, <@!169986893167984640>")


bot.run(TOKEN)