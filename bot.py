import discord
import hypixel
import random
import string
from discord.ext import commands
import datetime
import os, re, io
import time
import math
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure, MissingPermissions
from Cybernator import Paginator as pag
from PIL import Image
import matplotlib.pyplot as plt

bot = commands.Bot(command_prefix = "/")
bot.remove_command('help')


classes = ["Hunter", "Zombie", "Creeper", "Arcanist", "Shaman", "Dreadlord", "Golem", "Squid", "Moleman", "Enderman", "Herobrine", "Blaze",
           "Pigman", "Spider", "Werewolf", "Pirate", "Phoenix", "Skeleton", "Assassin", "Renegade", "Snowman", "Automaton", "Cow", "Shark"]



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('/help'))
    
    print(bot.user.name + " is ready.")

# @bot.command(pass_context=True)
# async def servers(ctx):
#     client = discord.Client()
#     servers = list(client.guilds)
#     print("Connected on " + str(len(client.guilds)) + " servers:")
#     for x in range(len(servers)):
#         print(" "+servers[x-1].name)


@bot.command(pass_context=True)
async def servers(ctx):
    servers = list(bot.guilds)
    print(f"Connected to {str(len(servers))} servers:")
    print('\n'.join(server.name for server in servers))











@bot.command(aliases=['stats', 'hypixel', 'statistics'])
async def info(ctx, name=None):
    if name is None:
        name = ctx.message.author.display_name
    # name is None
    # await ctx.send(f'Command Currently Unavailable!')
    try:
        data = hypixel.hypixel_api(name)
        data2 = hypixel.hypixel_api2(name)

        ign = hypixel.get_displayname(name, data)

        level = hypixel.get_level(name, data2)
        karma = hypixel.get_karma(name, data2)
        achievementPoints = hypixel.get_achievementPoints(name, data2)
        quests = hypixel.get_quests(name, data2)
    except:
        await ctx.send(f"Player `{name}` is not found!")
    version = hypixel.get_mcVersionRp(name, data)
    firstLogin = hypixel.get_firstLogin(name, data)
   
    dt_firstLogin = datetime.datetime.utcfromtimestamp(round(firstLogin/1000))
    try:
        lastLogin = hypixel.get_lastLogin(name, data)
        dt_lastLogin = datetime.datetime.utcfromtimestamp(round(lastLogin/1000))
    except:
        lastLogin = "Unknown"
        dt_lastLogin = "Unknown"



    embed1 = discord.Embed(
    title = 'Jagares Bot',
    colour = discord.Colour.orange()
    )



    # embed.set_author(name='w')
    embed1.add_field(name='IGN', value=f'{ign}', inline=False)
    embed1.add_field(name='Level', value=f'{level}', inline=False)
    embed1.add_field(name='Karma', value=f"{'{:,}'.format(karma)}", inline=False)
    embed1.add_field(name='Achievement Points', value=f"{'{:,}'.format(achievementPoints)}", inline=False)
    embed1.set_footer(text="© 2020 LazBoi All Rights Reserved | Page 1/3 ")



    embed2 = discord.Embed(
    title = 'Jagares Bot',
    colour = discord.Colour.orange()
    )



    # embed.set_author(name='w')


    embed2.add_field(name='Quests Completed', value=f"{'{:,}'.format(quests)}", inline=False)
    embed2.add_field(name='Version', value=f'{version}', inline=False)
    embed2.add_field(name='First Login', value=f'{dt_firstLogin} UTC', inline=False)
    embed2.add_field(name='Last Login', value=f'{dt_lastLogin} UTC', inline=False)
    embed2.set_footer(text="© 2020 LazBoi All Rights Reserved | Page 2/3 ")



    embed3 = discord.Embed(
    title = 'Jagares Bot',
    colour = discord.Colour.orange()
    )



    # embed.set_author(name='w')


    embed3.set_image(url=f"https://minotar.net/armor/body/{ign}.png")
    embed3.set_footer(text="© 2020 LazBoi All Rights Reserved | Page 3/3 ")

    embeds = [embed1, embed2, embed3]

    message = await ctx.send(embed=embed1)

    page = pag(bot, message, only=ctx.author, footer=False, use_more=False, embeds = embeds, language='en',use_exit=False, exit_reaction=["⏹"])

    if level == 0:
        await ctx.send("Player not found! (Make sure to use their Minecraft username)")
    else:
         await page.start()



@bot.command()
async def help(ctx):
    

    embed1 = discord.Embed(
    title = 'Jagares Bot',
    colour = discord.Colour.orange()
    )


    
    embed1.set_author(name='Commands')

    embed1.add_field(name='Mega Walls Stats', value='/mw <player>', inline=False)
    embed1.add_field(name='Mega Walls Class Points', value='/cp <player>', inline=False)
    embed1.add_field(name='Mega Walls Class Stats', value='/mwclass <class> <player>', inline=False)
    embed1.add_field(name='Blitz Survival Games Stats', value='/bsg <player>', inline=False)
    embed1.add_field(name='Info', value='/info <player>', inline=False)
    embed1.add_field(name='Guild Info', value='/guild <player>', inline=False)
    embed1.add_field(name='Watchdog/Staff Stats', value='/watchdog', inline=False)


    embed1.set_footer(text="© 2020 LazBoi All Rights Reserved | Page 1/3 ")


    embed2 = discord.Embed(
    title = 'Jagares Bot',
    colour = discord.Colour.orange()
    )


    
    embed2.set_author(name='Commands')

    embed2.add_field(name='Guild Cape', value='/gcape', inline=False)
    embed2.add_field(name='8ball', value='/8ball <question>', inline=False)
    embed2.add_field(name='Good Night', value='/gn <person>', inline=False)
    embed2.add_field(name='Duel', value='/duel <player1> <player2>', inline=False)


    embed2.set_footer(text="© 2020 LazBoi All Rights Reserved | Page 2/3 ")



    embed3 = discord.Embed(
    title = 'Jagares Bot',
    colour = discord.Colour.orange()
    )


    
    embed3.set_author(name='Commands')

    embed3.add_field(name='Pet Image', value='/dog/cat/bird/panda', inline=False)
    embed3.add_field(name='Lyrics', value='/lyrics <song>', inline=False)
    embed3.add_field(name='Bot Chat', value='/chat <message>', inline=False)
    embed3.add_field(name='Shoutout', value='/shoutout', inline=False)

    embed3.set_footer(text="© 2020 LazBoi All Rights Reserved | Page 3/3 ")


    embeds = [embed1, embed2, embed3]
    message = await ctx.send(embed=embed1)
    page = pag(bot, message, footer=False, only=ctx.author, use_more=False, embeds = embeds, language='en',use_exit=False, exit_reaction=["⏹"])

    await page.start()




