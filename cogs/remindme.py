from discord.ext import commands
import discord
import json
from .utils.dataIO import dataIO
from .utils.dataIO import fileIO
import os
import asyncio
import time
import datetime
import logging

reminders = None

class Remindme:
	"""My custom cog that does stuff"""
	def __init__(self,bot):
		self.bot = bot
		self.times = {"minute": 60, "minutes": 60}

	@commands.command(pass_context=True, no_pm=True)
	async def remindmein(self, ctx, timenum:int, timeunit:str, msg:str):
	#create dictionary to store user + message
	#check for time input and compare with current time, if same then ping user
		author = ctx.message.author
		curr_time = ctx.message.timestamp
		if timenum < 1:
			await self.bot.say("Time can't be less than 1.")
			return
		if not timeunit in self.times:
			await self.bot.say("Invalid input.")
			return
		
		timer = datetime.timedelta(seconds = self.times[timeunit]*timenum)
		new_time = curr_time + timer 
		t = new_time.strftime('%Y-%m-%d %H:%M')
		#await self.bot.say(str(new_time))
		
		#store reminder 
		reminders = 1 #new_time
		print(reminders)
		
		#print out confirmation to user
		await self.bot.say("Current time: " + str(curr_time) + ". "+ "Reminder on " + str(t) + " to " + msg + " is set " + author.mention)
		
	async def checkreminder(self):
		while self is self.bot.get_cog("Remindme"):
		#while True:
			print("inside loop")
			if reminders != None:
				if datetime.datetime.now() >= new_time:
					await self.bot.say("It's " + str(t) + author.mention + ". Remember to " + msg + "!")
					reminders = None
			await asyncio.sleep(5)
		
def check_folders():
    folders = ("data", "data/remindme/")
    for folder in folders:
        if not os.path.exists(folder):
            print("Creating " + folder + " folder...")
            os.makedirs(folder)

def check_files():
    if not os.path.isfile("data/remindme/settings.json"):
        print("Creating empty settings.json...")
        dataIO.save_json("data/remindme/settings.json", {})

def setup(bot):
    check_folders()
    check_files()
    thisbot = Remindme(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(thisbot.checkreminder())
    bot.add_cog(thisbot)
