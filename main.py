import keep_alive
import os
from discord import channel
from discord.colour import Color
from discord.ext import commands
import discord
from geopy.geocoders import Nominatim
from discord import Member
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
import random_topic
import randfacts
import requests
import json  
import keep_alive
from discord import *
import urllib.request 
import time 
import geocoder
geolocator = Nominatim(user_agent="geoapiExercises")
bot = commands.Bot(command_prefix='-') #change it to whatever you want
bot.remove_command("help")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! :rocket: {0}'.format(round(bot.latency, 1)))
    
@bot.command()
async def info(ctx):
  em = discord.Embed(title="Information:",description="International Space Station")
  em.add_field(name="Basic",value="The ISS is a multi-national collaborative effort to study conditions in space, to further understand the effects of micro-gravity, radiation, etc on the human body. Scientists from participating countries conduct experiments here.")
  em.add_field(name="Participating nations", value=" Canada, Japan, the Russian Federation, the United States, and eleven Member States of the European Space Agency (Belgium, Denmark, France, Germany, Italy, The Netherlands, Norway, Spain, Sweden, Switzerland and the United Kingdom)")
  em.add_field(name="Official NASA site", value="https://www.nasa.gov/mission_pages/station/main/index.html")
  em.add_field(name="Wiki site",value="https://en.wikipedia.org/wiki/International_Space_Station")
  em.add_field(name="Official National Lab site",value="https://www.issnationallab.org/about/iss-timeline/")
  em.set_footer(text="The ISS bot")
  await ctx.send(embed=em)    

@bot.command()
async def about(ctx):
  em = discord.Embed(title="About the ISS Bot", value="~")
  em.add_field(name="GitHub link",value="https://github.com/Sachit71/ISS-Info-Bot ISS Bot is an open source bot!")
  em.add_field(name="Head dev",value="cyber#3709")
  em.set_footer(text="The ISS bot")
  await ctx.send(embed=em)

@bot.command()
async def live(ctx):
  await ctx.send("https://iss-1.blyons.repl.co/")

@bot.command()
async def location(ctx):
  url = "http://api.open-notify.org/iss-now.json"
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())

  # Extract the ISS location
  location = result["iss_position"]
  lat = location['latitude']
  lon = location['longitude']

  # Ouput lon and lat to the terminal
  latz = str(lat)
  long = str(lon)
  print(lat,lon)
  #print("\nLatitude: " + str(lat))
  #print("\nLongitude: " + str(lon))
  location = geolocator.reverse(latz+","+long)
  print(location)
  y = [latz, long]

  em = discord.Embed(title="Location",description="Shows the current location of the ISS")
  em.add_field(name="Location:", value=location)
  em.add_field(name="Co-ordinates",value=y)
  em.set_footer(text="The ISS bot")
  await ctx.send(embed=em)

@bot.event
async def on_ready():
    activity = discord.Game(name="", type=3) #you can change from playing to watching, etc 
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")

@bot.command()
async def topic(ctx):
    topic=random_topic.get_topic()
    await ctx.send(topic)

@bot.command()
async def facts(ctx):
    
    x = randfacts.get_fact()
    await ctx.send(x)

@bot.command()
async def help(ctx):
  em = discord.Embed(title="Command list:", description="Command list for the ISS Bot")
  em.add_field(name="`-help`",value="Shows this embed")
  em.add_field(name="`-location`",value="Fetches you the location of the ISS")
  em.add_field(name="`-info`",value="Get basic info about the ISS and other inmportant links")
  em.add_field(name="`-about`",value="Get GitHub and developer info")
  em.add_field(name="`-facts`", value="Gives you random facts")
  em.add_field(name="`-topic`",value="Get a random topic to talk about")
  em.add_field(name="`-live`",value="Get a website to look at the Live camera and location of the ISS!")
  em.add_field(name="`Note`",value="Location over oceans and seas are shown as **None**")
  em.set_footer(text="Upvote us on top.gg!")
  await ctx.send(embed=em)
  
keep_alive.keep_alive()    
bot.run('Your bot token here')
