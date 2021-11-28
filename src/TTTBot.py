import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!")

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

#milyen mezőkkel nyerhet egy-egy játékos
winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2
        
        #pálya kirajzolása a játék kezdetéhez
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]
        
        #kezdőjátékos eldöntése randomizálva
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("<@" + str(player1.id) + "> kezdi a játékot.")
        elif num == 2:
            turn = player2
            await ctx.send("<@" + str(player2.id) + "> kezdi a játékot.")
    else:
        await ctx.send("Még tart a játék.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                #pálya kirajzolása aktuális állás szerint
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]
                #játékállás megnézése, szükség esetén eredményhirdetés
                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(":first_place:" + mark + " wins! :first_place: ")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Döntetlen :handshake:!")

                #fordulók váltása
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("1 és 9 között válassz üres mezőt. :1234: ")
        else:
            await ctx.send("A másik játékos következik. :point_up: ")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Magadat és egy másik játékost is nevezz meg. :clap: ")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Használd az '@USER_NAME' szintaxist, hogy más játékosokat meghívj a játékba. :eyes: ")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Nevezd meg a pozíciót amit megjelölsz. :point_left: ")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("A játék csak egészszám-értékkel működik, azt adj meg  :1234:   :wink:")

client.run("Token here")