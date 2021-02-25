import requests
import math, re


API_KEY = "d52f4c03-9f60-4358-8a24-d5d97b46ceb1"
BASE = 10_000
GROWTH = 2_500
REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH
REVERSE_CONST = REVERSE_PQ_PREFIX
GROWTH_DIVIDES_2 = 2 / GROWTH



















def uuid_or_name(input):
    uuid_pattern = re.compile(r'^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-5][0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$', re.IGNORECASE)
    uuid_matches = uuid_pattern.finditer(input)

    mcname_pattern = re.compile(r'^\w{1,16}$', re.IGNORECASE)
    mcname_matches = mcname_pattern.finditer(input)
    result = None
    if list(uuid_matches) != []:
        # await ctx.send('uuid')
        result = "uuid"
    else:
        list(mcname_matches) != []
        # await ctx.send('name')
        result = "name"


    return result






# API
# API
# API






def hypixel_api(name):
    result = uuid_or_name(name)
    url = f"https://api.hypixel.net/player?key={API_KEY}&{result}={name}"
    res = requests.get(url)
    data = res.json()
    if data["player"] is None:
        return None
    return data




def hypixel_api2(name):
    url2 = f"https://api.slothpixel.me/api/players/{name}"
    res2 = requests.get(url2)
    data2 = res2.json()
    if data2["username"] is None:
        return None
    return data2





def hypixel_gapi(name):
    result = uuid_or_name(name)
    if result == "name":
        try:
            uuid = hypixel_api(name)["player"]["uuid"]
            name = uuid
        except:
            name = "none"
    gurl = f"https://api.hypixel.net/guild?key={API_KEY}&player={name}"
    gres = requests.get(gurl)
    gdata = gres.json()
    if gdata["success"] == False or gdata["guild"] == None:
        gdata = None
    return gdata





def hypixel_wdapi():
    wdurl = f"https://api.hypixel.net/watchdogstats?key={API_KEY}"
    wdres = requests.get(wdurl)
    wddata = wdres.json()
    if wddata["watchdog_total"] is None:
        return None
    return wddata


# def mojang_api(name):
#     url = f"https://api.mojang.com/users/profiles/minecraft/{name}"
#     res = requests.get(url)
#     mdata = res.json()
#     if mdata["id"] is None:
#         return None
#     return mdata["id"]










# NOT HYPIXEL
# NOT HYPIXEL
# NOT HYPIXEL


def chat_api(message):

    chat_res = requests.get(f"https://some-random-api.ml/chatbot?message={message}")
    chat_data = chat_res.json()
    if chat_data["response"] is None:
        return None
    return chat_data["response"]

def lyrics_api(title):

    res = requests.get(f"https://some-random-api.ml/lyrics?title={title}")
    data = res.json()

    return data











def bird_img_api():

    res = requests.get("https://some-random-api.ml/img/birb")
    data = res.json()
    if data["link"] is None:
        return None
    return data["link"]


def dog_img_api():

    res = requests.get("https://dog.ceo/api/breeds/image/random")
    data = res.json()
    if data["message"] is None:
        return None
    return data["message"]



def cat_img_api():

    res = requests.get("https://some-random-api.ml/img/cat")
    data = res.json()
    if data["link"] is None:
        return None
    return data["link"]




def panda_img_api():

    res = requests.get("https://some-random-api.ml/img/panda")
    data = res.json()
    if data["link"] is None:
        return None
    return data["link"]




























# INFO
# INFO
# INFO
# INFO
# INFO







def get_displayname(name, data):
    try:
        ign = str(data["player"]["displayname"])
    except:
        ign = "none"
    return ign

def get_uuid(name, data):
    try:
        uuid = str(data["player"]["uuid"])
    except:
        uuid = "none"
    return uuid


def get_level(name, data2):
    try:
        exp = int(data2["exp"])
    except:
        exp = 0
    return round(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * exp))


def get_karma(name, data2):
    try:
        karma = int(data2["karma"])
    except:
        karma = 0
    return karma


def get_achievementPoints(name, data2):
    try:
        achievementPoints = int(data2["achievement_points"])
    except:
        achievementPoints = 0
    return achievementPoints

def get_quests(name, data2):
    try:
        quests_completed = int(data2["quests_completed"])
    except:
        quests_completed = 0
    return quests_completed


def get_mcVersionRp(name, data):
    try:
        mcVersionRp = str(data["player"]["mcVersionRp"])
    except:
        mcVersionRp = "Unknown"

    return mcVersionRp


