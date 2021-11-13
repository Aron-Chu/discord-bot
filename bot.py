import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready.")


# @client.command()
# async def ping(ctx):
#     await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


# @client.command(aliases=["8ball"])
# async def _8ball(ctx, *, question):
#     responses = ['Yes',
#                  'No',
#                  "Maybe"]
#     await ctx.send(f"Question: {question}\n Answer: {random.choice(responses)}")


@client.command()
async def message(ctx, user: discord.Member, *, message=None):
    message = "Welcome to the server!"
    embed = discord.Embed(title=message)
    await user.send(embed=embed)


# @client.event
# async def on_member_join(member):
#     print(f"{member} has joined a server.")

# @client.event
# async def on_member_remove(member):
#     print(f"{member} has left the server")

client.run("OTA5MTg2ODQyMTMyMzgxNzI2.YZAoOw.qYmMlZ9f5ydSAOMdQeK3jik-07I")
