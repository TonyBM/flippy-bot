from message_commands import message_command_map
from discord.ext import commands
import random
bot = commands.Bot(command_prefix="8=D", description="This is a Helper Bot")

throat_sounds = ["GULP", "GGGGHGHGHGGHGH", "UUGHGHG", "GXH"]

@bot.command()
async def throat(ctx):
    rand_int = random.randint(0, len(throat_sounds) - 1)
    await ctx.send(throat_sounds[rand_int])

@bot.event
async def on_ready():
    print("Aqui toi")

bot.run('OTY4NzIwNjk3NTE1OTcwNTgw.Ymi9dA.CmrleZA2AWUYxCtAZLtFUOqHu-I')