def get_firstLogin(name, data):
    _id = data["player"]["_id"]
    firstLogin = int(_id[0:8], base = 16) * 1000
    return firstLogin


def get_lastLogin(name, data):
    
    lastLogin = int(data["player"]["lastLogin"])
    return lastLogin

def get_playerDiscord(name, data):
    try:
        playerDiscord = str(data["player"]["socialMedia"]["links"]["DISCORD"])
    except:
        playerDiscord = None
    return playerDiscord



def get_newPackageRank(name, data):
    try:
        newPackageRank = str(data["player"]["newPackageRank"])
    except:
        newPackageRank = "Unknown"

    return newPackageRank


def get_monthlyPackageRank(name, data):
    try:
        monthlyPackageRank = str(data["player"]["monthlyPackageRank"])
    except:
        monthlyPackageRank = "Unknown"

    return monthlyPackageRank





def get_knownAliases(name, data):
    try:
        nameHistory = (data["player"]["knownAliases"])
    except:
        nameHistory = ['\u200b' '\u200b']
    return nameHistory

















# MEGA WALLS
# MEGA WALLS
# MEGA WALLS
# MEGA WALLS
# MEGA WALLS











def get_final_kills(name, data):
    try:
        final_kills = int(data["player"]["stats"]["Walls3"]["final_kills"])
    except:
        final_kills = 0
    return final_kills

# def get_finalKills(name, data):
#     try:
#         finalKills = int(data["player"]["stats"]["Walls3"]["finalKills"])
#     except:
#         finalKills = 0
#     return finalKills


def get_final_assists(name, data):
    try:
        final_assists = int(data["player"]["stats"]["Walls3"]["final_assists"])
    except:
        final_assists = 0
    return final_assists


def get_final_deaths_post(name, data):
    try:
        final_deaths = int(data["player"]["stats"]["Walls3"]["final_deaths"])
    except:
        final_deaths = 0
    return final_deaths


def get_final_deaths_pre(name, data):
    try:
        finalDeaths = int(data["player"]["stats"]["Walls3"]["finalDeaths"])
    except:
        finalDeaths = 0
    return finalDeaths


def get_wins(name, data):
    try:
        wins = int(data["player"]["stats"]["Walls3"]["wins"])
    except:
        wins = 0
    return wins


def get_losses(name, data):
    try:
        losses = int(data["player"]["stats"]["Walls3"]["losses"])
    except:
        losses = 0
    return losses


def get_coins(name, data):
    try:
        coins = int(data["player"]["stats"]["Walls3"]["coins"])
    except:
        coins = 0
    return coins


def get_mythic_favor(name, data):
    try:
        mythic_favor = int(data["player"]["stats"]["Walls3"]["mythic_favor"])
    except:
        mythic_favor = 0
    return mythic_favor


def get_wither_damage(name, data):
    try:
        wither_damage = int(data["player"]["stats"]["Walls3"]["wither_damage"])
    except:
        wither_damage = 0
    return wither_damage


def get_chosen_class(name, data):
    try:
        chosen_class = str(data["player"]["stats"]["Walls3"]["chosen_class"])
    except:
        chosen_class = "none"
    return chosen_class

def get_chosen_skin(name, chosen_class, data):
    try:
        chosen_skin = str(data["player"]["stats"]["Walls3"][f"chosen_skin_{chosen_class.capitalize()}"])
    except:
        chosen_skin = "none"
    return chosen_skin


def get_cakes_found(name, data):
    try:
        cakes_found = int(data["player"]["stats"]["Walls3"]["cakes_found"])
    except:
        cakes_found = 0
    return cakes_found

















def get_class_finals(name, Class, data):
    
    try:
        class_finals = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_final_kills_standard"])
    except:
        class_finals = 0
    return class_finals


def get_class_final_assists(name, Class, data):
    
    try:
        class_final_assists = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_final_assists_standard"])
    except:
        class_final_assists = 0
    return class_final_assists

def get_class_wins(name, Class, data):
    
    try:
        class_wins = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_wins_standard"])
    except:
        class_wins = 0
    return class_wins


# def get_class_final_deaths(name, Class, data):
    
#     try:
#         class_final_deaths = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_final_deaths_standard"])
#     except:
#         class_final_deaths = 0
#     return class_final_deaths


# def get_class_losses(name, Class, data):
    
#     try:
#         class_final_losses = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_losses_standard"])
#     except:
#         class_final_losses = 0
#     return class_final_losses