@bot.command(aliases=['sync', 'link'])
async def verify(ctx, name):
    
    data = hypixel.hypixel_api(name)
    ign = hypixel.get_displayname(name, data)

    newPackageRank = hypixel.get_newPackageRank(name, data)
    monthlyPackageRank = hypixel.get_monthlyPackageRank(name, data)


    playerDiscord = hypixel.get_playerDiscord(name, data)
    username = ctx.message.author
    # userId = ctx.message.author.id

    embedSuccess = discord.Embed(colour = discord.Colour.green())
    embedSuccess.set_author(name='Jagares Bot')
    embedSuccess.add_field(name=f'Verified', value=f"Your discord account has been linked.", inline=False)
    embedSuccess.set_footer(text="© 2020 LazBoi All Rights Reserved ")

    embedFail = discord.Embed(colour = discord.Colour.red())
    embedFail.set_author(name='Jagares Bot')
    embedFail.add_field(name=f'Error', value=f"You need to link your discord on hypixel.", inline=False)
    embedFail.set_footer(text="© 2020 LazBoi All Rights Reserved ")

    embedNotMatch = discord.Embed(colour = discord.Colour.red())
    embedNotMatch.set_author(name='Jagares Bot')
    embedNotMatch.add_field(name=f'Error', value=f"Your current discord account and hypixel discord tag don't match.", inline=False)
    embedNotMatch.set_footer(text="© 2020 LazBoi All Rights Reserved ")


    # await ctx.send(f'username: {username} \nplayerDiscord: {playerDiscord}')


    if ctx.channel.id == 787080811064328283:
        if playerDiscord is None:
            await ctx.send(embed=embedFail)


        elif str(username) == str(playerDiscord):
            try:
                await ctx.send(embed=embedSuccess)

                time.sleep(1)








                await ctx.message.author.edit(nick=ign)
                await username.add_roles(discord.utils.get(username.guild.roles, name="Verified"))
                await username.add_roles(discord.utils.get(username.guild.roles, name="Community Members"))
                





                if newPackageRank == "VIP":
                    await username.add_roles(discord.utils.get(username.guild.roles, name="VIP"))
                elif newPackageRank == "VIP_PLUS":
                    await username.add_roles(discord.utils.get(username.guild.roles, name="VIP+"))
                elif newPackageRank == "MVP":
                    await username.add_roles(discord.utils.get(username.guild.roles, name="MVP"))
                elif newPackageRank == "MVP_PLUS":
                    await username.add_roles(discord.utils.get(username.guild.roles, name="MVP+"))



                if monthlyPackageRank == "SUPERSTAR":
                    await username.add_roles(discord.utils.get(username.guild.roles, name="MVP++"))



                # await ctx.channel.purge(limit=7)

                
            except Exception as e:
                await ctx.send(f'Error: `{e}`')


            
        elif str(username) != str(playerDiscord):
            await ctx.send(embed=embedNotMatch)        

        time.sleep(5)

        await ctx.channel.purge(limit=25)
    else:
        await ctx.send(f'You can only verify in `#verification`')






@bot.command(aliases=['8ball', 'eightball', 'ateball'])
async def _8Ball(ctx, *, question):
    responses = ['It is certain', 
                 'It is decidedly so', 
                 'Without a doubt', 
                 'Yes – definitely', 
                 'You may rely on it', 
                 'As I see it, yes', 
                 'Most likely', 
                 'jajajajaja', 
                 'Yes Signs point to yes', 
                 'YEP LMAOOO', 'try again', 
                 'Ask again later', 
                 'Better not tell you now', 
                 'Cannot predict now', 
                 'Concentrate and ask again', 
                 'Dont count on it', 
                 'My reply is no', 
                 'My sources say no', 
                 'yep yep yep', 
                 'Very doubtful']

    await ctx.send(f'{random.choice(responses)}')

@bot.command(aliases=['guildcape'])
async def gcape(ctx):
    username = ctx.message.author
    if get(username.roles, id=519612131738386441):
        capes = ['https://www.needcoolshoes.com/banner?=aapfaiavpyac', 
                    'https://www.needcoolshoes.com/banner?=paafpipvaypc', 
                    'https://www.needcoolshoes.com/banner?=pamfpipvmypc', 
                    'https://www.needcoolshoes.com/banner?=pajfpipvjypc', 
                    'https://www.needcoolshoes.com/banner?=paffpipvfypc', 
                    'https://www.needcoolshoes.com/banner?=paefpipveypc', 
                    'https://www.needcoolshoes.com/banner?=pakfpipvkypc', 
                    'https://www.needcoolshoes.com/banner?=palfpipvlypc', 
                    'https://www.needcoolshoes.com/banner?=paofpipvoypc', 
                    'https://www.needcoolshoes.com/banner?=pabfpipvbypc', 
                    'https://www.needcoolshoes.com/banner?=aalfaiavlyac', 
                    'https://www.needcoolshoes.com/banner?=aaofaiavoyac', 
                    'https://www.needcoolshoes.com/banner?=aabfaiavbyac', 
                    'https://www.needcoolshoes.com/banner?=aakfaiavkyac', 
                    'https://www.needcoolshoes.com/banner?=aamfaiavmyac', 
                    'https://www.needcoolshoes.com/banner?=aaefaiaveyac', 
                    'https://www.needcoolshoes.com/banner?=aaffaiavfyac', 
                    'https://www.needcoolshoes.com/banner?=japfjijvpyjc', 
                    'https://www.needcoolshoes.com/banner?=fapffifvpyfc', 
                    'https://www.needcoolshoes.com/banner?=eapfeievpyec',
                    'https://www.needcoolshoes.com/banner?=mapfmimvpymc',
                    'https://www.needcoolshoes.com/banner?=kapfkikvpykc',
                    'https://www.needcoolshoes.com/banner?=lapflilvpylc',
                    'https://www.needcoolshoes.com/banner?=oapfoiovpyoc',
                    'https://www.needcoolshoes.com/banner?=bapfbibvpybc',
                    'https://www.needcoolshoes.com/banner?=dalfdidvlydc',
                    'https://www.needcoolshoes.com/banner?=fajffifvjyfc',
                    'https://www.needcoolshoes.com/banner?=fakffifvkyfc',
                    'https://www.needcoolshoes.com/banner?=labflilvbylc', 
                    'https://www.needcoolshoes.com/banner?=gapfgigvpygc', 
                    'https://www.needcoolshoes.com/banner?=jaffjijvfyjc']

        await ctx.send(f'Generated A Guild Cape {random.choice(capes)}')
    else:
        await ctx.send(f'Only Guild Members Can Generate Guild Capes!')

