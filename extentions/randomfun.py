import disnake
from disnake.ext import commands
import random

validanswers = ["yes", "Yes", "no", "No", "n", 'N', "Y", "y"]
yes = ["Yes", "yes", "Y", "y"]
no = ["No", "no", "N", "n"]

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Rolls a dice with the specified amount of sides.")
    async def rolldice(self, inter, arg = int(0)):
        if arg == 0:
            await inter.response.send_message("You need to specify how many sides.")
        else:
            await inter.response.send_message(f"You rolled a D{arg}")
            numrolled = random.randint(1, arg)
            await inter.response.send_message(f"You rolled a {numrolled}!")

    @commands.slash_command(description="Flips a coin and lands on either heads or tails.")
    async def coinflip(self, inter):
        sides = ["Heads", "Tails"]
        flipside = random.choice(sides)
        await inter.response.send_message(f"The coin flipped and landed {flipside}")

    @commands.slash_command(description="Kills a user with a random weapon.")
    async def kill(self, inter, user: disnake.Member):
        weapon=("Knife", "Gun", "Sword")
        await inter.response.send_message(inter.author.mention + f" Killed {user} with a {random.choice(weapon)}")

    @commands.slash_command(description="Stabs a user with a knife.")
    async def stab(self, inter, user: disnake.Member):
        await inter.response.send_message(f"{inter.author.mention} Just stabbed {user}")
        
    @commands.slash_command(description="Insults a user.")
    async def insult(self, inter, user: disnake.Member):
        insults = ("Screw you", "You are a jerk", "You suck", "OH NO ITS", "Ugh, its", "EVERYBODY GET OUT, ITS", "Deal with it", "Frick you ", "GDIAH ", "small pp ")
        await inter.response.send_message(f"{random.choice(insults)} {user}")
        
    @commands.slash_command(description="Compliments a user")
    async def compliment(self, inter, user: disnake.Member):
        compliments = ("Is Looking nice today", "Is Awesome", "Is a good person", "Is nice", "Is A cool person", "Isn't an idiot", "Needs to talk more")
        await inter.response.send_message(f"{user} {random.choice(compliments)}")
        
    @commands.slash_command(description="Tells you your mental state")
    async def mental(self, inter):
        answers = ("Is Mentally Insane", "Is Mentally Stable", "Is Going Insane", "Needs therapy", "Needs a huge suppository", "Is an idiot", "Has Crippling Depression")
        await inter.response.send_message(f"{inter.author.mention} {random.choice(answers)}")

    @commands.slash_command(description="Chooses stuff For You, maybe a little insulting")
    async def eightball(self, inter, question):
        possible_responses = [
                'Thats gonna have to be a no',
                'It Is not looking likely',
                'For Sure you jerk',
                'Fuck you im not answering that',
                'Might be Likely you idiot',
                'I dont care you piece of shit',
                'Ok The answer is FUCK yes.', ]
        await inter.response.send_message(f"Question: {question}\nAnswer: " + random.choice(possible_responses) + ", " + inter.author.mention)
    
    @commands.slash_command(description="OwO-ifys your text")
    async def owoify(self, inter, text=""):
        if text == "":
            text = inter.author.name
        else:
            pass
        text = text.replace("r", "w")
        text = text.replace("l", "w")
        text = text.replace("R", "W")
        text = text.replace("L", "W")
        text = text.replace("ove", "uv")
        text = text.replace("OVE", "UV")
        text = text.replace("o", "ow")
        text = text.replace("O", "OW")
        await inter.response.send_message(text)


def setup(bot):
    bot.add_cog(FunCog(bot))