from discord.ext import commands
import discord
import json
from .utils.dataIO import dataIO
import os
import asyncio
import random


class Mycog:
	"""My custom cog that does stuff"""
	def __init__(self,bot):
		self.bot = bot
	
	@commands.command()
	async def cry(self, user:discord.Member):
		await self.bot.say("Don't cry " + user.mention + "...")

	async def rcy(self): 
		rcypic = random.randrange(1,6)
		await self.bot.upload("data/mycog/" + str(rcypic) + "rcy.jpg")
			
def check_folders():
    folders = ("data", "data/mycog/")
    for folder in folders:
        if not os.path.exists(folder):
            print("Creating " + folder + " folder...")
            os.makedirs(folder)

def check_files():
    if not os.path.isfile("data/mycog/settings.json"):
        print("Creating empty settings.json...")
        dataIO.save_json("data/mycog/settings.json", {})

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Mycog(bot))