@bot.command(pass_context=True)
async def give(ctx, role=None):
    lazid = ctx.message.author.id 
    if lazid == 535137720981520384:
        pass
    else:
        await ctx.send(f'Command Failed')




@bot.command()
async def gn(ctx, *, Object="bird"):
    
    await ctx.send(f'gn {Object}')

@bot.command(aliases=['Bhoppare', 'xhealz', 'bhopper'])
async def bhoppare(ctx):
    
    await ctx.send(f'https://tenor.com/view/xhealz-megawalls-dreadlord-bhop-minecraft-gif-17190956')


@bot.command(pass_context=True, aliases=['discord'])

async def dc(ctx):
    username = ctx.message.author
    if get(username.roles, id=519612131738386441):
        await ctx.send(f'https://discord.gg/88qd5TX')
    else:
        await ctx.send(f'Only Guild Members Have Access To This Command!')
 
		    
@bot.command()
async def apply(ctx):
    embed = discord.Embed(
    title = f"Apply For Jagares",
    colour = discord.Colour.orange()
    )
    embed.add_field(name='\u200b', value=f"[apply here](https://hypixel.net/threads/%E2%98%95%EF%B8%8F-jagares-jag-%E2%98%95%EF%B8%8F-level-89-%E2%98%95%EF%B8%8F-mega-walls-more-%E2%98%95%EF%B8%8F-top-100-%E2%98%95%EF%B8%8F-events-%E2%98%95%EF%B8%8F.2490194/)", inline=True)

    # await ctx.send(f'https://hypixel.net/threads/%E2%98%95%EF%B8%8F-jagares-jag-%E2%98%95%EF%B8%8F-level-89-%E2%98%95%EF%B8%8F-mega-walls-more-%E2%98%95%EF%B8%8F-top-100-%E2%98%95%EF%B8%8F-events-%E2%98%95%EF%B8%8F.2490194/')
    await ctx.send(embed=embed)
		    
@bot.command(pass_context=True, aliases=['clear'])
@has_permissions(manage_messages=True)
async def purge(ctx, ammount=3):
    await ctx.channel.purge(limit=ammount+1)

		    

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        		    	    
        await ctx.send("You don't have the permission to delete messages.")
		    

		    
# @bot.command(pass_context=True)
# @has_permissions(manage_messages=True)
# async def say(ctx, *, msg):
#     await ctx.send(f"{msg}")		    
		    
		    
# @say.error
# async def say_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
        		    	    
#         await ctx.send("Looks like you don't have the permissions.")		    



# @bot.command()
# async def chat(ctx, *, message):
#     Message = hypixel.chat_api(message)
    
#     await ctx.send(f'{Message}')


# @bot.command()
# async def seth(ctx):
    
#     await ctx.send(f'lmao the guy who skips you mean?')


# @bot.command()
# async def cijaye(ctx):
    
#     await ctx.send(f'lmao the guy who stays you mean?')



# @bot.command(aliases=['44hp', '44HP', 'wouter'])
# async def _44HP(ctx):
    
#     await ctx.send(f'lmao the guy who never dies you mean?')



# @bot.command()
# async def lyrics(ctx, *, title):
    


#     try:
#         Title = hypixel.lyrics_api(title)['title']
#         Author = hypixel.lyrics_api(title)['author']
#         Lyrics = hypixel.lyrics_api(title)['lyrics']    
#         await ctx.send(f'Title: {Title} - {Author}')
#         await ctx.send('\u200b')
#         await ctx.send('%.2000s' % Lyrics)
    
#     except:
 

#         await ctx.send(f'Song not found')



# @bot.command(aliases=['SO'])
# async def shoutout(ctx):
#     shoutouts = ['Shoutout to 44HP', 
#                  'Shoutout to Cijaye', 
#                  'Shoutout to TheManOfCake', 
#                  'Shoutout to Sethlol', 
#                  'Shoutout to Shtruz', 
#                  'Shoutout to UnityPusheen', 
#                  'Shoutout to LessYou', 
#                  'Shoutout to Rom', 
#                  'Shoutout to Dagals', 
#                  'Shoutout to OhWellDone', 
#                  'Shoutout to LazBoi', 
#                  'Shoutout to Non', 
#                  'Shoutout to 7mu', 
#                  'Shoutout to Souls', 
#                  'Shoutout to Pijaye', 
#                  'Shoutout to BAKERTHEBAGELMAN', 
#                  'Shoutout to JediKnight625', 
#                  'Shoutout to BlackKnight625', 
#                  'Shoutout to Tqqn', 
#                  'Shoutout to BurnBlade']

#     await ctx.send(f'{random.choice(shoutouts)}')















@bot.command()
async def bird(ctx):
    img_link = hypixel.bird_img_api()
    
    await ctx.send(f'{img_link}')

@bot.command()
async def dog(ctx):
    img_link = hypixel.dog_img_api()
    
    await ctx.send(f'{img_link}')


