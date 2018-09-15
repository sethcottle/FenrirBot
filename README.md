# 🐺 FenrirBot
### A simple Discord bot for Illidan's Fenrir guild.

This is version 0.1.0 of this Discord bot. We haven't quite decided on all of the tasks we would like for it to perform. Right now, the purpose is to give guild members a quick set of commands to access guild information on the fly. A guild member could use the command `!raid` and the bot would return the current raid times for the guild.

![`!raid` command](https://i.imgur.com/pcjXDHU.gif)

## Prerequisites

To connect your bot, you're going to need create a new application from within the [Discord Developer Portal](https://discordapp.com/developers). [Discord.py](https://discordpy.readthedocs.io/en/rewrite/discord.html) has a nice little guide to walk you through the process if you need help.

You'll need somewhere to run a small [.py](https://fileinfo.com/extension/py) application. We used  [Raspberry Pi 3 Model B+](https://www.amazon.com/ELEMENT-Element14-Raspberry-Pi-Motherboard/dp/B07BDR5PDW?tag=cottle-20) so we could quickly get a proof of concept of our bot out.

## Hardware

[Fenrir](https://fenrirguild.com) is a _really_ small guild, so we didn't need anything fancy to get FenrirBot up and running - especially having such a small scope with release 0.1.0.

I have a [Raspberry Pi 3 Model B+](https://www.amazon.com/ELEMENT-Element14-Raspberry-Pi-Motherboard/dp/B07BDR5PDW?tag=cottle-20) sitting on my desk, that's it!

## Software
I have the Pi running the latest version of [Raspbian Stretch Lite](https://www.raspberrypi.org/downloads/raspbian/) (June 2018 release at the time of this writing). The version of shipped with Python 3.5.3, but I went ahead and upgraded to 3.6.6 (since I've had issues using pip on the Pi running 3.7 in the past & for this, it's good enough).



#### Prerequisites for Python 3.6.X

Install the latest build tools.

```$ sudo apt-get update
$ sudo apt-get install build-essential tk-dev
$ sudo apt-get install libncurses5-dev libncursesw5-dev libreadline6-dev
$ sudo apt-get install libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev
$ sudo apt-get install libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev  
```

You should already have most of these, but `libssl-dev` is important for making sure pip would be working once I upgraded to 3.6.X. Better safe than sorry I suppose.

_If one of the packages above cannot be found, try a newer version number (e.g. `libdb5.4-dev` instead of `libdb5.3-dev`)._

_Optional: Purge the source code and previously installed packages._    

```$ sudo rm -r Python-3.6.6
$ rm Python-3.6.6.tgz
$ sudo apt-get --purge remove build-essential tk-dev
$ sudo apt-get --purge remove libncurses5-dev libncursesw5-dev libreadline6-dev
$ sudo apt-get --purge remove libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev
$ sudo apt-get --purge remove libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
$ sudo apt-get autoremove
$ sudo apt-get clean
```

#### Getting the latest version of Python

[Grab the latest version of Python](https://www.python.org/downloads/). I'm using Python 3.6.6 for this project.

`$ get https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz`

Extract the .tgz with `$ tar xzvf Python-3.6.6.tgz`

Go into the directory with `$ cd Python-3.6.6/`

Run `$ ./configure` to check for dependencies, this should only take a few minutes.

Compile using `$ make`, this could take quite some time so be patient.

Now we'll install Python 3.6.6 with `$ sudo make install`

Last but not least, reboot `$ sudo reboot`.

#### Configure the Discord bot

Install the latest version of [Discord.py](https://github.com/Rapptz/discord.py).

`$ python3 -m pip install -U discord.py`

Now we'll setup a directory for FenrirBot.

`$ mkdir ~/fenrirbot`

Move into the directory you just created.

`$ cd ~/fenrirbot`

Create a new file.

`$ touch bot.py`

Edit that file with nano.

`$ nano bot.py`

You can copy/paste our simple code to get started. Just be sure to replace `TOKEN` with [your bot's token](https://discordpy.readthedocs.io/en/rewrite/discord.html) to get things working.

```
import discord
from discord.ext import commands

TOKEN = 'TOKEN'

description = '''FenrirBot | For the Horde!'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def raid():
    """will display our current raiding schedule."""
    await bot.say("We'll be raiding every Monday & Wednesday at 9:00PM EST")

@bot.command()
async def pug():
    """will give you the URL to invite temporary members to the Discord Server."""
    await bot.say("Invite PUG members using: LINK REVOKED")

@bot.command()
async def hello():
    """FenrirBot will respond back."""
    await bot.say("Hello, Champion!")


bot.run(TOKEN)
```

Save the edits you've made in `nano` with `CTRL+X` and `y`.

Now you can run your bot! `$ python3 bot.py`
You can also run using `$ nohup python3 -u ~/fenrirbot/bot.py &`. `nohup` will allow the task to continue running after you terminate your SSH connection. `&` is going to run the task in the background to keep the terminal open for use. There is also an issue where the script auto-terminates after 2-3 hours, I've opened [Issue 1](https://github.com/sethcottle/FenrirBot/issues/1) but I haven't had time to work on it. Learn more in the issue on setting up a Cron job to keep the bot running.

#### Give it a whirl
Now your bot should show an online status.

![Online Status](https://i.imgur.com/Gm9XsS2.png)

Quickly test your bots response by issuing the `!help` command.

##### Thanks for checking out this simple project for Fenrir.
