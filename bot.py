import discord
import hypixel
import random
from discord.ext import commands
import datetime
import os
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure, MissingPermissions


bot = commands.Bot(command_prefix = "/")
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('/help'))
    
    print(bot.user.name + " is ready.")

@bot.command()
async def info(ctx, name):
    data = hypixel.hypixel_api(name)
    try:
        ign = hypixel.get_displayname(name, data)
    except:
        await ctx.send("Player not found! (Make sure to use their Minecraft username)")
    level = hypixel.get_level(name, data)
    karma = hypixel.get_karma(name, data)
    achievementPoints = hypixel.get_achievementPoints(name, data)
    version = hypixel.get_mcVersionRp(name, data)
    firstLogin = hypixel.get_firstLogin(name, data)
   
    dt_firstLogin = datetime.datetime.utcfromtimestamp(round(firstLogin/1000))
    try:
        lastLogin = hypixel.get_lastLogin(name, data)
        dt_lastLogin = datetime.datetime.utcfromtimestamp(round(lastLogin/1000))
    except:
        lastLogin = "Unknown"
        dt_lastLogin = "Unknown"
    # quests = hypixel.get_quests(name, data)


    embed = discord.Embed(
    title = 'Jagares Bot',
    colour = discord.Colour.orange()
    )



    # embed.set_author(name='w')
    embed.add_field(name='Ign', value=f'{ign}', inline=False)
    embed.add_field(name='Level', value=f'{level}', inline=False)
    embed.add_field(name='Karma', value=f"{'{:,}'.format(karma)}", inline=False)
    embed.add_field(name='Achievement Points', value=f"{'{:,}'.format(achievementPoints)}", inline=False)
    # embed.add_field(name='Quests Completed', value=f"{'{:,}'.format(quests)}", inline=False)
    embed.add_field(name='Version', value=f'{version}', inline=False)
    embed.add_field(name='First Login', value=f'{dt_firstLogin} UTC', inline=False)
    embed.add_field(name='Last Login', value=f'{dt_lastLogin} UTC', inline=False)
    embed.set_image(url=f"https://minotar.net/armor/body/{ign}.png")
    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")



    if level == 0:
        await ctx.send("Player not found! (Make sure to use their Minecraft username)")
    else:
         await ctx.send(embed=embed)



