#───────────────────────────────────────────────────────────────#
# ███████╗██╗   ██╗██████╗ ██╗  ██╗ ██████╗ ██████╗ ██╗ █████╗  #
# ██╔════╝██║   ██║██╔══██╗██║  ██║██╔═══██╗██╔══██╗██║██╔══██╗ #
# █████╗  ██║   ██║██████╔╝███████║██║   ██║██████╔╝██║███████║ #
# ██╔══╝  ██║   ██║██╔═══╝ ██╔══██║██║   ██║██╔══██╗██║██╔══██║ #
# ███████╗╚██████╔╝██║     ██║  ██║╚██████╔╝██║  ██║██║██║  ██║ #
# ╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ #
#───────────────────────────────────────────────────────────────#                       
# Coded & maintained by Xellu#1337 | github.com/xellu/euphoria  #
#───────────────────────────────────────────────────────────────#                      

from ast import Break
from calendar import c
from ipaddress import ip_address
import os

try:
    open(".install")
except:
    pass
else:
    os.system("start installer.py")
    os._exit(0)    

try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
try:
    import mouse
except ModuleNotFoundError:
    os.system("pip install mouse")
try:
    import pyautogui
except ModuleNotFoundError:
    os.system("pip install pyautogui")
try:
    import urllib
except ModuleNotFoundError:
    os.system("pip install urllib")
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
try:
    import discord
except ModuleNotFoundError:
    os.system('pip install discord.py')
try:
    import discord_webhook
except ModuleNotFoundError:
    os.system('pip install discord_webhook')
try:
    import zipfile
except ModuleNotFoundError:
    os.system('pip install zipfile')
try:
    import hashlib
except ModuleNotFoundError:
    os.system('pip intall hashlib')
try:
    import base64
except ModuleNotFoundError:
    os.system('pip install base64')

import os
import sys
import time
import json
import mouse
import urllib
import string
import ctypes
import random
import hashlib
import discord
import pyfiglet
import requests
import pyautogui
import subprocess
from zipfile import ZipFile
from colorama import *
from discord import Webhook, RequestsWebhookAdapter
from discord_webhook import *
from urllib.request import Request, urlopen
from discord.ext import *
from discord.ext import commands
from discord import embeds



#───────────────────────────────────────────────────────────────#                      
# VARIABLES                                                     #
#───────────────────────────────────────────────────────────────# 

#--Misc--
database = "https://xello.blue/i/euphoria"
width = os.get_terminal_size().columns
config = json.loads(open("settings/config.json").read())
current = json.loads(open("settings/current.json").read())
userdata = json.loads(open("settings/userdata.json").read())
db_index = json.loads(urlopen(f"{database}/index.json").read())
db_broadcast = json.loads(urlopen(f"{database}/broadcast.json").read())
db_latest = json.loads(urlopen(f"{database}/latest.json").read())

#--Unicode&Colorcodes--
empty_char = "⠀"
channel_space = "᲼"
yellow = "\033[38;5;226m"

#--Config--
token = config["token"]
prefix = config["prefix"]
autoupdate = config["autoupdate"]
notifications = config["notifications"]
consolemode = config["consolemode"]

#--Current--
version = current["version"]
release = current["release"]

#--Codeblock--
codeblock = "```"
footer = f"\n\n[ ᴇᴜᴘʜᴏʀɪᴀ ᴠ ]"
cb_prefix = "ini\n"
cb_error = "css\n"

#--Console--
cmd_prefix = f"{Fore.LIGHTBLACK_EX}>     {Fore.LIGHTBLUE_EX}[E] {Fore.WHITE}"
cmd_input = f"{Fore.LIGHTBLACK_EX}>     {Fore.LIGHTBLUE_EX}[>] {Fore.WHITE}"

#--Selfbot--
euphoria = commands.Bot(command_prefix=prefix, self_bot=True)
euphoria.remove_command('help')

#--Commandlist--
c_help = f"""[Categories]  
{prefix}abuse
{prefix}admin
{prefix}controls
{prefix}fun
{prefix}image
{prefix}text
{prefix}misc
"""

c_abuse = f"""[Abuse]
{prefix}spam <delay> <amount> [message] ─ spams a message for a set amount of times
{prefix}ttsspam <delay> <amount> [message] ─ message spammer using text to speech (/tts)
{prefix}hooksend <message> ─ sends a message through webhook
{prefix}hookdel [url] ─ deletes the inserted webhook
{prefix}hookcreate <amount> ─ creates copious amount of webhooks (max is 10 for each channel)
{prefix}cchat [bypass] ─ clears the chat even if you dont have permissions to do so
{prefix}garbage <amount> ─ spam garbage into the chat
{prefix}basetalk <amount> ─ spams random strings encoded with base64
{prefix}deltroll <amount> ─ sends a large message and then deletes it
"""

c_admin = f"""[Admin]
{prefix}ban <@user> ─ bans a user from the server
{prefix}kick <@user> ─ kicks a user from the server
{prefix}mute <@user> [reason] ─ allows you to mute a user
{prefix}unmute <@user> ─ unmute already muted user
{prefix}createchannel <vc/text> <channel name> ─ easy way create text/voice channel
{prefix}channelspace <channel name> ─ allows you to make a text channel with spaces in the name
{prefix}unlock ─ unlocks the channel 
{prefix}lock ─ locks the channel, usefull against raids
{prefix}purge <amount> ─ clears messages
{prefix}slowmode [delay (s)] ─ changes the channels slowmode
"""