@bot.command()
async def cat(ctx):
    img_link = hypixel.cat_img_api()
    
    await ctx.send(f'{img_link}')

@bot.command()
async def panda(ctx):
    img_link = hypixel.panda_img_api()
    
    await ctx.send(f'{img_link}')







# def uuid_or_name(input):
#     uuid_pattern = re.compile(r'^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-5][0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$', re.IGNORECASE)
#     uuid_matches = uuid_pattern.finditer(input)

#     mcname_pattern = re.compile(r'^\w{1,16}$', re.IGNORECASE)
#     mcname_matches = mcname_pattern.finditer(input)
#     result = None
#     if list(uuid_matches) != []:
#         # await ctx.send('uuid')
#         result = "uuid"
#     elif list(mcname_matches) != []:
#         # await ctx.send('name')
#         result = "mcname"
#     else:
#         # await ctx.send('invalid')
#         result = "Input-Error"
#     return result











@bot.command()
async def duel(ctx, p1=None, p2=None):

    players = [p1, p2]
    if p1 is None:
        await ctx.send(f'`First` Player argument is missing.')

    elif p2 is None:
        await ctx.send(f'`Second` Player argument is missing.')
    
    elif p1 is None and p2 is None:
        await ctx.send(f'`Both` Player arguments are missing.')
        await ctx.send(f'/duel <Player1> <Player2>')

    else:
        await ctx.send(f'`{random.choice(players)}` won the duel.')




@bot.command()
async def mw(ctx, name=None):
    if name is None:
        name = ctx.message.author.display_name
    # result = uuid_or_name(name)
    # await ctx.send(result)

    data = hypixel.hypixel_api(name)
    try:
        ign = hypixel.get_displayname(name, data)
    except:
        await ctx.send(f"Player `{name}` is not found!")

    final_kills = hypixel.get_final_kills(name, data) 
    wins = hypixel.get_wins(name, data)
    fds1 = hypixel.get_final_deaths_post(name, data)
    fds2 = hypixel.get_final_deaths_pre(name, data)
    losses = hypixel.get_losses(name, data)
    coins = hypixel.get_coins(name, data)
    chosen_class = hypixel.get_chosen_class(name, data)
    chosen_skin = hypixel.get_chosen_skin(name, chosen_class, data)
    wither_damage = hypixel.get_wither_damage(name, data)
    mythic_favor = hypixel.get_mythic_favor(name, data)
    cakes_found = hypixel.get_cakes_found(name, data)
    fas = hypixel.get_final_assists(name, data)
    fds = fds1 + fds2
    cps = final_kills + fas + (wins * 10)



    if chosen_skin == chosen_class:
        chosen_skin = "Default"

    if chosen_skin == "none":
        chosen_skin = "Default"



    if fds == 0:
        fkd = final_kills
    else:
        fkd = round(final_kills/fds, 2)
    
    if losses == 0:
        wl = wins
    else:
        wl = round(wins/losses,  2)


    next_fkd = math.floor(fkd + 1)

    if fds == 0:
        need_fks = next_fkd - final_kills
    else:
        need_fks = (fds * next_fkd) - final_kills






    rand = get_random_string(12)
    
    embed = discord.Embed(
    title = f'{ign}',
    colour = discord.Colour.orange()
    )



    embed.set_author(name='Jagares Bot', icon_url=f"https://minotar.net/helm/{ign}/400")
    embed.add_field(name='Final Kills', value=f"`{'{:,}'.format(final_kills)}`", inline=True)
    embed.add_field(name='Final Assists', value=f"`{'{:,}'.format(fas)}`", inline=True)
    embed.add_field(name='Final Deaths', value=f"`{'{:,}'.format(fds)}`", inline=True)
    embed.add_field(name='FK/D Ratio', value=f'`{fkd}`', inline=True)
    embed.add_field(name=f'Finals For {next_fkd} FK/D Ratio', value=f"``{'{:,}'.format(need_fks)}``", inline=True)
    embed.add_field(name='Wins', value=f"`{'{:,}'.format(wins)}`", inline=True)
    embed.add_field(name='Losses', value=f"`{'{:,}'.format(losses)}`", inline=True)
    embed.add_field(name='W/L Ratio', value=f"`{'{:,}'.format(wl)}`", inline=True)
    embed.add_field(name='Coins', value=f"`{'{:,}'.format(coins)}`", inline=True)
    embed.add_field(name='Mythic Favor', value=f"`{'{:,}'.format(mythic_favor)}`", inline=True)
    embed.add_field(name='Wither Damage', value=f"`{'{:,}'.format(wither_damage)}`", inline=True)
    embed.add_field(name='Chosen Class', value=f"`{chosen_class}`", inline=True)
    embed.add_field(name='Cakes Found', value=f"`{'{:,}'.format(cakes_found)}`", inline=True)
    embed.add_field(name='Class Points', value=f"`{'{:,}'.format(cps)}`", inline=True)
    embed.add_field(name='Chosen Skin', value=f"`{chosen_skin}`", inline=True)
    embed.set_image(url=f"https://gen.plancke.io/mw/{ign}/2.png?random={rand}")

    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")

    await ctx.send(embed=embed)

@bot.command()
async def cp(ctx, name=None):
    if name is None:
        name = ctx.message.author.display_name
    data = hypixel.hypixel_api(name)
    try:
        ign = hypixel.get_displayname(name, data)
    except:
        await ctx.send(f"Player `{name}` is not found!")


       

    
    embed = discord.Embed(
    title = f"{ign}'s class points",
    colour = discord.Colour.orange()
    )



    embed.set_author(name='Jagares Bot', icon_url=f"https://minotar.net/helm/{ign}/400")

    for Class in classes:
        class_points = (hypixel.get_class_wins(name, Class, data) * 10) + hypixel.get_class_finals(
            name, Class, data) + hypixel.get_class_final_assists(name, Class, data)
        embed.add_field(name=f'{Class.capitalize()}',
                        value=f"{'{:,}'.format(class_points)}", inline=True)


    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")

    await ctx.send(embed=embed)








