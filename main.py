import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from GSpreadsheet import GSpreadsheet

if __name__ == '__main__':
    intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
    bot = commands.Bot(command_prefix='!heyfool ', intents=intents)
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    g = GSpreadsheet()
    @bot.event
    async def on_ready():
        print("Fool Ready to Rock&Roll")

    @bot.command()
    async def helpme(ctx):
        message_channel = bot.get_channel(int(os.environ['CHANNEL_ID']))
        await message_channel.send("I'm Ready Sir")

    @bot.command()
    async def records(ctx):
        message_channel = bot.get_channel(int(os.environ['CHANNEL_ID']))
        df, msg = g.get_all_records(), ""
        for val in df.values:
            msg += val
        await message_channel.send(msg)

    @bot.command()
    async def add_records(ctx):
        message_channel = bot.get_channel(int(os.environ['CHANNEL_ID']))
        message_list = ctx.message.content.split()[2:]
        g.insert_items(message_list)
        await message_channel.send("Items added!")

    @bot.command()
    async def delete_records(ctx):
        message_channel = bot.get_channel(int(os.environ['CHANNEL_ID']))
        commands = ctx.message.content.split()[2:]
        g.delete_items(commands)
        await message_channel.send("Items deleted!")

    bot.run(os.environ['DISCORD_TOKEN'])