c_controls = f"""[Controls]
{prefix}reboot/r/restart ─ reboot the selfbot
{prefix}exit ─ exits the selfbot
{prefix}update ─ checks if update is available
{prefix}autoupdate ─ toggles autoupdating
{prefix}join ─ join official euphoria discord
{prefix}repo ─ opens github repository
{prefix}cls ─ clears the console
{prefix}setprefix <prefix> ─ change the prefix
{prefix}broadcast ─ sends the current broadcast message
"""

c_fun = f"""[Fun]
{prefix}gayometer [@user] ─ really advanced system to detect how much @tagged_user is gay
{prefix}penis [@user] ─ dick size measurement
{prefix}iqtest [@user] ─ very precisely measures @users iq
{prefix}ip ─ sends randomly generated ip
{prefix}dox <@user> ─ sends randomly generated information about user 
{prefix}empty ─ sends an empty message
{prefix}dice ─ roll a dice
{prefix}roast <@user> ─ roast the sh- out of someone
{prefix}nitro [amount] ─ send random nitro link
"""

c_image = f"""[Image]
{prefix}cat ─ random cat pic
{prefix}dog ─ random dog pic
{prefix}advancement [text] ─ minecraft achievement
{prefix}trash <@user> ─ take out the trash
{prefix}captcha [text] ─ recaptcha
{prefix}meme ─ random meme
"""

c_text = f"""[Text]
{prefix}ascii [text] ─ creates ascii text with a message
{prefix}space <message> ─ makes the message ｓｐａｃｅｄ－ｏｕｔ
{prefix}spoil <text> ─ marks every character of the message as spoiler
{prefix}regional <message> ─ makes every letter of the message emoji
{prefix}leet <text> ─ become real 1337 h4x0r
{prefix}smartass <text> ─ cHaT lIkE a ReAl SmArTaSs
{prefix}counter <amount> [delay (ms)] ─ counts numbers (insane)
{prefix}owo <message> ─ owify your message
{prefix}encode <encryption> ─ encode text to sha256, sha512 or base64
{prefix}decode <string> ─ decode base64 to text
{prefix}zalgo <text> ─ makes your message ẅ̷e̵̓ȋ̷r̵͗d looking
{prefix}morsecode <text> ─ translates text to morsecode
"""

c_misc = f"""[Misc]
{prefix}credits </>
{prefix}mytoken ─ displays your token in the console
""" #add selfpurge

c_credits = f"""[Credits]
Benny's API - https://api.benny.fun/
"""

# {prefix}command ─ desc

#───────────────────────────────────────────────────────────────#                      
# FUNCTIONS                                                     #
#───────────────────────────────────────────────────────────────#   

# print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
# if consolemode == "false":
#     await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}command <argument>\"{footer}{codeblock}")

def selfbot_restart():
    time.sleep(1.5)
    os.system("start euphoria.py")
    print(Fore.BLACK)
    os._exit(0)

def show():
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 1 )

def userdata_save():
    username = f"{euphoria.user.name}#{euphoria.user.discriminator}"
    content = {
        "username": username,
        "id": euphoria.user.id
    }
    json_object = json.dumps(content, indent = 2)
    with open("settings/userdata.json", "w") as outfile:
        outfile.write(json_object)

def pcid():
    pci1 = os.getenv("UserName")
    pci2 = os.getenv("COMPUTERNAME")
    pcid = f"{pci1}@{pci2}"
    return pcid

def updater():
    latest_version = db_index["version"]
    if latest_version != version:
        print(f"{cmd_prefix}{yellow}[TASK] {Fore.WHITE}Update available")
        checks(True)
    else:
        print(f"{cmd_prefix}{yellow}[TASK] {Fore.WHITE}Update isnt available, use \"{prefix}join\" to join official discord & know when update is released")

def checks(update_bypass=False):
    #imports
    latest_version = db_index["version"]
    broadcast = db_index["broadcast"]
    #AUTOUPDATER
    if latest_version != version:
        if autoupdate == "true" or update_bypass == True:
            title()
            try:
                open(".update", "w")
            except Exception as err:
                print(f"{cmd_prefix}{Fore.RED}[AutoUpdater] {Fore.WHITE}Error: {err}")
            else:
                print(f"{cmd_prefix}{yellow}[AutoUpdater] {Fore.WHITE}Please wait, updating in progress..")
                errors = 0
                try:
                    lrelease = db_latest['release']
                    lversion = db_latest['version']
                    content = {
                    "version": lversion,
                    "release": lrelease
                    }
                    json_object = json.dumps(content, indent = 2)
                    with open("settings/current.json", "w") as f:
                        f.write(json_object)
                except Exception as err:
                    errors += 1
                    print(f"{cmd_prefix}{Fore.RED}[AutoUpdater] {Fore.WHITE}Error: {err}")
                else:
                    print(f"{cmd_prefix}{Fore.GREEN}[AutoUpdater] {Fore.WHITE}Success: current.json was updated")
            
                try:
                    download = requests.get(f"{database}/download/euphoria.py")
                    open(f'euphoria.py', 'wb').write(download.content)
                except Exception as err:
                    errors +=1
                    print(f"{cmd_prefix}{Fore.RED}[AutoUpdater] {Fore.WHITE}Error: {err}")
                else:
                    print(f"{cmd_prefix}{Fore.GREEN}[AutoUpdater] {Fore.WHITE}Success: euphoria.py was updated")

                if errors == 0:
                    lversion = db_latest['version']
                    print(f"{cmd_prefix}{yellow}[AutoUpdater] {Fore.WHITE}Successfully updated to {lversion}")
                input("Press any key to reboot")
                os.system("start euphoria.py")
                os.remove(".update")
                os._exit(0)
    #BROADCAST
    if broadcast == "true":
        message = db_broadcast["message"]
        display_type = db_broadcast["display_type"]
        if display_type == "1":
            display_type = "[Broadcast]"
        elif display_type == "2":
            display_type = "[Notification]"
        else:
            display_type = "[Announcement]"
        print(f"{cmd_input}{yellow}{display_type} {Fore.LIGHTBLACK_EX}{message}")

            
