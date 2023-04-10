import disnake
import os
import asyncio
from disnake.ext import commands
import random



INTENTS = disnake.Intents.all()
TOKEN = open("token.txt", "r").read()

client = commands.InteractionBot(intents=INTENTS, allowed_mentions = disnake.AllowedMentions(users = True, everyone = True, replied_user=True, roles = True))

client.load_extension("extentions.moderation")
client.load_extension("extentions.randomfun")
@client.event
async def on_ready():
    print("Bot is ready!")
    while True:
        statusNum = random.randint(1, 4)
        if statusNum == 1:
            await client.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name= ' You give me commands UwU'))
        elif statusNum == 2:
            await client.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name = " /help OwO"))
        elif statusNum == 3:
            await client.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name = " games with friends OwO"))
        elif statusNum == 4:
            await client.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name = " Some random anime UwU"))
        await asyncio.sleep(50)



@client.slash_command(description="Says Hello!")
async def hello(inter):
    await inter.response.send_message("Hello!")

@client.slash_command(description="Sends the command list!")
async def help(inter):
    await inter.response.send_message(
        "Hello! What Commands would you like to see?",
        components=[
        disnake.ui.Button(label="Moderation", style=disnake.ButtonStyle.success, custom_id="mod"),
        disnake.ui.Button(label="Fun", style=disnake.ButtonStyle.success, custom_id="fun"),
        disnake.ui.Button(label="Games", style=disnake.ButtonStyle.success, custom_id="games"),
        ]
        )


@client.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["mod", "fun", "games"]:
        # We filter out any other button presses except
        # the components we wish to process.
        return

    if inter.component.custom_id == "mod":
        embed = disnake.Embed(title="Moderation Commands", description="These are the Moderation Commands!", color=0x00ff00)
        embed.add_field(name="Ban", value="Bans a user from the server!", inline=False)
        embed.add_field(name="Kick", value="Kicks a user from the server!", inline=False)
        embed.add_field(name="Vote", value="Have People Vote For Something!", inline=False)
        await inter.response.send_message(embed=embed, ephemeral=True)

    if inter.component.custom_id == "fun":
        embed = disnake.Embed(title="Fun Commands", description="These are the Fun Commands!", color=0x00ff00)
        embed.add_field(name="Ping", value="Pings the bot!", inline=False)
        embed.add_field(name="Hello", value="Says Hello!", inline=False)
        embed.add_field(name="insult", value="Insult your friends, needs you to @ someone")
        embed.add_field(name="compliment", value="Compliment your friends, needs you to @ someone")
        embed.add_field(name="rolldice", value="Rolls a die, you need to specify the ammount of sides")
        embed.add_field(name="coinflip", value="Flips a coin!")
        embed.add_field(name="mental", value="Tells everyone your mental state!")
        embed.add_field(name="eightball", value="A (maybe insulting) 8Ball!")
        embed.add_field(name="kill", value="Kill your friends, requires you at @ someone")
        embed.add_field(name="owoify", value="OwOify your text or username!")
        await inter.response.send_message(embed=embed, ephemeral=True)

    if inter.component.custom_id == "games":
        embed = disnake.Embed(title="Game Commands", description="These are the Game Commands!", color=0x00ff00)
        embed.add_field(name="NO COMMANDS HERE YET.", value="None", inline=False)

        await inter.response.send_message(embed=embed, ephemeral=True)


client.run(TOKEN)