@bot.command()
async def help(ctx):
    

    embed = discord.Embed(
    title = 'Jagares Bot',
    colour = discord.Colour.orange()
    )


    
    embed.set_author(name='Commands')
    embed.add_field(name='Info', value='/info <player>', inline=False)
    embed.add_field(name='Guild Info', value='/guild <guild name>', inline=False)
    embed.add_field(name='Watchdog/Staff Stats', value='/watchdog', inline=False)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Mega Walls Stats', value='/mw <player>', inline=False)
    embed.add_field(name='Mega Walls Class Points', value='/cp <player>', inline=False)
    embed.add_field(name='Mega Walls Class Stats', value='/mwclass <class> <player>', inline=False)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='Blitz Survival Games Stats', value='/bsg <player>', inline=False)
    embed.add_field(name='\u200b', value='\u200b', inline=False)
    embed.add_field(name='8ball', value='/8ball <question>', inline=False)
    embed.add_field(name='Good Night', value='/gn <person>', inline=False)
    embed.add_field(name='Duel', value='/duel <player1> <player2>', inline=False)
    embed.add_field(name='Pet Image', value='/dog/cat/bird/panda', inline=False)
    embed.add_field(name='Lyrics', value='/lyrics <song>', inline=False)
    embed.add_field(name='Bot Chat', value='/chat <message>', inline=False)
    embed.add_field(name='Shoutout', value='/shoutout', inline=False)
    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")

    await ctx.send(embed=embed)

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
    capes = ['https://www.needcoolshoes.com/banner?=aapfaiavpypEac', 
                 'https://www.needcoolshoes.com/banner?=paafpipvayaEpc', 
                 'https://www.needcoolshoes.com/banner?=pamfpipvmymEpc', 
                 'https://www.needcoolshoes.com/banner?=pajfpipvjyjEpc', 
                 'https://www.needcoolshoes.com/banner?=paffpipvfyfEpc', 
                 'https://www.needcoolshoes.com/banner?=paefpipveyeEpc', 
                 'https://www.needcoolshoes.com/banner?=pakfpipvkykEpc', 
                 'https://www.needcoolshoes.com/banner?=palfpipvlylEpc', 
                 'https://www.needcoolshoes.com/banner?=paofpipvoyoEpc', 
                 'https://www.needcoolshoes.com/banner?=pabfpipvbybEpc', 
                 'https://www.needcoolshoes.com/banner?=aalfaiavlylEac', 
                 'https://www.needcoolshoes.com/banner?=aaofaiavoyoEac', 
                 'https://www.needcoolshoes.com/banner?=aabfaiavbybEac', 
                 'https://www.needcoolshoes.com/banner?=aakfaiavkykEac', 
                 'https://www.needcoolshoes.com/banner?=aamfaiavmymEac', 
                 'https://www.needcoolshoes.com/banner?=aaefaiaveyeEac', 
                 'https://www.needcoolshoes.com/banner?=aaffaiavfyfEac', 
                 'https://www.needcoolshoes.com/banner?=japfjijvpypEjc', 
                 'https://www.needcoolshoes.com/banner?=fapffifvpypEfc', 
                 'https://www.needcoolshoes.com/banner?=eapfeievpypEec',
                 'https://www.needcoolshoes.com/banner?=mapfmimvpypEmc',
	         'https://www.needcoolshoes.com/banner?=kapfkikvpypEkc',
	         'https://www.needcoolshoes.com/banner?=lapflilvpypElc',
		 'https://www.needcoolshoes.com/banner?=oapfoiovpypEoc',
		 'https://www.needcoolshoes.com/banner?=bapfbibvpypEbc',
		 'https://www.needcoolshoes.com/banner?=dalfdidvlylEdc',
		 'https://www.needcoolshoes.com/banner?=fajffifvjyjEfc',
		 'https://www.needcoolshoes.com/banner?=fakffifvkykEfc',
		 'https://www.needcoolshoes.com/banner?=labflilvbybElc', 
		 'https://www.needcoolshoes.com/banner?=gapfgigvpypEgc', 
	         'https://www.needcoolshoes.com/banner?=jaffjijvfyfEjc']

    await ctx.send(f'Generated A Guild Cape {random.choice(capes)}')

@bot.command()
async def gn(ctx, *, Object="bird"):
    
    await ctx.send(f'gn {Object}')



@bot.command(pass_context=True, aliases=['discord'])

async def dc(ctx):
    username = ctx.message.author
    if get(username.roles, id=519612131738386441):
        await ctx.send(f'https://discord.gg/88qd5TX')
    else:
        await ctx.send(f'Only Guild Members Have Access To This Command!')
 
		    
		    
		    
@bot.command(pass_context=True, aliases=['clear'])
@has_permissions(administrator=True, manage_messages=True, manage_channels=True)
async def purge(ctx, ammount=3):
    await ctx.channel.purge(limit=ammount+1)

		    

@purge.error
async def purge_error(error, ctx):
    if isinstance(error, MissingPermissions):
        		    	    
        await ctx.send("Looks like you don't have the permission lol")
		    
		    
		    
		    



@bot.command()
async def chat(ctx, *, message):
    Message = hypixel.chat_api(message)
    
    await ctx.send(f'{Message}')


# @bot.command()
# async def non(ctx):
    
#     await ctx.send(f'L non u are bad.')



@bot.command()
async def lyrics(ctx, *, title):
    


    try:
        Title = hypixel.lyrics_api(title)['title']
        Author = hypixel.lyrics_api(title)['author']
        Lyrics = hypixel.lyrics_api(title)['lyrics']    
        await ctx.send(f'Title: {Title} - {Author}')
        await ctx.send('\u200b')
        await ctx.send('%.2000s' % Lyrics)
    
    except:
 

        await ctx.send(f'Song not found')



@bot.command(aliases=['SO'])
async def shoutout(ctx):
    shoutouts = ['Shoutout to 44HP', 
                 'Shoutout to Cijaye', 
                 'Shoutout to TheManOfCake', 
                 'Shoutout to Sethlol', 
                 'Shoutout to Shtruz', 
                 'Shoutout to UnityPusheen', 
                 'Shoutout to LessYou', 
                 'Shoutout to Rom', 
                 'Shoutout to Dagals', 
                 'Shoutout to OhWellDone', 
                 'Shoutout to LazBoi', 
                 'Shoutout to Non', 
                 'Shoutout to 7mu', 
                 'Shoutout to Souls', 
                 'Shoutout to Pijaye', 
                 'Shoutout to BAKERTHEBAGELMAN', 
                 'Shoutout to JediKnight625', 
                 'Shoutout to BlackKnight625', 
                 'Shoutout to Tqqn', 
                 'Shoutout to BurnBlade']

    await ctx.send(f'{random.choice(shoutouts)}')















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
