def startup():
    clear()
    os.system(f"title Euphoria {version}")
    userdata_save()
    title()
    separator()
    checks()

def clear():
    os.system("cls")

#───────────────────────────────────────────────────────────────#                      
# UIS                                                           #
#───────────────────────────────────────────────────────────────#    

def title():
    print(f"{Fore.LIGHTBLUE_EX}\n\n")
    print("███████╗██╗   ██╗██████╗ ██╗  ██╗ ██████╗ ██████╗ ██╗ █████╗ ".center(width))
    print("██╔════╝██║   ██║██╔══██╗██║  ██║██╔═══██╗██╔══██╗██║██╔══██╗".center(width))
    print("█████╗  ██║   ██║██████╔╝███████║██║   ██║██████╔╝██║███████║".center(width))
    print("██╔══╝  ██║   ██║██╔═══╝ ██╔══██║██║   ██║██╔══██╗██║██╔══██║".center(width))
    print("███████╗╚██████╔╝██║     ██║  ██║╚██████╔╝██║  ██║██║██║  ██║".center(width))
    print("╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝".center(width))
    print(f"Welcome, {euphoria.user}".center(width))

def separator():
    separator_size = width-4
    print(Fore.LIGHTBLUE_EX + " ┌" + "─"*separator_size + "┐ ")
    print(Fore.LIGHTWHITE_EX + f"Prefix: {prefix} | Logged into: {euphoria.user} | Servers: {len(euphoria.guilds)}".center(width))
    print(Fore.LIGHTBLUE_EX + " └" + "─"*separator_size + "┘ ")
    print(yellow + "[LOG]".center(width))
    #┌┐└┘  

#───────────────────────────────────────────────────────────────#                      
# EVENTS                                                        #
#───────────────────────────────────────────────────────────────#    

@euphoria.event #ON READY
async def on_ready():
    startup()

@euphoria.event #ON COMMAND
async def on_command(ctx):
    if ctx.command.name != "purge":
        await ctx.message.delete()
    print(f"{cmd_prefix}{yellow}[COMMAND] {Fore.WHITE}{ctx.command.name}")

@euphoria.event #ON COMMAND ERROR
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        try:
            await ctx.message.delete()
        except:
            pass
    else:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}: {error}")
        if consolemode != "true":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] {error}{footer}{codeblock}")
        await ctx.message.delete()
        
@euphoria.event #BAN DETECTION
async def on_member_ban(guild, user):
    if str(user) == str(euphoria.user):
        print(f"{cmd_prefix}{Fore.RED}[NOTIFICATION]{Fore.WHITE} You were banned in '{guild}' [{guild.id}]")

@euphoria.event #KICK DETECTION
async def on_member_kick(guild, user):
    if str(user) == str(euphoria.user):
        print(f"{cmd_prefix}{Fore.RED}[NOTIFICATION]{Fore.WHITE} You were kicked from '{guild}' [{guild.id}]")

#───────────────────────────────────────────────────────────────#                      
# COMMANDS                                                      #
#───────────────────────────────────────────────────────────────#    

#ABUSE ----------------------------------------------------------

@euphoria.command() #basetalk
async def basetalk(ctx, amount: int=None):
    if amount == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}basetalk <amount>\"{footer}{codeblock}")
    else:
        s = 0
        for i in range(amount):
            message = "".join(random.choice(string.ascii_letters) for i in range(1000))
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            encoded = base64_bytes.decode('ascii')
            await ctx.send(f"{codeblock}{encoded}{codeblock}")
            s += 1
            os.system(f"title Euphoria {version} [Progress: {s}/{amount}]")
        os.system(f"title Euphoria {version}")

@euphoria.command() #garbage
async def garbage(ctx, amount: int=None):
    if amount == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}garbage <amount>\"{footer}{codeblock}")
    else:
        s = 0
        for i in range(amount):
            r_string = "".join(random.choice(string.printable) for i in range(1994))
            await ctx.send(f"{codeblock}{r_string}{codeblock}")
            s += 1
            os.system(f"title Euphoria {version} [Progress: {s}/{amount}]")
        os.system(f"title Euphoria {version}")

@euphoria.command() #deltroll
async def deltroll(ctx, amount: int=None):
    if amount == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}deltroll <amount>\"{footer}{codeblock}")
    else:
        for i in range(amount):
            wall = ""
            for i in range(1000):
                wall += "".join(random.choice(string.digits) for i in range(1)) + "\n"
            await ctx.send(wall, delete_after=1)
            time.sleep(1.5)

@euphoria.command() #cchat
async def cchat(ctx, bypass="false"):
    wall = f"{empty_char}\n"*1000
    if bypass == "false":
        for i in range(7):
            await ctx.send(wall)
    elif bypass == "spam":
        await ctx.send(wall)
    elif bypass == "wall":
        wall = ""
        for i in range(1000):
            wall += "".join(random.choice(string.digits) for i in range(1)) + "\n"
        for i in range(5):
            await ctx.send(wall)
    elif bypass == "both":
        wall = ""
        for i in range(1000):
            wall += "".join(random.choice(string.digits) for i in range(1)) + "\n"
        await ctx.send(wall)
    else:
        await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}cchat [bypass: spam/wall/both]\"{footer}{codeblock}")