@bot.command(aliases=['class', 'mwc'])
async def mwclass(ctx, Class, name=None):
    if name is None:
        name = ctx.message.author.display_name

    if Class.capitalize() == "Hun":
        Class = "Hunter"
    elif Class.capitalize() == "Zom":
        Class = "Zombie"
    
    elif Class.capitalize() == "Cre":
        Class = "Creeper"
    
    elif Class.capitalize() == "Arc":
        Class = "Arcanist"
    
    elif Class.capitalize() == "Sha":
        Class = "Shaman"
    
    elif Class.capitalize() == "Dre" or Class.capitalize() == "Dreadroad" or Class.capitalize() == "Dread":
        Class = "Dreadlord"

    elif Class.capitalize() == "Gol":
        Class = "Golem"

    elif Class.capitalize() == "Squ" or Class.capitalize() == "Sqd":
        Class = "Squid"
    
    elif Class.capitalize() == "Mol" or Class.capitalize() == "Mole" or Class.capitalize() == "Mm":
        Class = "Moleman"
    
    elif Class.capitalize() == "End" or Class.capitalize() == "Endy":
        Class = "Enderman"
    
    elif Class.capitalize() == "Hbr" or Class.capitalize() == "Hb" or Class.capitalize() == "Him":
        Class = "Herobrine"
    
    elif Class.capitalize() == "Bla":
        Class = "Blaze"
    
    elif Class.capitalize() == "Pig":
        Class = "Pigman"
    
    elif Class.capitalize() == "Spi":
        Class = "Spider"
    
    elif Class.capitalize() == "Wer" or Class.capitalize() == "Ww":
        Class = "Werewolf"
    
    elif Class.capitalize() == "Pir":
        Class = "Pirate"
    
    elif Class.capitalize() == "Phx":
        Class = "Phoenix"
    
    elif Class.capitalize() == "Ske" or Class.capitalize() == "Skele":
        Class = "Skeleton"
    
    elif Class.capitalize() == "Asn":
        Class = "Assassin"
    
    elif Class.capitalize() == "Ren":
        Class = "Renegade"
    
    elif Class.capitalize() == "Sno":
        Class = "Snowman"
    
    elif Class.capitalize() == "Aut" or Class.capitalize() == "Atn" or Class.capitalize() == "Auto":
        Class = "Automaton"
    
    elif Class.capitalize() == "Shr" or Class.capitalize() == "Srk":
        Class = "Shark"
    
   
    

    if Class.capitalize() in classes:
        
        data = hypixel.hypixel_api(name)
        try:
            ign = hypixel.get_displayname(name, data)
        except:
            await ctx.send(f"Player `{name}` is not found!")
        class_final_kills = hypixel.get_class_finals(name, Class, data)
        class_final_assists = hypixel.get_class_final_assists(name, Class, data)
        class_wins = hypixel.get_class_wins(name, Class, data)
        # class_final_deaths = hypixel.get_class_final_deaths(name, Class, data)
        # class_losses = hypixel.get_class_losses(name, Class, data)

        class_cp = class_wins * 10 + class_final_kills + class_final_assists



        class_final_kills_all = hypixel.get_class_finals_all(name, Class, data)
        class_final_assists_all = hypixel.get_class_final_assists_all(name, Class, data)
        class_wins_all = hypixel.get_class_wins_all(name, Class, data)
        class_final_deaths_all = hypixel.get_class_final_deaths_all(name, Class, data)
        class_losses_all = hypixel.get_class_losses_all(name, Class, data)

        class_games_all = class_wins_all + class_losses_all
        if class_games_all == 0:
            class_cpg = class_cp
        else:
            class_cpg = round(class_cp / class_games_all, 2)


        if class_final_deaths_all == 0:
            class_fkd = class_final_kills_all
        else:
            class_fkd = round(class_final_kills_all/class_final_deaths_all, 2)
        if class_losses_all == 0:
            class_wlr = class_wins_all
        else:
            class_wlr = round(class_wins_all/class_losses_all, 2)


        class_next_fkd = math.floor(class_fkd + 1)

        if class_final_deaths_all == 0:
            class_need_fks = class_next_fkd - class_final_kills_all
        else:
            class_need_fks = (class_final_deaths_all * class_next_fkd) - class_final_kills_all



        rand = get_random_string(12)


        embed = discord.Embed(
        title = f"{ign}'s {Class.capitalize()} Stats",
        colour = discord.Colour.orange()
        )


        embed.set_author(name='Jagares Bot', icon_url=f"https://minotar.net/helm/{ign}/400")

        embed.add_field(name=f'FKs | FAs', value=f"`{'{:,}'.format(class_final_kills_all)}`   `{'{:,}'.format(class_final_assists_all)}`", inline=False)
        # embed.add_field(name=f'Final Assists', value=f"`{'{:,}'.format(class_final_assists_all)}`", inline=False)
        embed.add_field(name=f'Wins | Losses', value=f"`{'{:,}'.format(class_wins_all)}`   `{'{:,}'.format(class_losses_all)}`", inline=False)
        embed.add_field(name=f'FK/D | W/L', value=f"`{'{:,}'.format(class_fkd)}`   `{'{:,}'.format(class_wlr)}`", inline=False)
        # embed.add_field(name=f'W/L Ratio', value=f"`{'{:,}'.format(class_wlr)}`", inline=False)   
        embed.add_field(name=f'Finals For {class_next_fkd} FK/D Ratio', value=f"`{'{:,}'.format(class_need_fks)}`", inline=False)
        # embed.add_field(name=f'Losses', value=f"`{'{:,}'.format(class_losses_all)}`", inline=False)
        embed.add_field(name=f'Final Deaths', value=f"`{'{:,}'.format(class_final_deaths_all)}`", inline=False)
        embed.add_field(name=f'Class Points', value=f"`{'{:,}'.format(class_cp)}`", inline=False)
        embed.add_field(name=f'Class Point/Game', value=f"`{'{:,}'.format(class_cpg)}`", inline=False)

        embed.set_image(url=f"https://gen.plancke.io/mwclass/{ign}/{Class.capitalize()}.png?random={rand}")
        embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")




        await ctx.send(embed=embed)
    else:
         await ctx.send(f"`{Class}` class does not exist!")







