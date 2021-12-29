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
    channel = client.get_channel(925587325457690625)
    global msg
    msg = await channel.send("Subscribe to the Announcement Bot")
    await msg.add_reaction("✅")


@ client.event
async def on_reaction_add(reaction, user):
    # if reaction.user == client.user:
    #     return
    guild = client.get_guild(751914393796608090)
    channel = client.get_channel(925587325457690625)
    if reaction.message == msg and reaction.emoji == "✅":
        if user == client.user:
            return
        verified = discord.utils.get(guild.roles, name="subscriber")
        await user.add_roles(verified)


@ client.event
async def on_reaction_remove(reaction, user):
    guild = client.get_guild(751914393796608090)
    if reaction.message == msg and reaction.emoji == "✅":
        verified = discord.utils.get(guild.roles, name="subscriber")
        await user.remove_roles(verified)


@ client.event
async def on_member_join(member):
    embed = discord.Embed(
        title="Welcome to the Machine Learning Club!",
        description="Here, you can find more about club meetings and resources for machine learning. To subscribe and unsubscribe to the Announcement bot react or unreact to the bot in the commands section. ```✅``` \n **Be Respectful**\n This is a community for learning. If you ever feel like you are being harassed, or not welcome by somebody, please reach out to the management team and let us know. Let's all be respectful towards each other and follow the [#rules](https://discord.com/channels/751914393796608090/757818662429392988/758454584875810826)\n\nIf you ever have any questions feel free to PM a moderator. We hope you enjoy your stay!",
        colour=discord.Colour.orange()
    )
    embed.set_author(name="ML@ASU",
                     icon_url="https://cdn.discordapp.com/attachments/909213318588272691/924023959270334484/test.png")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/909213318588272691/924024902518997072/unknown.png")
    embed.add_field(name="Social Media",
                    value="[SunDevilSync](https://asu.campuslabs.com/engage/organization/machinelearningclubasu)\n[Instagram](https://www.instagram.com/machinelearningclubasu/)", inline=True)
    embed.add_field(name="Other Resources",
                    value="[Kaggle Competition](https://www.kaggle.com/c/asuml)\n[Coursera](https://www.instagram.com/machinelearningclubatasu/)\n[ML Resources](https://discord.com/channels/751914393796608090/921134484735283251/921134502405873674)", inline=True)

    await member.send(embed=embed)

client.run( < REPLACE_CLIENT_SECRET > )
