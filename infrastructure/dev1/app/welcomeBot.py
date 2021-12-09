import discord
from discord import Embed
from discord.utils import get
from discord.ext import commands


intents = intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents)


@client.event
async def on_ready():
    print("Bot is ready.")


# @client.event()
# async def on_member_join(member):
#     # replace id with the welcome channel's id
#     await member.send("Bruh")


@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title="Welcome to the Machine Learning Club!",
        description="Here, you can find more about club meetings and resources for machine learning. To subscribe and unsubscribe to the Announcement bot say the commands below in the commands section, ```.subscribe``` ```.unsubscribe```\nIf you ever have any questions feel free to PM a moderator. We hope you enjoy your stay!",
        colour=discord.Colour.orange()
    )
    embed.set_author(name="ML@ASU",
                     icon_url="https://cdn.discordapp.com/icons/909189262463885322/233543728d46e0b164dea05fc6101bfe.webp?size=1024")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/icons/909189262463885322/233543728d46e0b164dea05fc6101bfe.webp?size=1024")
    embed.add_field(name="Social Media",
                    value="[SunDevilSync](https://asu.campuslabs.com/engage/organization/machinelearningclubasu)\n[Instagram](https://www.instagram.com/machinelearningclubatasu/)", inline=True)
    await member.send(embed=embed)

client.run(replace)