@bot.command(aliases=['compare'])
async def classcompare(ctx, Class, name1, name2=None):
    if name2 is None:
        name2 = ctx.message.author.display_name


    data1 = hypixel.hypixel_api(name1)
    try:
        ign1 = hypixel.get_displayname(name1, data1)
    except:
        await ctx.send(f"Player `{name1}` is not found!")
    class_final_kills1 = hypixel.get_class_finals(name1, Class, data1)
    class_final_assists1 = hypixel.get_class_final_assists(name1, Class, data1)
    class_wins1 = hypixel.get_class_wins(name1, Class, data1)
    # class_final_deaths = hypixel.get_class_final_deaths(name, Class, data)
    # class_losses = hypixel.get_class_losses(name, Class, data)

    class_cp1 = class_wins1 * 10 + class_final_kills1 + class_final_assists1



    class_final_kills_all1 = hypixel.get_class_finals_all(name1, Class, data1)
    class_final_assists_all1 = hypixel.get_class_final_assists_all(name1, Class, data1)
    class_wins_all1 = hypixel.get_class_wins_all(name1, Class, data1)
    class_final_deaths_all1 = hypixel.get_class_final_deaths_all(name1, Class, data1)
    class_losses_all1 = hypixel.get_class_losses_all(name1, Class, data1)
    


    if class_final_deaths_all1 == 0:
        class_fkd1 = class_final_kills_all1
    else:
        class_fkd1 = round(class_final_kills_all1/class_final_deaths_all1, 2)
    if class_losses_all1 == 0:
        class_wlr1 = class_wins_all1
    else:
        class_wlr1 = round(class_wins_all1/class_losses_all1, 2)




    data2 = hypixel.hypixel_api(name2)
    try:
        ign2 = hypixel.get_displayname(name2, data2)
    except:
        await ctx.send(f"Player `{name2}` is not found!")
    class_final_kills2 = hypixel.get_class_finals(name2, Class, data2)
    class_final_assists2 = hypixel.get_class_final_assists(name2, Class, data2)
    class_wins2 = hypixel.get_class_wins(name2, Class, data2)
    # class_final_deaths = hypixel.get_class_final_deaths(name, Class, data)
    # class_losses = hypixel.get_class_losses(name, Class, data)

    class_cp2 = class_wins2 * 10 + class_final_kills2 + class_final_assists2



    class_final_kills_all2 = hypixel.get_class_finals_all(name2, Class, data2)
    class_final_assists_all2 = hypixel.get_class_final_assists_all(name2, Class, data2)
    class_wins_all2 = hypixel.get_class_wins_all(name2, Class, data2)
    class_final_deaths_all2 = hypixel.get_class_final_deaths_all(name2, Class, data2)
    class_losses_all2 = hypixel.get_class_losses_all(name2, Class, data2)
    


    if class_final_deaths_all2 == 0:
        class_fkd2 = class_final_kills_all2
    else:
        class_fkd2 = round(class_final_kills_all2/class_final_deaths_all2, 2)
    if class_losses_all2 == 0:
        class_wlr2 = class_wins_all2
    else:
        class_wlr2 = round(class_wins_all2/class_losses_all2, 2)



    if class_cp1 > class_cp2:
        class_cp_dif = class_cp1 - class_cp2
    elif class_cp1 < class_cp2:
        class_cp_dif = class_cp2 - class_cp1
    else:
        class_cp_dif = 0


    if class_final_kills_all1 > class_final_kills_all2:
        class_fks_dif = class_final_kills_all1 - class_final_kills_all2
    elif class_final_kills_all1 < class_final_kills_all2:
        class_fks_dif = class_final_kills_all2 - class_final_kills_all1
    else:
        class_fks_dif = 0

    if class_wins_all1 > class_wins_all2:
        class_win_dif = class_wins_all1 - class_wins_all2
    elif class_wins_all1 < class_wins_all2:
        class_win_dif = class_wins_all2 - class_wins_all1
    else:
        class_win_dif = 0








    # rand = get_random_string(12)


    embed = discord.Embed(
    title = f"`{ign1} | {ign2}`",
    colour = discord.Colour.orange()
    )


    embed.set_author(name=f'{Class.capitalize()}')

    embed.add_field(name=f'Final Kills', value=f"`{'{:,}'.format(class_final_kills_all1)} | {'{:,}'.format(class_final_kills_all2)}`", inline=False)
    embed.add_field(name=f'Final Assists', value=f"`{'{:,}'.format(class_final_assists_all1)} | {'{:,}'.format(class_final_assists_all2)}`", inline=False)
    embed.add_field(name=f'FK/D Ratio', value=f"`{'{:,}'.format(class_fkd1)} | {'{:,}'.format(class_fkd2)}`", inline=False)
    embed.add_field(name=f'Wins', value=f"`{'{:,}'.format(class_wins_all1)} | {'{:,}'.format(class_wins_all2)}`", inline=False)
    embed.add_field(name=f'Losses', value=f"`{'{:,}'.format(class_losses_all1)} | {'{:,}'.format(class_losses_all2)}`", inline=False)
    embed.add_field(name=f'W/L Ratio', value=f"`{'{:,}'.format(class_wlr1)} | {'{:,}'.format(class_wlr2)}`", inline=False)   
    embed.add_field(name=f'Class Points', value=f"`{'{:,}'.format(class_cp1)} | {'{:,}'.format(class_cp2)}`", inline=False)
    embed.add_field(name=f'Final Kills Difference', value=f"`{'{:,}'.format(class_fks_dif)}`", inline=False)
    embed.add_field(name=f'Wins Difference', value=f"`{'{:,}'.format(class_win_dif)}`", inline=False)
    embed.add_field(name=f'Class Points Difference', value=f"`{'{:,}'.format(class_cp_dif)}`", inline=False)


    # embed.set_image(url=f"https://gen.plancke.io/mwclass/{ign}/{Class.capitalize()}.png?random={rand}")
    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")




    await ctx.send(embed=embed)










#GUILD COMMANDS
#GUILD COMMANDS
#GUILD COMMANDS







