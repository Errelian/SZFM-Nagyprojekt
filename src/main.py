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
async def echoTaggedId(ctx, user: disnake.User):
    await ctx.send(user.id)

@bot.command()
async def author(ctx):
    await ctx.send(ctx.author.id)


@bot.command()
async def chessChallenge(ctx, user: disnake.User):
    reply = chessBot.matchup(ctx.author, user)
    await ctx.send(reply)


@bot.command() #MAKES A MOVE
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
    reply = "info"
    await ctx.send(reply)


@bot.command() #TODO CHALLENGES THE AI
async def tictac(ctx):
    reply = 'tictac'
    await ctx.send(reply)


@bot.command()
async def ping(ctx):
    reply = 'pong'
    await ctx.send(reply)

discord_token = os.getenv('DISCORD_TOKEN')
bot.run(discord_token)