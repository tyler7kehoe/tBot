# bot.py by Tyler Kehoe
# TODO: figure out exception handling for 8 ball

# Implementation ideas:

import discord
import random
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument

bot = commands.Bot(command_prefix='t!')


@bot.event
async def on_ready():
    print('tBot is ready :D')


# message when member joins
@bot.event
async def on_member_join(member):
    print(f'Welcome {member} to your new home! <3 ')



# message when member leaves
@bot.event
async def on_member_remove(member):
    print(f'{member} has left :( probably better off this way...')




# HELP SECTION -> needs work, creates a pop-up box with incorrect info
@bot.command
async def help(ctx):
    await ctx.send('Welcome to the tBot help menu!\n\nHere is a list of all the available commands!\n'
                   + '/ping\n/coinflip\n/8ball')


# gets the ping of the bot
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)} ms')

# coin flip game
@bot.command(aliases = ['flipcoin', 'flip'])
async def coinflip(ctx):
    coinsides = ['Heads', 'Tails']
    await ctx.send(f'{random.choice(coinsides)}!')



# Magic 8-ball game
@bot.command(aliases=['8ball', 'eightball', '8-ball'])  # aliases allow to be used as a command
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Your question made absolutely no sense. Try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes – definitely.',
                 'You may rely on it.']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


bot.run('NzYyNzEzOTQ1MTQ3OTY1NTIw.X3tKtw.DfnjkWUu3LDBtm1-oOIDEKLP5lg')