@euphoria.command() #webhook
async def webhook(ctx):
    c_list = f"""[Webhook commands]
hooksend - sends a message with webhook (insane)
hookdel - deletes selected webhook
hookcreate - created copious amounts of webhooks

[>] Want more webhook features? try NoteRaw 2.0 right now! 
    > Download: https://github.com/xellu/NoteRaw-2.0/"""
    await ctx.send(f"{codeblock}{cb_prefix}{c_list}{footer}{codeblock}")

@euphoria.command() #hookcreate
async def hookcreate(ctx, amount: int=None, *, name="Euphoria selfbot on top!"):
    if amount == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}hookcreate <amount>\"{footer}{codeblock}")
    else:
        created = 0
        for i in range(amount):
            try:
                await ctx.channel.create_webhook(name=f"Euphoria {version} best")
            except:
                print(f"{cmd_prefix}{Fore.RED}[ERROR] {Fore.WHITE}webhook limit reached")
                if consolemode == "false":
                    await ctx.send(f"{codeblock}{cb_error}[ERROR] webhook limit reached{footer}{codeblock}")
                break
            else:
                created += 1
        await ctx.send(f"{codeblock}{cb_prefix}[E] Successfully created {created} webhooks{footer}{codeblock}")

@euphoria.command() #hookdel
async def hookdel(ctx, url=None):
    if url == None:
        show()
        await ctx.send(f"{codeblock}{cb_prefix}[E] Warning: Please enter a webhook url into the console, otherwise you won't be able to use commands{codeblock}")
        url = input(f"{cmd_input}{yellow}Webhook URL: " + Fore.LIGHTBLACK_EX)
        if url != "":         
            try:
                webhook = Webhook.from_url(f'{url}', adapter=RequestsWebhookAdapter())
                webhook.delete()
            except Exception as err:
                print(f"{cmd_prefix}{Fore.RED}[ERROR] {Fore.WHITE}{err}")
                if consolemode == "false":
                    await ctx.send(f"{codeblock}{cb_error}[ERROR] Check the console to see what happened{footer}{codeblock}")
            else:
                print(f"{cmd_prefix}{yellow}[TASK]{Fore.WHITE} hooksend: successfully sent a message to the webhook") 
                await ctx.send(f"{codeblock}{cb_prefix}[E] Webhook was deleted{footer}{codeblock}")

@euphoria.command() #hooksend
async def hooksend(ctx, *, message=None):
    if message == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}hooksend <message>\"{footer}{codeblock}")
    else:
        show()
        await ctx.send(f"{codeblock}{cb_prefix}[E] Warning: Please enter a webhook url into the console, otherwise you won't be able to use commands{codeblock}")
        url = input(f"{cmd_input}{yellow}Webhook URL: " + Fore.LIGHTBLACK_EX)
        if url != "":
            try:
                hook = DiscordWebhook(url=url, rate_limit_retry=False)
                hook.set_content(message)
                hook.execute()
            except Exception as err:
                print(f"{cmd_prefix}{Fore.RED}[ERROR] {Fore.WHITE}{err}")
                if consolemode == "false":
                    await ctx.send(f"{codeblock}{cb_error}[ERROR] Check the console to see what happened{footer}{codeblock}")
            else:
                print(f"{cmd_prefix}{yellow}[TASK]{Fore.WHITE} hooksend: successfully sent a message to the webhook")   
                await ctx.send(f"{codeblock}{cb_prefix}[E] Message sent{footer}{codeblock}")     

@euphoria.command() #ghostping
async def ghostping(ctx, user: discord.User=None):
    if user == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}ghostping <@user>\"{footer}{codeblock}")
    #IF THE USER IS TAGGED IN THE COMMAND IT WILL BE DELETED AUTOMATICLY

@euphoria.command() #ttsspam
async def ttsspam(ctx, delay: int=None, amount: int=None, *, message="** **"):
    if delay == None or amount == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}ttsspam <delay (ms)> <amount> [message]\"{footer}{codeblock}")
    else:
        sent = 0
        for i in range(amount):
            await ctx.send(message, tts=True)
            sent += 1
            os.system(f"title Euphoria {version} [Progress: {sent}/{amount}]")
            time.sleep(delay/1000)
        os.system(f"title Euphoria {version}")

@euphoria.command() #spam
async def spam(ctx, delay: int=None, amount: int=None, *, message="** **"):
    if delay == None or amount == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}spam <delay (ms)> <amount> [message]\"{footer}{codeblock}")
    else:
        sent = 0
        for i in range(amount):
            await ctx.send(message)
            sent += 1
            os.system(f"title Euphoria {version} [Progress: {sent}/{amount}]")
            time.sleep(delay/1000)
        os.system(f"title Euphoria {version}")

#ADMIN ----------------------------------------------------------

@euphoria.command() #slowmode
async def slowmode(ctx, delay: int=None):
    if delay == None:
        delay = 0
    await ctx.channel.edit(slowmode_delay=delay)