@bot.command()
async def duel(ctx, p1="player1", p2="player2"):

    players = [p1, p2]
    
    await ctx.send(f'{random.choice(players)} Wins The Duel!')



@bot.command()
async def mw(ctx, name):
    data = hypixel.hypixel_api(name)
    try:
        ign = hypixel.get_displayname(name, data)
    except:
        await ctx.send("Player not found! (Make sure to use their Minecraft username)")
    final_kills = hypixel.get_final_kills(name, data) 
    wins = hypixel.get_wins(name, data)
    fds1 = hypixel.get_final_deaths_post(name, data)
    fds2 = hypixel.get_final_deaths_pre(name, data)
    losses = hypixel.get_losses(name, data)
    coins = hypixel.get_coins(name, data)
    chosen_class = hypixel.get_chosen_class(name, data)
    wither_damage = hypixel.get_wither_damage(name, data)
    mythic_favor = hypixel.get_mythic_favor(name, data)
    cakes_found = hypixel.get_cakes_found(name, data)
    fas = hypixel.get_final_assists(name, data)
    fds = fds1 + fds2
    if fds == 0: fds = 1
    fkd = round(final_kills/fds, 2)
    wl = round(wins/losses,  2)
    
    embed = discord.Embed(
    title = f'{ign}',
    colour = discord.Colour.orange()
    )



    embed.set_author(name='Jagares Bot', icon_url=f"https://minotar.net/helm/{ign}/400")
    embed.add_field(name='Final Kills', value=f"{'{:,}'.format(final_kills)}", inline=True)
    embed.add_field(name='Final Assists', value=f"{'{:,}'.format(fas)}", inline=True)
    embed.add_field(name='Final Deaths', value=f"{'{:,}'.format(fds)}", inline=True)
    embed.add_field(name='FK/D Ratio', value=f'{fkd}', inline=True)
    embed.add_field(name='Wins', value=f"{'{:,}'.format(wins)}", inline=True)
    embed.add_field(name='Losses', value=f"{'{:,}'.format(losses)}", inline=True)
    embed.add_field(name='W/L Ratio', value=f"{'{:,}'.format(wl)}", inline=True)
    embed.add_field(name='Coins', value=f"{'{:,}'.format(coins)}", inline=True)
    embed.add_field(name='Mythic Favor', value=f"{'{:,}'.format(mythic_favor)}", inline=True)
    embed.add_field(name='Wither Damage', value=f"{'{:,}'.format(wither_damage)}", inline=True)
    embed.add_field(name='Chosen Class', value=f"{chosen_class}", inline=True)
    embed.add_field(name='Cakes Found', value=f"{'{:,}'.format(cakes_found)}", inline=True)
    embed.set_image(url=f"https://gen.plancke.io/mw/{ign}/2.png")

    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")

    await ctx.send(embed=embed)

