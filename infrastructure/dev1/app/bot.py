import discord
import pickle
import random
from discord import Embed
from discord.utils import get
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=".", intents=intents)


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
users2 = []


@client.command(pass_context=True)
async def deletethis(ctx):
    await ctx.message.delete()


@client.command(pass_context=True)
async def sendtousers(ctx):

    guild = client.get_guild(751914393796608090)
    channel = client.get_channel(925587325457690625)
    embed = discord.Embed(
        title="Machine Learning Club",
        description="I’m excited to announce that our next meeting will be about neural networks! There will be a workshop and live code demonstration/walkthrough!",
        colour=discord.Colour.orange()
    )
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/757324459538514051/910338516649640036/neural_network-flyer.png")
    embed.set_thumbnail(
        url=ctx.guild.icon_url)
    embed.set_author(name="ML@ASU",
                     icon_url=ctx.guild.icon_url)
    embed.add_field(name="Location", value="PSH 150", inline=True)
    embed.add_field(name="Time", value="Friday, 5:00pm-6:30pm", inline=True)
    verified = discord.utils.get(guild.roles, name="subscriber")
    for member in guild.members:
        if verified in member.roles:
            await member.send(embed=embed)

    # for i in users2:
    #     await i.send(embed=embed)
    await channel.send(embed=embed)
    await ctx.message.delete()
    # await ctx.send(embed=embed)


@client.command(pass_context=True)
async def announcemeeting(ctx):

    guild = client.get_guild(751914393796608090)
    embed = discord.Embed(
        title="Machine Learning Club",
        description="I’m excited to announce that our next meeting will be about neural networks! There will be a workshop and live code demonstration/walkthrough!",
        colour=discord.Colour.orange()
    )
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/757324459538514051/910338516649640036/neural_network-flyer.png")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/909213318588272691/924024902518997072/unknown.png")
    embed.set_author(name="ML@ASU",
                     icon_url=ctx.guild.icon_url)
    embed.add_field(name="Location", value="PSH 150", inline=True)
    embed.add_field(name="Social Media",
                    value="[here](https://asu.campuslabs.com/engage/organization/machinelearningclubasu) [Instagram](https://www.instagram.com/machinelearningclubatasu/)", inline=True)
    embed.add_field(name="Time", value="Friday, 5:00pm-6:30pm", inline=True)
    # embed.add_field(name="Description", value="Field Value", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()
    # await ctx.send(embed=embed)


channel_id = 12345  # Replace with channel id
message_id = 613850569718890495  # Note these are ints, not strings

channel_id = 909189309947576340  # Replace with channel id
message_id = 909194774546898995  # Note these are ints, not strings


client.run( < REPLACE_CLIENT_SECRET > )