@euphoria.command() #unmute
@commands.has_permissions(manage_channels=True)
async def unmute(ctx, member: discord.Member):
    try:
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    except:
        await ctx.send(f"{codeblock}{cb_error}[E] Error: no muted role was found{footer}{codeblock}")
    else:
        await member.remove_roles(mutedRole)
        await member.send(f"{codeblock}{cb_prefix}[E] You were unmuted from {ctx.guild.name}{codeblock}")
        await ctx.send(f"{codeblock}{cb_prefix}[E] {member} was unmuted{footer}{codeblock}")

@euphoria.command() #mute
@commands.has_permissions(manage_channels=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    try:
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    except:
        await ctx.send(f"{codeblock}{cb_error}[E] Error: no muted role was found{footer}{codeblock}")
    else:
        await member.add_roles(mutedRole)
        if reason == None:
            await member.send(f"{codeblock}{cb_error}[E] You were muted from {ctx.guild.name}{codeblock}")
        else:
            await member.send(f"{codeblock}{cb_error}[E] You were muted from {ctx.guild.name} for \"{reason}\"{codeblock}")
        await ctx.send(f"{codeblock}{cb_prefix}[E] {member} was muted{footer}{codeblock}")

@euphoria.command() #unlock
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f"{codeblock}{cb_prefix}[E] 🔓 Channel was unlocked {footer}{codeblock}")  

@euphoria.command() #lock
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f"{codeblock}{cb_prefix}[E] 🔒 Channel was locked {footer}{codeblock}")   


@euphoria.command() #purge
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int=None):
    if limit == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}purge <amount>\"{footer}{codeblock}")
    else:
        await ctx.channel.purge(limit=limit)
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_prefix}[E] {limit} messages were deleted{footer}{codeblock}", delete_after=3)
        

@euphoria.command() #createchannel
@commands.has_permissions(manage_channels=True)
async def createchannel(ctx, type, *, channel_name=None):
    if channel_name == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}channelspace <channel name>\"{footer}{codeblock}")
    else:
        if type == "vc":
            await ctx.guild.create_voice_channel(channel_name)
            type = "voice"
        else:
            await ctx.guild.create_text_channel(channel_name)
            type = "text"
        await ctx.send(f"{codeblock}{cb_prefix}[E] Created {type} channel{footer}{codeblock}")

@euphoria.command() #channelspace
@commands.has_permissions(manage_channels=True)
async def channelspace(ctx, *, channel_name=None):
    if channel_name == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}channelspace <channel name>\"{footer}{codeblock}")
    else:
        output_name = ""
        for letter in channel_name:
            if letter == " ":
                output_name += channel_space
            else:
                output_name += letter
        try:
            await ctx.guild.create_text_channel(output_name)
        except Exception as err:
            print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}: {err}")
            if consolemode == "false":
                await ctx.send(f"{codeblock}{cb_error}[E] Error: {err}{footer}{codeblock}")
        else:
            await ctx.send(f"{codeblock}{cb_prefix}[E] Created channel named \"{output_name}\"{footer}{codeblock}")

@euphoria.command() #kick
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User=None, reason=None):
    if reason == None:
        reason = "no reason provided"
    if user == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}kick <@user>\"{footer}{codeblock}")
    elif user == ctx.message.author:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] {ctx.command.name}: cannot kick yourself\"{footer}{codeblock}")
    else:
        await user.send(f"{codeblock}{cb_error}[E] You were kicked from {ctx.guild.name} for: \"{reason}\"{footer}{codeblock}")
        try:
            await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name} was kicked{footer}{codeblock}")
        except:
            pass
        await user.kick(reason=reason)
        print(f"{cmd_prefix}{yellow}[KICK] {Fore.WHITE}You kicked {user} from {ctx.guild.name} for {reason}")

@euphoria.command() #ban
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User=None, reason=None):
    if reason == None:
        reason = "no reason provided"
    if user == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}ban <@user>\"{footer}{codeblock}")
    elif user == ctx.message.author:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] {ctx.command.name}: cannot ban yourself\"{footer}{codeblock}")
    else:
        await user.send(f"{codeblock}{cb_error}[E] You were banned from {ctx.guild.name} for: \"{reason}\"{footer}{codeblock}")
        try:
            await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name} was banned{footer}{codeblock}")
        except:
            pass
        await user.ban(reason=reason)
        print(f"{cmd_prefix}{yellow}[BAN] {Fore.WHITE}You banned {user} from {ctx.guild.name} for {reason}")

#CONTROLS -------------------------------------------------------

@euphoria.command() #setprefix
async def setprefix(ctx, *, newprefix=None):
    if newprefix == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}setprefix <prefix>\"{footer}{codeblock}")
    else:
        content = {
                "token": token,
                "prefix": newprefix,
                "autoupdate": "false",
                "notifications": notifications,
                "consolemode": consolemode
            }
        json_object = json.dumps(content, indent = 5)
        with open("settings/config.json", "w") as f:
            f.write(json_object)
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_prefix}[E] Please wait...{footer}{codeblock}")
        selfbot_restart()

@euphoria.command() #mytoken
async def mytoken(ctx):
    print(f"{cmd_prefix}{yellow}[TASK] {Fore.WHITE}User Token: {token}")
    if consolemode == "false":
        await ctx.send(f"{codeblock}{cb_prefix}[E] Token was sent into the console{footer}{codeblock}")

