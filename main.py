from dotenv import load_dotenv
import discord, json, os, logging, time, re, string, os.path
from discord.ext import commands, tasks
#from progam_functions import *

#Program Variables
dir = os.path.dirname(__file__)

#Program Functions
load_dotenv(os.path.join(dir, ".env"))
'''
if os.path.isdir('./guildfiles') != True:
    os.mkdir(os.path.join('./', 'guildfiles'))      
else:
    pass
'''

# Discord Variables
activity = discord.Activity(type=discord.ActivityType.listening, name="stupid questions")
author_id = "892999941146963969"
prefix = 'g!'

# Bot info
bot = commands.Bot(
    command_prefix=prefix,
    case_insensitive=True,
    activity=activity,
    status=discord.Status.online
)
bot.author_id = author_id 
#bot.remove_command("help") #For custom help command

# Logger
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)

#google
@bot.command()
@commands.has_role('Moderator')
async def g(ctx):
  google ="https://www.google.com/search?q="
  message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
  arg = re.sub("\s", "+", message.content)
  await ctx.send(f'{message.author.mention}\n{google}{arg}')

@g.error
async def g_error(ctx, error):
  await ctx.send(f"Error: {error}")

#RUN
if __name__ == "__main__":
    bot.run(os.environ.get("KEY"))