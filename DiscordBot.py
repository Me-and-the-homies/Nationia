import discord
from discord.ext import commands



client = commands.Bot(command_prefix=';')

"""@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def spakian(ctx):
    await ctx.send('is amazing')

@client.command()
async def ajsharkson(ctx):
    await ctx.send('is cool')

@client.command()
async def pings(ctx):
    await ctx.send('are gay')

@client.command()
async def discountWhiskey(ctx):
    await ctx.send('shows off way too much')

@client.command()
async def pingStaff(ctx):
    await ctx.send('did you expect me to ping them? If so, just DM them instead')

@client.command()
async def getRole(ctx):
    await ctx.send('DM an Admin or an IllusionTV member if you want a custom role')"""

async def createPoll(ctx, pollName):
    await ctx.send(f"new poll {pollName} has been created. Start naming your options\n\n ex:\n1.cool\n2.not cool\n3.epic")



client.run('a9qTq06Y1DmWEaKEuyUOBb3rXoWrNSc3')