@euphoria.command() #broadcast
async def broadcast(ctx):
    db_index = json.loads(urlopen(f"{database}/index.json").read())
    db_broadcast = json.loads(urlopen(f"{database}/broadcast.json").read())
    toggle = db_index["broadcast"]
    if toggle == "true":
        message = db_broadcast["message"]
        display_type = db_broadcast["display_type"]
        if display_type == "1":
            display_type = "[Broadcast]"
        elif display_type == "2":
            display_type = "[Notification]"
        else:
            display_type = "[Announcement]"
        await ctx.send(f"{codeblock}{cb_prefix}> {display_type}: {message}{footer}{codeblock}")
        print(f"{cmd_input}{yellow}{display_type} {Fore.LIGHTBLACK_EX}{message}")
    else:
        print(f"{cmd_prefix}{Fore.RED}[ERROR] {Fore.WHITE}Broadcast is disabled")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[E] Broadcast is disabled{footer}{codeblock}")

@euphoria.command() #cls
async def cls(ctx):
    await ctx.send(f"{codeblock}{cb_error}[E] Clearing...{footer}{codeblock}")
    startup()

@euphoria.command() #update
async def update(ctx):
    updater()

@euphoria.command() #autoupdate
async def autoupdate(ctx):
    if autoupdate == "true":
        content = {
            "token": token,
            "prefix": prefix,
            "autoupdate": "false",
            "notifications": notifications,
            "consolemode": consolemode
        }
        json_object = json.dumps(content, indent = 5)
        with open("settings/config.json", "w") as f:
            f.write(json_object)
        toggle = "True"
    else:
        content = {
            "token": token,
            "prefix": prefix,
            "autoupdate": "false",
            "notifications": notifications,
            "consolemode": consolemode
        }
        json_object = json.dumps(content, indent = 5)
        with open("settings/config.json", "w") as f:
            f.write(json_object)
        toggle = "False"
    await ctx.send(f"{codeblock}ini\n[E] autoupdater switched to: {toggle}{footer}{codeblock}")

@euphoria.command() #repo
async def repo(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}[E] Please wait..{footer}{codeblock}")
    os.system(f"start \"\" https://github.com/xellu/euphoria/")

@euphoria.command() #join
async def join(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}Joining...{footer}{codeblock}")
    discord_invite = "https://discord.gg/kjh9bEytUH"
    os.system(f"start \"\" {discord_invite}")

@euphoria.command() #exit
async def exit(ctx):
    exit_message = random.randint(1, 5)
    if exit_message == 1:
        exit_message = "See you soon!"
    elif exit_message == 2:
        exit_message = "Thank you for using euphoria <3"
    elif exit_message == 3:
        exit_message = f"Goodbye {euphoria.name}!"
    elif exit_message == 4:
        exit_message = "Hope we'll meet again."
    else:
        exit_message = f"Farewell {euphoria.name}."
    await ctx.send(f"{codeblock}{cb_prefix}[E] {exit_message}{footer}{codeblock}")
    show()
    print(f"\n\n{yellow}" + f"{exit_message}".center(width) + "\n\n")
    time.sleep(1)
    os._exit(0)

@euphoria.command() #reboot
async def reboot(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}[E] Rebooting..{footer}{codeblock}", delete_after=1)
    selfbot_restart()

@euphoria.command() #restart
async def restart(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}[E] Rebooting..{footer}{codeblock}", delete_after=1)
    selfbot_restart()

@euphoria.command() #r
async def r(ctx):
    await ctx.send(f"{codeblock}{cb_prefix}[E] Rebooting..{footer}{codeblock}", delete_after=1)
    selfbot_restart()

#FUN ------------------------------------------------------------

@euphoria.command() #roast
async def roast(ctx, user: discord.User=None):
    if user == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}roast <@user>\"{footer}{codeblock}")
    else:
        r = json.loads(requests.get("https://api.benny.fun/v1/roast").text)
        roast = r["text"]
        await ctx.send(f"{user.mention} {roast}")

@euphoria.command() #dox
async def dox(ctx, user: discord.User=None):
    if user == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}dox <@user>\"{footer}{codeblock}")
    else:
        #general
        ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        faketoken = "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(40, 50)))
        nameid = random.randint(1,5)
        lastnameid = random.randint(1,6)
        if nameid == 1:
            name = "David"
        elif nameid == 2:
            name = "Aidan"
        elif nameid == 3:
            name = "Martina"
        elif nameid == 4:
            name = "Alexa"
        else:
            name = "Jack"
        if lastnameid == 1:
            lastname = "Bullard"
        elif lastnameid == 2:
            lastname = "Sinclair"
        elif lastnameid == 3:
            lastname = "Romijnsen"
        elif lastnameid == 4:
            lastname = "Smith"
        else:
            lastname = "Newell"
        fullname = f"{name} {lastname}"
        age = random.randint(13,50)
        #creditcard
        card_num = "".join(random.choice(string.digits) for i in range(16))
        card_cvc = "".join(random.choice(string.digits) for i in range(3))
        typeid = random.randint(1,2)
        if typeid == 1:
            type = "MasterCard"
        else:
            type = "Visa"
        content = f"""[ {user.name} DOX ]

[>] GENERAL:
Name: {fullname}
Age: {age}
Ip: {ip}
Token: {faketoken}
Discord: {user}

[>] CREDIT CARD:
Number: {card_num}
Expiration date: {random.randint(1,12)}/{random.randint(25, 29)}
Card holder: {fullname}
CVC: {card_cvc}
Company: {type}
        """
        await ctx.send(f"{codeblock}{cb_prefix}{content}{footer}{codeblock}")


