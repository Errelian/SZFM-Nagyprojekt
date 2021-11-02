import disnake
import os
from disnake.ext import commands

bot = commands.Bot(
    command_prefix='!',
    #test_guilds=[885913747091255366], # Optional
    sync_commands_debug=True
)

@bot.slash_command(description="Initiates chess game") #TODO
async def chess(inter):
    await inter.response.send_message("World")

@bot.slash_command(description="Gives info about the bot") #TODO
async def info(inter):
    await inter.response.send_message("World")

@bot.slash_command(description="Initiates a game of Tic-Tac-Toe") #TODO
async def tictac(inter):
    await inter.response.send_message("World")

discord_token = os.getenv('DISCORD_TOKEN')
print(discord_token)
bot.run(discord_token)