@bot.command()
async def cp(ctx, name):
    data = hypixel.hypixel_api(name)
    try:
        ign = hypixel.get_displayname(name, data)
    except:
        await ctx.send("Player not found! (Make sure to use their Minecraft username)")

    hunter_class_points = hypixel.get_hunter_class_points(name, data)
    zombie_class_points = hypixel.get_zombie_class_points(name, data)
    creeper_class_points = hypixel.get_creeper_class_points(name, data)
    arcanist_class_points = hypixel.get_arcanist_class_points(name, data)
    shaman_class_points = hypixel.get_shaman_class_points(name, data)
    dreadlord_class_points = hypixel.get_dreadlord_class_points(name, data)
    golem_class_points = hypixel.get_golem_class_points(name, data)
    squid_class_points = hypixel.get_squid_class_points(name, data)
    moleman_class_points = hypixel.get_moleman_class_points(name, data)
    enderman_class_points = hypixel.get_enderman_class_points(name, data)
    herobrine_class_points = hypixel.get_herobrine_class_points(name, data)
    blaze_class_points = hypixel.get_blaze_class_points(name, data)
    pigman_class_points = hypixel.get_pigman_class_points(name, data)
    spider_class_points = hypixel.get_spider_class_points(name, data)
    werewolf_class_points = hypixel.get_werewolf_class_points(name, data)
    pirate_class_points = hypixel.get_pirate_class_points(name, data)
    phoenix_class_points = hypixel.get_phoenix_class_points(name, data)
    skeleton_class_points = hypixel.get_skeleton_class_points(name, data)
    assassin_class_points = hypixel.get_assassin_class_points(name, data)
    renegade_class_points = hypixel.get_renegade_class_points(name, data)
    snowman_class_points = hypixel.get_snowman_class_points(name, data)
    automaton_class_points = hypixel.get_automaton_class_points(name, data)
    cow_class_points = hypixel.get_cow_class_points(name, data)
    shark_class_points = hypixel.get_shark_class_points(name, data)

       

    
    embed = discord.Embed(
    title = f"{ign}'s class points",
    colour = discord.Colour.orange()
    )



    embed.set_author(name='Jagares Bot', icon_url=f"https://minotar.net/helm/{ign}/400")

    embed.add_field(name='Hunter', value=f"{'{:,}'.format(hunter_class_points)}", inline=True)
    embed.add_field(name='Zombie', value=f"{'{:,}'.format(zombie_class_points)}", inline=True)
    embed.add_field(name='Creeper', value=f"{'{:,}'.format(creeper_class_points)}", inline=True)
    embed.add_field(name='Arcanist', value=f"{'{:,}'.format(arcanist_class_points)}", inline=True)
    embed.add_field(name='Shaman', value=f"{'{:,}'.format(shaman_class_points)}", inline=True)
    embed.add_field(name='Dreadlord', value=f"{'{:,}'.format(dreadlord_class_points)}", inline=True)
    embed.add_field(name='Golem', value=f"{'{:,}'.format(golem_class_points)}", inline=True)
    embed.add_field(name='Squid', value=f"{'{:,}'.format(squid_class_points)}", inline=True)
    embed.add_field(name='Moleman', value=f"{'{:,}'.format(moleman_class_points)}", inline=True)
    embed.add_field(name='Enderman', value=f"{'{:,}'.format(enderman_class_points)}", inline=True)
    embed.add_field(name='Herobrine', value=f"{'{:,}'.format(herobrine_class_points)}", inline=True)
    embed.add_field(name='Blaze', value=f"{'{:,}'.format(blaze_class_points)}", inline=True)
    embed.add_field(name='Pigman', value=f"{'{:,}'.format(pigman_class_points)}", inline=True)
    embed.add_field(name='Spider', value=f"{'{:,}'.format(spider_class_points)}", inline=True)
    embed.add_field(name='Werewolf', value=f"{'{:,}'.format(werewolf_class_points)}", inline=True)
    embed.add_field(name='Pirate', value=f"{'{:,}'.format(pirate_class_points)}", inline=True)
    embed.add_field(name='Phoenix', value=f"{'{:,}'.format(phoenix_class_points)}", inline=True)
    embed.add_field(name='Skeleton', value=f"{'{:,}'.format(skeleton_class_points)}", inline=True)
    embed.add_field(name='Assassin', value=f"{'{:,}'.format(assassin_class_points)}", inline=True)
    embed.add_field(name='Renegade', value=f"{'{:,}'.format(renegade_class_points)}", inline=True)
    embed.add_field(name='Snowman', value=f"{'{:,}'.format(snowman_class_points)}", inline=True)
    embed.add_field(name='Automaton', value=f"{'{:,}'.format(automaton_class_points)}", inline=True)
    embed.add_field(name='Cow', value=f"{'{:,}'.format(cow_class_points)}", inline=True)
    embed.add_field(name='Shark', value=f"{'{:,}'.format(shark_class_points)}", inline=True)


    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")

    await ctx.send(embed=embed)