@euphoria.command() #iqtest
async def iqtest(ctx, user: discord.User=None):
    if user == None:
        user = euphoria.user
    iq = random.randint(0,150)
    if iq < 100:
        await ctx.send(f"{codeblock}{cb_error}[E] {user.name} failed the iq test{footer}{codeblock}")
    else:
        await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name} passed the iq test with {iq} IQ{footer}{codeblock}")

@euphoria.command() #penis
async def penis(ctx, user: discord.User=None):
    size = random.randint(0,15)
    if user == None:
        user = euphoria.user
    dick = "8"
    for i in range(size):
        dick += "="
    dick += "D"
    await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name}'s penis: {dick}{footer}{codeblock}")

@euphoria.command() #gayometer
async def gayometer(ctx, user: discord.User=None):
    if user == None:
        user = euphoria.user
    await ctx.send(f"{codeblock}{cb_prefix}[E] {user.name} is {random.randint(0,100)}% gay{footer}{codeblock}")

@euphoria.command() #ip
async def ip(ctx):
    await ctx.send(f"{codeblock}{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}{codeblock}")

@euphoria.command() #empty
async def empty(ctx):
    await ctx.send("** **")

@euphoria.command() #dice
async def dice(ctx):
    emojiid = random.randint(1,6)
    if emojiid == 1:
        emoji = ":one:"
    elif emojiid == 2:
        emoji = ":two:"
    elif emojiid == 3:
        emoji = ":three:"
    elif emojiid == 4:
        emoji = ":four:"
    elif emojiid == 5:
        emoji = ":five:"
    else:
        emoji = ":six:"
    await ctx.send(emoji)
    
@euphoria.command() #nitro
async def nitro(ctx, amount: int=1):
    if amount > 10:
        amount = 10
    message = ""
    for i in range(amount):
        code = "https://discord.gift/" + "".join(random.choice(string.ascii_letters) for i in range(16))
        message += f"{code} "
    await ctx.send(message)

#IMAGE ----------------------------------------------------------

@euphoria.command() #avatar
async def avatar(ctx, user: discord.User=None):
    if user == None:
        avatar = euphoria.user.avatar_url
    else:
        avatar = user.avatar_url
    await ctx.send(avatar)

@euphoria.command() #captcha
async def captcha(ctx, text="Euphoria on top"):
    text_encode = ""
    for letter in text:
        if letter == " ":
            text_encode += "%20"
        else:
            text_encode += letter
    await ctx.send(f"https://api.benny.fun/v1/captcha?text={text_encode}")

@euphoria.command() #trash
async def trash(ctx, user: discord.User=None):
    if user == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}trash <@user>\"{footer}{codeblock}")
    else:
        face = euphoria.user.avatar_url
        trash = user.avatar_url
        await ctx.send(f"https://api.benny.fun/v1/trash?face={face}&trash={trash}")

@euphoria.command() #fakemsg
async def fakemsg(ctx, user: discord.User,*, text):
    username = user.name
    avatar = user.avatar_url
    username_encode = ""
    text_encode = ""
    for letter in username:
        if letter == " ":
            username_encode += "%20"
        else:
            username_encode += letter
    for letter in text:
        if letter == " ":
            text_encode += "%20"
        else:
            text_encode += letter
    await ctx.send(f"https://api.benny.fun/v1/discordmessage?text={text_encode}&username={username_encode}&avatar={avatar}")

@euphoria.command() #advancement
async def advancement(ctx, text="Euphoria on top"):
    output = ""
    for letter in text:
        if letter == " ":
            output += "%20"
        else:
            output += letter
    await ctx.send(f"https://api.benny.fun/v1/achievement?text={output}")

@euphoria.command() #meme
async def meme(ctx):
    r = json.loads(requests.get("https://api.benny.fun/v1/meme").text)
    url = r["meme"]
    await ctx.send(url)

@euphoria.command() #dog
async def dog(ctx):
    r = json.loads(requests.get("https://api.benny.fun/v1/dog").text)
    url = r["image"]
    await ctx.send(url)

@euphoria.command() #cat
async def cat(ctx):
    r = json.loads(requests.get("https://api.benny.fun/v1/cat").text)
    url = r["image"]
    await ctx.send(url)

#TEXT -----------------------------------------------------------

@euphoria.command() #encode
async def encode(ctx, type=None, *, string=None):
    if string == None or type == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}encode <sha512/sha256/base64> <string>\"{footer}{codeblock}")
    else:
        if type == "sha256":
            output = \
                hashlib.sha256(string.encode()).hexdigest()
            success = True
        elif type == "sha512":
            output = \
                hashlib.sha512(string.encode()).hexdigest()
            success = True
        elif type == "base64":
            string_bytes = string.encode('ascii')
            base64_bytes = base64.b64encode(string_bytes)
            output = base64_bytes.decode('ascii')
            success = True
        else:
            success = False
        if success == True:
            await ctx.send(f"{codeblock}{cb_prefix}[E] Encoded string: {output}{footer}{codeblock}")
        else:
            print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}: invalid encryption type")
            if consolemode == "false":
                await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}encode <sha512/sha256/base64> <string>\"{footer}{codeblock}")

@euphoria.command() #decode
async def decode(ctx, *, string=None):
    if string == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}decode <string>\"{footer}{codeblock}")
    else:
        output = base64.b64decode(string)
        await ctx.send(f"{codeblock}{cb_prefix}[E] Decoded text: {output}{footer}{codeblock}")

@euphoria.command() #morsecode
async def morsecode(ctx, *, text=None):
    if text == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}morsecode <message>\"{footer}{codeblock}")
    else:
        text = text.upper()
        DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
        output = ''
        for letter in text:
            if letter != ' ':
                output += DICT[letter] + ' '
            else:
                output += ' '
        await ctx.send(output)

