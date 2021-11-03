import disnake
import os
from disnake.ext import commands
from ChessBot import ChessBot

bot = commands.Bot(
    command_prefix='!',
)

chessBot = ChessBot()

@bot.event
async def on_ready():
    chessBot = ChessBot()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.command()
async def author(ctx):
    await ctx.send(ctx.author.id)


@bot.command() #TODO REMOVE QUEUE AND MAKE IT SO YOU CAN CHALLENGE PEOPLE
async def chess(ctx):
    ###Starts a new game between two people in the queue
    reply = chessBot.queue(ctx.author.id, ctx.author)
    await ctx.send(reply)


@bot.command() #TODO MAKES A MOVE
async def move(ctx, algNot: str):
    reply = chessBot.move(ctx.author.id, algNot)
    if reply is None:
        reply = chessBot.representation(ctx.author.id)
        reply += chessBot.overCleanup(ctx.author.id)
    await ctx.send(reply)


@bot.command()
async def resign(ctx):
    reply = chessBot.resign(ctx.author.id)
    await ctx.send(reply)


@bot.command()
async def legal(ctx):
    reply = chessBot.listLegalMoves(ctx.author.id)
    await ctx.send(reply)

@bot.command() #TODO GIVES INFO ABOUT THE BOT
async def info(ctx):
    await ctx.send("info")


@bot.command() #TODO CHALLENGES THE AI
async def tictac(ctx):
    await ctx.send("tictac")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

discord_token = os.getenv('DISCORD_TOKEN')
bot.run(discord_token)