@bot.command()
async def guild(ctx, name):
    # name is None
    # await ctx.send(f'Command Currently Unavailable!')
    data = hypixel.hypixel_api(name)
    gdata = hypixel.hypixel_gapi(name)
    try:
        guild_name = hypixel.get_guild_name(name, gdata)
    except:
        await ctx.send("Guild not found!")
    guild_members = hypixel.get_guild_members(name, gdata)


    try:
        guild_tag_color = str(gdata["guild"]["tagColor"]).capitalize()
    except:
        guild_tag_color = "Gray"
    
    try:
        guild_tag = str(gdata["guild"]["tag"])
    except:
        guild_tag = "none"



    # if guild_tag_color == "yellow":
    #     guild_tag_color = "#ddcd37"
    # elif guild_tag_color == "dark_green":
    #     guild_tag_color = "#0d7e14"
    # elif guild_tag_color == "dark_aqua":
    #     guild_tag_color = "#0da7ab"
    # guild_description = hypixel.get_guild_description(name, gdata)
    # guild_exp = hypixel.get_guild_exp(name, gdata)
    # guild_date = datetime.datetime.utcfromtimestamp(round(hypixel.get_guild_date(name, gdata)/1000))
    # guild_exp_history = hypixel.get_guild_exp_history(name, gdata)

    embed = discord.Embed(
    # title = 'Jagares Bot',
    colour = discord.Colour.orange()
    )




    exp = [0, 0, 0, 0, 0, 0, 0]
    expEachDay = []
    k = 0
    expValue = ""
    for member in guild_members:
        i = 0
        for dailyExpHistory in member["expHistory"]:
            exp[i] += member["expHistory"][dailyExpHistory]
            i = i + 1
        if member["rank"] == "Guild Master":
            owner_uuid = member["uuid"]
            owner_name = hypixel.hypixel_api(owner_uuid)["player"]["displayname"]
    for dailyExpHistory in member["expHistory"]:
        expValue += f"{dailyExpHistory} ➠ **{'{:,}'.format(exp[k])}** \n"
        expEachDay.append(dailyExpHistory)
        k = k + 1 
    
    ranks = ["Guild Master"]
    rank_tags = ["GM"]
    for rank in gdata["guild"]["ranks"]:
        try:
            ranks.append(rank["name"])
            rank_tags.append(rank["tag"])
        except:
            pass
        if rank["default"] == True:
            try:
                default_rank = rank["name"]
                default_rank_tag = rank["tag"]
            except:
                pass
            
        
    guild_stats = f'''
Guild Name ➠ **{guild_name}**
Guild Tag ➠ **{guild_tag}**
Tag Color ➠ **{guild_tag_color}**
Guild Master ➠ **{owner_name}**
Default Rank ➠ **{default_rank} [{default_rank_tag}]**
    '''

    guild_ranks = f'''
Guild Name ➠ **{guild_name}**
Guild Tag ➠ **{guild_tag}**
Tag Color ➠ **{guild_tag_color}**
Guild Master ➠ **{owner_uuid}**

    '''


    embed.set_author(name=f'{guild_name} [{guild_tag}]')



    embed.add_field(name=f'Stats', value=guild_stats, inline=False)


    
    embed.add_field(name=f'Weekly Experience', value=expValue, inline=False)
    expEachDay.reverse()
    exp.reverse()

    plt.figure(figsize=(10, 4))
    axis_x = expEachDay
    axis_y = exp
    plt.style.use("ggplot")
    plt.plot(axis_x, axis_y, label="Guild Exp",  linewidth=3, color="#ec9b00", marker="o")
    plt.ticklabel_format(axis="y", style="plain")
    # plt.tight_layout()
    # plt.title("test", size=30)
    plt.legend()
    plt.savefig("graph.png", transparent=False, bbox_inches='tight')
    img = discord.File("graph.png", filename="graph.png")
    embed.set_image(url="attachment://graph.png")






    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")
    await ctx.send(file=img, embed=embed)







#WATCHDOG
#WATCHDOG
#WATCHDOG





@bot.command(aliases=['wd', 'staff', 'hackisban'])
async def watchdog(ctx):
    
    wddata = hypixel.hypixel_wdapi()

    wd_last = hypixel.get_watchdog_last(wddata)
    wd_daily = hypixel.get_watchdog_daily(wddata)
    wd_total = hypixel.get_watchdog_total(wddata)
    staff_daily = hypixel.get_staff_daily(wddata)
    staff_total = hypixel.get_staff_total(wddata)


    embed = discord.Embed(
    title = f"Watchdog Stats",
    colour = discord.Colour.orange()
    )


    embed.set_author(name='Jagares Bot')
    try:
        embed.add_field(name=f'Watchdog Bans Last Minute', value=f"{'{:,}'.format(wd_last)}", inline=False)
        embed.add_field(name=f'Watchdog Bans Daily', value=f"{'{:,}'.format(wd_daily)}", inline=False)
        embed.add_field(name=f'Watchdog Bans Total', value=f"{'{:,}'.format(wd_total)}", inline=False)
        embed.add_field(name=f'Staff Bans Daily', value=f"{'{:,}'.format(staff_daily)}", inline=False)
        embed.add_field(name=f'Staff Bans Total', value=f"{'{:,}'.format(staff_total)}", inline=False)
    except:
         embed.add_field(name=f'Watchdog Stats', value=f"Watchdog Stats Unavailable", inline=False)

    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")
    await ctx.send(embed=embed)