@euphoria.command() #count
async def counter(ctx, amount :int=None, delay=500):
    if amount == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}count <amount> [delay (ms)]\"{footer}{codeblock}")
    else:
        num = 0
        for i in range(amount):
            num += 1
            await ctx.send(num)
            time.sleep(delay/1000)

@euphoria.command() #owo
async def owo(ctx, *, text=None):
    whitelist = "rRlL"
    DICT = {
        "r": "w", "R": "W", "l": "w", "L": "W"
    }
    if text == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}owo <text>\"{footer}{codeblock}")
    else:
        output = ""
        for letter in text:
            if letter in whitelist:
                output += DICT[letter]
            else:
                output += letter
        await ctx.send(output)

@euphoria.command() #smartass
async def smartass(ctx, *, text=None):
    if text == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}regional <text>\"{footer}{codeblock}")
    else:
        caps = 0
        output = ""
        for letter in text:
            if caps == 0:
                output += letter.upper()
                caps += 1
            else:
                output += letter.lower()
                caps = 0
        await ctx.send(output)

@euphoria.command() #regional
async def regional(ctx, *, text=None):
    if text == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}regional <text>\"{footer}{codeblock}")
    else:
        regional_prefix = ":regional_indicator_"
        letter_whitelist = "abcdefghijklmnopqrstuvwxyz"
        number_whitelist = "0123456789"
        text = text.lower()
        output = ""
        for letter in text:
            if letter in letter_whitelist:
                output += f"{regional_prefix}{letter}:"
            elif letter in number_whitelist:
                if letter == "1":
                    output += ":one:"
                elif letter == "2":
                    output += ":two:"
                elif letter == "3":
                    output += ":three:"
                elif letter == "4":
                    output += ":four:"
                elif letter == "5":
                    output += ":five:"
                elif letter == "6":
                    output += ":six:"
                elif letter == "7":
                    output += ":seven:"
                elif letter == "8":
                    output += ":eight:"
                elif letter == "9":
                    output += ":nine:"
            elif letter == " ":
                output += "   "            
        await ctx.send(output)

@euphoria.command() #ascii
async def ascii(ctx, *, text=None):
    if text == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}ascii <text>\"{footer}{codeblock}")
    else:
        output = pyfiglet.figlet_format(text)
        await ctx.send(f"{codeblock}{output}{codeblock}")

@euphoria.command() #zalgo
async def zalgo(ctx, *, text=None):
    if text == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}zalgo <message>\"{footer}{codeblock}")
    else:
        output = ""
        zalgochar = "̷̞̟̇"
        for letter in text:
            output += f"{letter}{zalgochar}"
        await ctx.send(output)

@euphoria.command() #spoil
async def spoil(ctx, *, text=None):
    if text == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}spoil <message>\"{footer}{codeblock}")
    else:
        output = ""
        for letter in text:
            output += f"||{letter}||"
        await ctx.send(output)

@euphoria.command() #leet
async def leet(ctx, *, text=None):
    if text == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}leet <message>\"{footer}{codeblock}")
    else:
        output = ""
        text = text.upper()
        DICT = {"L": "1", "I": "1", "E": "3", "A": "4", "S": "5", "T": "7", "O": "0"}
        for letter in text:
            if letter != " ":
                try:
                    output += DICT[letter]
                except:
                    output += letter
            else:
                output += " "
        await ctx.send(output)

@euphoria.command() #space
async def space(ctx, *, text=None):
    if text == None:
        print(f"{cmd_prefix}{Fore.RED}[COMMAND ERROR] {Fore.WHITE}{ctx.command.name}")
        if consolemode == "false":
            await ctx.send(f"{codeblock}{cb_error}[ERROR] USAGE: \"{prefix}space <message>\"{footer}{codeblock}")
    else:
        output = ""
        for letter in text:
            output += f"{letter} "
        await ctx.send(output)

#MISC -----------------------------------------------------------

#HELP -----------------------------------------------------------

@euphoria.command() #help
async def help(ctx):
    await ctx.send(f"{codeblock}ini\n{c_help}{footer}{codeblock}")

@euphoria.command() #abuse
async def abuse(ctx):
    await ctx.send(f"{codeblock}ini\n{c_abuse}{footer}{codeblock}")

@euphoria.command() #admin
async def admin(ctx):
    await ctx.send(f"{codeblock}ini\n{c_admin}{footer}{codeblock}")

@euphoria.command() #controls
async def controls(ctx):
    await ctx.send(f"{codeblock}ini\n{c_controls}{footer}{codeblock}")

@euphoria.command() #fun
async def fun(ctx):
    await ctx.send(f"{codeblock}ini\n{c_fun}{footer}{codeblock}")

@euphoria.command() #image
async def image(ctx):
    await ctx.send(f"{codeblock}ini\n{c_image}{footer}{codeblock}")

@euphoria.command() #text
async def text(ctx):
    await ctx.send(f"{codeblock}ini\n{c_text}{footer}{codeblock}")

@euphoria.command() #misc
async def misc(ctx):
    await ctx.send(f"{codeblock}ini\n{c_misc}{footer}{codeblock}")


#───────────────────────────────────────────────────────────────#

try:
    euphoria.run(token, bot=False)
except:
    print("[Euphoria] Invalid token")
    input("Press any key to continue... ")

# Coded by Xellu#1337 with ♡