@bot.command()
async def mwclass(ctx, Class, name):
    data = hypixel.hypixel_api(name)
    try:
        ign = hypixel.get_displayname(name, data)
    except:
        await ctx.send("Player not found! (Make sure to use the Minecraft username)")
    class_final_kills = hypixel.get_class_finals(name, Class, data)
    class_final_assists = hypixel.get_class_final_assists(name, Class, data)
    class_wins = hypixel.get_class_wins(name, Class, data)
    class_final_deaths = hypixel.get_class_final_deaths(name, Class, data)
    class_fkd = round(class_final_kills/class_final_deaths, 2)
    class_cp = class_wins * 10 + class_final_kills + class_final_assists
    class_losses = hypixel.get_class_losses(name, Class, data)
    class_wlr = round(class_wins/class_losses, 2)



    embed = discord.Embed(
    title = f"{ign}'s {Class.capitalize()} Stats",
    colour = discord.Colour.orange()
    )


    embed.set_author(name='Jagares Bot', icon_url=f"https://minotar.net/helm/{ign}/400")

    embed.add_field(name=f'{Class.capitalize()} Final Kills', value=f"{'{:,}'.format(class_final_kills)}", inline=True)
    embed.add_field(name=f'{Class.capitalize()} Final Assists', value=f"{'{:,}'.format(class_final_assists)}", inline=True)
    embed.add_field(name=f'{Class.capitalize()} FK/D Ratio', value=f"{'{:,}'.format(class_fkd)}", inline=True)
    embed.add_field(name=f'{Class.capitalize()} Wins', value=f"{'{:,}'.format(class_wins)}", inline=True)
    embed.add_field(name=f'{Class.capitalize()} Losses', value=f"{'{:,}'.format(class_losses)}", inline=True)
    embed.add_field(name=f'{Class.capitalize()} W/L Ratio', value=f"{'{:,}'.format(class_wlr)}", inline=True)   
    embed.add_field(name=f'{Class.capitalize()} Class Points', value=f"{'{:,}'.format(class_cp)}", inline=True)


    embed.set_image(url=f"https://gen.plancke.io/mwclass/{ign}/{Class.capitalize()}.png")
    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")




    await ctx.send(embed=embed)












#GUILD COMMANDS
#GUILD COMMANDS
#GUILD COMMANDS







@bot.command()
async def guild(ctx, *, gname):
    gdata = hypixel.hypixel_gapi(gname)
    try:
        guild_name = hypixel.get_guild_name(gname, gdata)
    except:
        await ctx.send("Guild not found! (Make sure to use the guild name)")
    guild_tag = hypixel.get_guild_tag(gname, gdata)
    guild_description = hypixel.get_guild_description(gname, gdata)
    guild_exp = hypixel.get_guild_exp(gname, gdata)
    guild_date = datetime.datetime.utcfromtimestamp(round(hypixel.get_guild_date(gname, gdata)/1000))


    embed = discord.Embed(
    title = 'Jagares Bot',
    colour = discord.Colour.orange()
    )



    # embed.set_author(name='w')
    embed.add_field(name='Guild Name', value=f'{guild_name} \u200b', inline=False)
    embed.add_field(name='Guild Tag', value=f'{guild_tag} \u200b', inline=False)
    embed.add_field(name='Guild description', value=f'{guild_description} \u200b', inline=False)
    embed.add_field(name='Guild Experience', value=f"{'{:,}'.format(guild_exp)} \u200b", inline=False)
    embed.add_field(name='Creation Date', value=f'{guild_date} UTC', inline=False)    

    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")



    if guild_name == 0:
        await ctx.send("Guild not found!")
    else:
         await ctx.send(embed=embed)







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










# BSG
# BSG
# BSG
# BSG
# BSG
# BSG











@bot.command(aliases=['blitz', 'sg', 'hg'])
async def bsg(ctx, name):
    data = hypixel.hypixel_api(name)
    try:
        ign = hypixel.get_displayname(name, data)
    except:
        await ctx.send("Player not found! (Make sure to use their Minecraft username)")
    kills = hypixel.get_bsg_kills(name, data) 
    wins_solo = hypixel.get_bsg_wins_solo_normal(name, data)
    wins_teams = hypixel.get_bsg_wins_teams_normal(name, data)
   # wins = wins_solo + wins_teams
    deaths = hypixel.get_bsg_deaths(name, data)
   # losses = hypixel.get_bsg_losses_solo_normal(name, data) + hypixel.get_bsg_losses_teams_normal(name, data)
    coins = hypixel.get_bsg_coins(name, data)
    kd = round(kills/deaths, 2)
   # wl = round(wins/losses, 2)
    
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



    embed.set_image(url=f"https://gen.plancke.io/blitz/{ign}/3.png")

    embed.set_footer(text="© 2020 LazBoi All Rights Reserved ")

    await ctx.send(embed=embed)

























bot.run(os.environ["token"])