@bot.command(aliases=['name', 'namehistory'])
async def nh(ctx, name=None):
    if name is None:
        name = ctx.message.author.display_name
    
    data = hypixel.hypixel_api(name)
    try:
        ign = hypixel.get_displayname(name, data)
    except:
        await ctx.send(f"Player `{name}` is not found!")

    nameHistory = hypixel.get_knownAliases(name, data)
    nameHistory.reverse()

    nameLength = len(nameHistory)
    pages = str(math.ceil(len(nameHistory) / 10))

    embed1 = discord.Embed(
    title = f"{ign}'s Name History",
    colour = discord.Colour.orange()
    )


    embed1.set_author(name='Jagares Bot')


    for value in nameHistory[0:9]:
        embed1.add_field(name=f'\u200b', value=f"``{value}`` \u200b", inline=False)
    

    embed1.set_footer(text=f"© 2020 LazBoi All Rights Reserved | Page 1/{pages} ")




    embed2 = discord.Embed(
    title = f"{ign}'s Name History",
    colour = discord.Colour.orange()
    )


    embed2.set_author(name='Jagares Bot')


    for value in nameHistory[10:19]:
        embed2.add_field(name=f'\u200b', value=f"``{value}`` \u200b", inline=False)
    

    embed2.set_footer(text=f"© 2020 LazBoi All Rights Reserved | Page 2/{pages} ")




    embed3 = discord.Embed(
    title = f"{ign}'s Name History",
    colour = discord.Colour.orange()
    )


    embed3.set_author(name='Jagares Bot')


    for value in nameHistory[20:29]:
        embed3.add_field(name=f'\u200b', value=f"``{value}`` \u200b", inline=False)
    

    embed3.set_footer(text=f"© 2020 LazBoi All Rights Reserved | Page 3/{pages} ")



    embed4 = discord.Embed(
    title = f"{ign}'s Name History",
    colour = discord.Colour.orange()
    )


    embed4.set_author(name='Jagares Bot')


    for value in nameHistory[30:39]:
        embed4.add_field(name=f'\u200b', value=f"``{value}`` \u200b", inline=False)
    

    embed4.set_footer(text=f"© 2020 LazBoi All Rights Reserved | Page 4/{pages} ")





    embed5 = discord.Embed(
    title = f"{ign}'s Name History",
    colour = discord.Colour.orange()
    )


    embed5.set_author(name='Jagares Bot')


    for value in nameHistory[40:49]:
        embed5.add_field(name=f'\u200b', value=f"``{value}`` \u200b", inline=False)
    

    embed5.set_footer(text=f"© 2020 LazBoi All Rights Reserved | Page 5/{pages} ")




    embed6 = discord.Embed(
    title = f"{ign}'s Name History",
    colour = discord.Colour.orange()
    )


    embed6.set_author(name='Jagares Bot')


    for value in nameHistory[50:59]:
        embed6.add_field(name=f'\u200b', value=f"``{value}`` \u200b", inline=False)
    

    embed6.set_footer(text=f"© 2020 LazBoi All Rights Reserved | Page 6/{pages} ")


    embed7 = discord.Embed(
    title = f"{ign}'s Name History",
    colour = discord.Colour.orange()
    )


    embed6.set_author(name='Jagares Bot')


    for value in nameHistory[60:69]:
        embed7.add_field(name=f'\u200b', value=f"``{value}`` \u200b", inline=False)
    

    embed7.set_footer(text=f"© 2020 LazBoi All Rights Reserved | Page 7/{pages} ")



    if nameLength <= 10:
        embeds = [embed1]
    elif nameLength <= 20:
        embeds = [embed1, embed2]
    elif nameLength <= 30:
        embeds = [embed1, embed2, embed3]
    elif nameLength <= 40:
        embeds = [embed1, embed2, embed3, embed4]
    elif nameLength <= 50:
        embeds = [embed1, embed2, embed3, embed4, embed5]
    elif nameLength <= 60:
        embeds = [embed1, embed2, embed3, embed4, embed5, embed6]
    elif nameLength <= 70:
        embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7]




    message = await ctx.send(embed=embed1)
    page = pag(bot, message, footer=False, only=ctx.author, use_more=False, embeds = embeds, language='en',use_exit=False, exit_reaction=["⏹"])

    await page.start()






# BSG
# BSG
# BSG
# BSG
# BSG
# BSG











@bot.command(aliases=['blitz', 'sg', 'hg'])
async def bsg(ctx, name=None):
    if name is None:
        name = ctx.message.author.display_name
    data = hypixel.hypixel_api(name)
    try:
        ign = hypixel.get_displayname(name, data)
    except:
        await ctx.send(f"Player `{name}` is not found!")
    kills = hypixel.get_bsg_kills(name, data) 
    wins_solo = hypixel.get_bsg_wins_solo_normal(name, data)
    wins_teams = hypixel.get_bsg_wins_teams_normal(name, data)
   # wins = wins_solo + wins_teams
    deaths = hypixel.get_bsg_deaths(name, data)
   # losses = hypixel.get_bsg_losses_solo_normal(name, data) + hypixel.get_bsg_losses_teams_normal(name, data)
    coins = hypixel.get_bsg_coins(name, data)
    if deaths == 0:
        kd = kills
    else:
        kd = round(kills/deaths, 2)
   # wl = round(wins/losses, 2)
    

    rand = get_random_string(12)


    embed = discord.Embed(
    title = f"{ign}'s Blitz Stats ",
    colour = discord.Colour.orange()
    )



    embed.set_author(name='Jagares Bot', icon_url=f"https://minotar.net/helm/{ign}/400")
    embed.add_field(name='Kills', value=f"{'{:,}'.format(kills)}", inline=True)
 
    embed.add_field(name='Deaths', value=f"{'{:,}'.format(deaths)}", inline=True)
    embed.add_field(name='K/D Ratio', value=f'{kd}', inline=True)
    embed.add_field(name='Solo Wins', value=f"{'{:,}'.format(wins_solo)}", inline=True)
    embed.add_field(name='Teams Wins', value=f"{'{:,}'.format(wins_teams)}", inline=True)
  #  embed.add_field(name='Losses', value=f"{'{:,}'.format(losses)}", inline=True)
  #  embed.add_field(name='W/L Ratio', value=f"{'{:,}'.format(wl)}", inline=True)
    embed.add_field(name='Coins', value=f"{'{:,}'.format(coins)}", inline=True)



    embed.set_image(url=f"https://gen.plancke.io/blitz/{ign}/3.png?random={rand}")

    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")

    await ctx.send(embed=embed)

















###OTHER
###OTHER
###OTHER

def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    rand = ''.join(random.choice(letters) for i in range(length))
    return rand



bot.run(os.environ["token"])
