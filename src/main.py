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


@bot.command() #TODO STARTS A NEW GAME
async def chess(ctx):
    response = chessBot.queue(ctx.author.id, ctx.author)
    await ctx.send(response)


@bot.command() #TODO MAKES A MOVE
async def move(ctx, algNot: str):
    response = chessBot.move(ctx.author.id, algNot)
    if response is None:
        response = chessBot.representation(ctx.author.id)
        response += chessBot.overCleanup()
    await ctx.send(response)


@bot.command() #TODO
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