def get_class_finals_all(name, Class, data):
    
    try:
        class_finals_all = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_final_kills"])
    except:
        class_finals_all = 0
    return class_finals_all

def get_class_final_assists_all(name, Class, data):
    
    try:
        class_final_assists_all = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_final_assists"])
    except:
        class_final_assists_all = 0
    return class_final_assists_all


def get_class_final_deaths_all(name, Class, data):
    
    try:
        class_final_deaths_all = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_final_deaths"])
    except:
        class_final_deaths_all = 0
    return class_final_deaths_all

def get_class_wins_all(name, Class, data):
    
    try:
        class_wins_all = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_wins"])
    except:
        class_wins_all = 0
    return class_wins_all


def get_class_losses_all(name, Class, data):
    
    try:
        class_losses_all = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_losses"])
    except:
        class_losses_all = 0
    return class_losses_all



def get_class_prestige(name, Class, data):
    
    try:
        class_prestige = int(data["player"]["stats"]["Walls3"]["classes"][f"{Class.lower()}"]["prestige"])
    except:
        class_prestige = 0
    return class_prestige


def get_class_unlocked(name, Class, data):
    
    try:
        class_unlocked = data["player"]["stats"]["Walls3"]["classes"][f"{Class.lower()}"]["unlocked"]
    except:
        class_unlocked = False
    return class_unlocked



def get_class_kit(name, Class, data):
    
    try:
        class_kit = int(data["player"]["stats"]["Walls3"]["classes"][f"{Class.lower()}"]["skill_level_d"])
    except:
        class_kit = 1
    return class_kit

def get_class_skill(name, Class, data):
    
    try:
        class_skill = int(data["player"]["stats"]["Walls3"]["classes"][f"{Class.lower()}"]["skill_level_a"])
    except:
        class_skill = 1
    return class_skill

def get_class_passive1(name, Class, data):
    
    try:
        class_passive1 = int(data["player"]["stats"]["Walls3"]["classes"][f"{Class.lower()}"]["skill_level_b"])
    except:
        class_passive1 = 1
    return class_passive1

def get_class_passive2(name, Class, data):
    
    try:
        class_passive2 = int(data["player"]["stats"]["Walls3"]["classes"][f"{Class.lower()}"]["skill_level_c"])
    except:
        class_passive2 = 1
    return class_passive2

def get_class_passive3(name, Class, data):
    
    try:
        class_passive3 = int(data["player"]["stats"]["Walls3"]["classes"][f"{Class.lower()}"]["skill_level_g"])
    except:
        class_passive3 = 1
    return class_passive3















# BLITZ SURVIVAL GAMES
# BLITZ SURVIVAL GAMES
# BLITZ SURVIVAL GAMES
# BLITZ SURVIVAL GAMES
# BLITZ SURVIVAL GAMES



def get_bsg_kills(name, data):
    try:
        bsg_kills = int(data["player"]["stats"]["HungerGames"]["kills"])
    except:
        bsg_kills = 0
    return bsg_kills

def get_bsg_kills_solo_normal(name, data):
    try:
        bsg_kills_solo_normal = int(data["player"]["stats"]["HungerGames"]["kills_solo_normal"])
    except:
        bsg_kills_solo_normal = 0
    return bsg_kills_solo_normal

def get_bsg_kills_teams_normal(name, data):
    try:
        bsg_kills_teams_normal = int(data["player"]["stats"]["HungerGames"]["kills_teams_normal"])
    except:
        bsg_kills_teams_normal = 0
    return bsg_kills_teams_normal







def get_bsg_deaths(name, data):
    try:
        bsg_deaths = int(data["player"]["stats"]["HungerGames"]["deaths"])
    except:
        bsg_deaths = 0
    return bsg_deaths







def get_bsg_coins(name, data):
    try:
        bsg_coins = int(data["player"]["stats"]["HungerGames"]["coins"])
    except:
        bsg_coins = 0
    return bsg_coins





def get_bsg_wins(name, data):
    try:
        bsg_wins = int(data["player"]["stats"]["HungerGames"]["wins"])
    except:
        bsg_wins = 0
    return bsg_wins




def get_bsg_games_played(name, data):
    try:
        bsg_games_played = int(data["player"]["stats"]["HungerGames"]["games_played"])
    except:
        bsg_games_played = 0
    return bsg_games_played





