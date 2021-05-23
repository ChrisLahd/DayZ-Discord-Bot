import os
import sys
import discord
import asyncio
import time
from discord.ext import commands

token = open('token.txt', 'r').readline()

bot = commands.Bot(command_prefix='=', description="Blackout DayZ Bot")
bot.remove_command('help')

@bot.event
async def on_ready():
    game = discord.Game(name="=help")
    await bot.change_presence(status=discord.Status.idle, activity=game)


@bot.command()
async def help(ctx):
    msg = discord.Embed(title="Help", description="Commands for the bot")
    msg.add_field(name="Basic", value="Uptime: **Shows Blackout server uptime**\nPlayers: **Shows online players**")
    await ctx.send(embed=msg)

bot.run(token)