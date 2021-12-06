import discord
import random
from discord import Embed
from discord.utils import get
from discord.ext import commands
from datetime import datetime


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
users = []


@client.command(pass_context=True)
async def deletethis(ctx):
    await ctx.message.delete()


@client.command(pass_context=True)
async def subscribe(ctx):
    member = ctx.message.author
    # message = ctx.message.id
    # if ctx.message == ".subscribe":
    #     await message.delete()
    # member = ctx.message.author.name
    # discrim = ctx.message.author.discriminator
    if member not in users:
        users.append(member)
    ctx.message.delete()
    print(member)
    print(users)
    await ctx.message.delete()


@client.command(pass_context=True)
async def unsubscribe(ctx):
    member = ctx.message.author
    # message = ctx.message.id
    # if ctx.message == ".subscribe":
    #     await message.delete()
    # member = ctx.message.author.name
    # discrim = ctx.message.author.discriminator
    users.remove(member)
    ctx.message.delete()
    print(member)
    print(users)
    await ctx.message.delete()


@client.command()
async def message(ctx, user: discord.Member, *, message=None):
    message = "Welcome to the server!"
    embed = discord.Embed(title=message)
    await user.send(embed=embed)


@client.command(pass_context=True)
async def sendtousers(ctx):

    guild = client.get_guild(909189262463885322)
    embed = discord.Embed(
        title="Machine Learning Club",
        description="I’m excited to announce that our next meeting will be about neural networks! There will be a workshop and live code demonstration/walkthrough!",
        colour=discord.Colour.orange()
    )
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/757324459538514051/910338516649640036/neural_network-flyer.png")
    embed.set_thumbnail(
        url=ctx.guild.icon_url)
    embed.set_author(name="Terricon",
                     icon_url=ctx.guild.icon_url)
    embed.add_field(name="Location", value="PSH 150", inline=True)
    embed.add_field(name="Time", value="Friday, 5:00pm-6:30pm", inline=True)
    # embed.add_field(name="Description", value="Field Value", inline=False)

    for i in users:
        await i.send(embed=embed)
    await ctx.send(embed=embed)
    await ctx.message.delete()
    # await ctx.send(embed=embed)


@client.command(pass_context=True)
async def announcemeeting(ctx):

    guild = client.get_guild(909189262463885322)
    embed = discord.Embed(
        title="Machine Learning Club",
        description="I’m excited to announce that our next meeting will be about neural networks! There will be a workshop and live code demonstration/walkthrough!",
        colour=discord.Colour.orange()
    )
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/757324459538514051/910338516649640036/neural_network-flyer.png")
    embed.set_thumbnail(
        url=ctx.guild.icon_url)
    embed.set_author(name="Terricon",
                     icon_url=ctx.guild.icon_url)
    embed.add_field(name="Location", value="PSH 150", inline=True)
    embed.add_field(name="Time", value="Friday, 5:00pm-6:30pm", inline=True)
    # embed.add_field(name="Description", value="Field Value", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()
    # await ctx.send(embed=embed)


@client.command(pass_context=True)
async def showsubscribed(ctx):
    for i in range(len(users)):
        await ctx.send(users[i].name + "#" + users[i].discriminator)
    await ctx.message.delete()

channel_id = 12345  # Replace with channel id
message_id = 613850569718890495  # Note these are ints, not strings

channel_id = 909189309947576340  # Replace with channel id
message_id = 909194774546898995  # Note these are ints, not strings


client.run(replace)
