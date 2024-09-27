from discord.ext import commands
import discord

BOT_TOKEN = "YOUR TOKEN"
CHANNEL_ID = YOUR ID


bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! Test bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Test bot is ready!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(BOT_TOKEN)