def get_bsg_wins_rambo(name, data):
    try:
        bsg_wins_rambo = int(data["player"]["stats"]["HungerGames"]["wins_rambo"])
    except:
        bsg_wins_rambo = 0
    return bsg_wins_rambo



def get_bsg_kills_rambo(name, data):
    try:
        bsg_kills_rambo = int(data["player"]["stats"]["HungerGames"]["kills_rambo"])
    except:
        bsg_kills_rambo = 0
    return bsg_kills_rambo



def get_bsg_chosen_victorydance(name, data):
    try:
        bsg_chosen_victorydance = str(data["player"]["stats"]["HungerGames"]["chosen_victorydance"])
    except:
        bsg_chosen_victorydance = "N/A"
    return bsg_chosen_victorydance


def get_bsg_chosen_finisher(name, data):
    try:
        bsg_chosen_finisher = str(data["player"]["stats"]["HungerGames"]["chosen_finisher"])
    except:
        bsg_chosen_finisher = "N/A"
    return bsg_chosen_finisher

def get_bsg_chosen_taunt(name, data):
    try:
        bsg_chosen_taunt = str(data["player"]["stats"]["HungerGames"]["chosen_taunt"])
    except:
        bsg_chosen_taunt = "N/A"
    return bsg_chosen_taunt


def get_bsg_taunt_kills(name, data):
    try:
        bsg_taunt_kills = int(data["player"]["stats"]["HungerGames"]["taunt_kills"])
    except:
        bsg_taunt_kills = 0
    return bsg_taunt_kills

def get_bsg_time_played(name, data):
    try:
        bsg_time_played = int(data["player"]["stats"]["HungerGames"]["time_played"])
    except:
        bsg_time_played = 0
    return bsg_time_played






#GUILD
#GUILD
#GUILD
#GUILD
#GUILD





def get_guild_name(name, gdata):
    try:
        guild_name = str(gdata["guild"]["name"])
    except:
        guild_name = "none"
    return guild_name

def get_guild_members(name, gdata):
    try:
        guild_members = gdata["guild"]["members"]
    except:
        guild_members = []
    return guild_members



def get_guild_tag(name, gdata):
    try:
        guild_tag = "[" + str(gdata["guild"]["tag"]) + "]"
    except:
        guild_tag = ""
    return guild_tag

def get_guild_tag_color(name, gdata):
    try:
        get_guild_tag_color = str(gdata["guild"]["tagColor"])
    except:
        get_guild_tag_color = "grey"
    return get_guild_tag_color

# def get_guild_description(name, gdata):
#     try:
#         guild_description = str(gdata["description"])
#     except:
#         guild_description = "unknown guild description"
#     if guild_description == "":
#         guild_description = "No Guild Description"
        

#     return guild_description

def get_guild_exp(name, gdata):
    try:
        guild_exp = int(gdata["guild"]["exp"])
    except:
        guild_exp = 0
    return guild_exp


def get_guild_level(exp):
    EXP_NEEDED = [
    100000,
    150000,
    250000,
    500000,
    750000,
    1000000,
    1250000,
    1500000,
    2000000,
    2500000,
    2500000,
    2500000,
    2500000,
    2500000,
    3000000,]
    
    level = 0

    for i in range(0, 1000):
        need = 0
        if i >= len(EXP_NEEDED):
            need = EXP_NEEDED[len(EXP_NEEDED) - 1]
        else:
            need = EXP_NEEDED[i]
        i += 1

        if (exp - need) < 0:
            return round((level + (exp / need)) * 100) / 100
        level += 1
        exp -= need
    
    return 0




# WATCHDOG
# WATCHDOG
# WATCHDOG
# WATCHDOG
# WATCHDOG



def get_watchdog_last(wddata):
    try:
        watchdog_last = int(wddata["watchdog_lastMinute"])
    except:
        watchdog_last = 0
    return watchdog_last

def get_watchdog_total(wddata):
    try:
        watchdog_total = int(wddata["watchdog_total"])
    except:
        watchdog_total = 0
    return watchdog_total

def get_watchdog_daily(wddata):
    try:
        watchdog_daily = int(wddata["watchdog_rollingDaily"])
    except:
        watchdog_daily = 0
    return watchdog_daily


def get_staff_daily(wddata):
    try:
        staff_daily = int(wddata["staff_rollingDaily"])
    except:
        staff_daily = 0
    return staff_daily

def get_staff_total(wddata):
    try:
        staff_total = int(wddata["staff_total"])
    except:
        staff_total = 0
    return staff_total








