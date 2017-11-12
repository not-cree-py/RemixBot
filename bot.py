import discord
import os
import io
import sys
from discord.ext import commands

bot = commands.Bot(command_prefix='c.')
bot.remove_command('help')
developers = [
        311970805342928896,
        316586772349976586,
        292690616285134850
    ]

@bot.event
async def on_ready():
    ctx.send("Bot Is Online")
@bot.command()
async def help(ctx):
        await ctx.send("\n\nping : Pong!")
@bot.command()
async def ping(ctx):
    """Pong! check if bot working"""
    await ctx.send("Pong! bot is up and working")

if not os.environ.get('TOKEN'):
  print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
