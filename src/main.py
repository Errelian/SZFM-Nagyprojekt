import disnake
import os
from disnake.ext import commands
from ChessBot import ChessBot

bot = commands.Bot(
    command_prefix='!',
)

chessBot = ChessBot()
#bot.get_user(userId)
@bot.event
async def on_ready():
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
    if reply != "One of the users is already in a game.":
        await ctx.send(file=disnake.File(reply))
        os.remove(reply)
    else:
        await ctx.send(reply)


@bot.command() #MAKES A MOVE
async def move(ctx, algNot: str):
    reply = chessBot.move(ctx.author.id, algNot)
    image = None
    if reply == "":
        image = chessBot.representation(ctx.author.id)
        reply = chessBot.overCleanup(ctx.author.id)
    await ctx.send(reply, file=disnake.File(image))


@bot.command()
async def resign(ctx):
    reply = chessBot.resign(ctx.author)
    await ctx.send(reply)


@bot.command()
async def legal(ctx):
    reply = chessBot.listLegalMoves(ctx.author.id)
    await ctx.send(reply)

@bot.command() #TODO GIVES INFO ABOUT THE BOT
async def info(ctx):
    reply = "This is a bot that helps you play chess against another user, or play Tic-Tac-Toe against the bot. For chess, type !chessChallenge @User. For Tic-Tac-Toe type !tictac. For more info, use !tictacInof and !chessInfo respectively"
    await ctx.send(reply)

@bot.command() #TODO GIVES INFO ABOUT CHESS
async def chessInfo(ctx):
    reply = "!resign to resign \n !legal to get your currently legal moves. !move [algnot] to move, !chessChellange @User to begin playing "
    await ctx.send(reply)


@bot.command() #TODO GIVES INFO ABOUT TICTACTOE
async def tictacInfo(ctx):
    reply = "!place [1-9] to place your symbol on empty square, !tictactoe @USER @ME to begin playing"
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
