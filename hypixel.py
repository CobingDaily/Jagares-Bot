import requests
import math


API_KEY = "d52f4c03-9f60-4358-8a24-d5d97b46ceb1"
BASE = 10_000
GROWTH = 2_500
REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH
REVERSE_CONST = REVERSE_PQ_PREFIX
GROWTH_DIVIDES_2 = 2 / GROWTH




# API
# API
# API



def hypixel_api(name):
    url = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
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
    gurl = f"https://api.slothpixel.me/api/guilds/{name}"
    gres = requests.get(gurl)
    gdata = gres.json()
    if gdata["name"] is None:
        return None
    return gdata


def hypixel_wdapi():
    wdurl = f"https://api.hypixel.net/watchdogstats?key={API_KEY}"
    wdres = requests.get(wdurl)
    wddata = wdres.json()
    if wddata["watchdog_total"] is None:
        return None
    return wddata












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
    ign = str(data["player"]["displayName"])
    return ign


def get_level(name, data2):
    try:
        exp = int(data2["exp"])
    except:
        exp = 0
    return math.floor(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * exp))


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
    mcVersionRp = str(data["player"]["mcVersionRp"])
    return mcVersionRp


def get_firstLogin(name, data):
    firstLogin = int(data["player"]["firstLogin"])
    return firstLogin


def get_lastLogin(name, data):
    
    lastLogin = int(data["player"]["lastLogin"])
    return lastLogin









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
        losses = 1
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


def get_cakes_found(name, data):
    try:
        cakes_found = int(data["player"]["stats"]["Walls3"]["cakes_found"])
    except:
        cakes_found = 0
    return cakes_found




def get_hunter_class_points(name, data):
    try:
        hunter_class_points = (int(data["player"]["stats"]["Walls3"]["hunter_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["hunter_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["hunter_final_assists_standard"])
    except:
        hunter_class_points = 0
    return hunter_class_points


def get_zombie_class_points(name, data):
    try:
        zombie_class_points = (int(data["player"]["stats"]["Walls3"]["zombie_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["zombie_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["zombie_final_assists_standard"])
    except:
        zombie_class_points = 0
    return zombie_class_points


def get_creeper_class_points(name, data):
    try:
        creeper_class_points = (int(data["player"]["stats"]["Walls3"]["creeper_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["creeper_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["creeper_final_assists_standard"])
    except:
        creeper_class_points = 0
    return creeper_class_points


def get_arcanist_class_points(name, data):
    try:
        arcanist_class_points = (int(data["player"]["stats"]["Walls3"]["arcanist_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["arcanist_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["arcanist_final_assists_standard"])
    except:
        arcanist_class_points = 0
    return arcanist_class_points


def get_shaman_class_points(name, data):
    try:
        shaman_class_points = (int(data["player"]["stats"]["Walls3"]["shaman_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["shaman_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["shaman_final_assists_standard"])
    except:
        shaman_class_points = 0
    return shaman_class_points


def get_dreadlord_class_points(name, data):
    try:
        dreadlord_class_points = (int(data["player"]["stats"]["Walls3"]["dreadlord_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["dreadlord_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["dreadlord_final_assists_standard"])
    except:
        dreadlord_class_points = 0
    return dreadlord_class_points


def get_golem_class_points(name, data):
    try:
        golem_class_points = (int(data["player"]["stats"]["Walls3"]["golem_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["golem_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["golem_final_assists_standard"])
    except:
        golem_class_points = 0
    return golem_class_points


def get_squid_class_points(name, data):
    try:
        squid_class_points = (int(data["player"]["stats"]["Walls3"]["squid_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["squid_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["squid_final_assists_standard"])
    except:
        squid_class_points = 0
    return squid_class_points

def get_moleman_class_points(name, data):
    try:
        moleman_class_points = (int(data["player"]["stats"]["Walls3"]["moleman_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["moleman_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["moleman_final_assists_standard"])
    except:
        moleman_class_points = 0
    return moleman_class_points


def get_enderman_class_points(name, data):
    try:
        enderman_class_points = (int(data["player"]["stats"]["Walls3"]["enderman_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["enderman_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["enderman_final_assists_standard"])
    except:
        enderman_class_points = 0
    return enderman_class_points

def get_herobrine_class_points(name, data):
    try:
        herobrine_class_points = (int(data["player"]["stats"]["Walls3"]["herobrine_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["herobrine_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["herobrine_final_assists_standard"])
    except:
        herobrine_class_points = 0
    return herobrine_class_points


def get_blaze_class_points(name, data):
    try:
        blaze_class_points = (int(data["player"]["stats"]["Walls3"]["blaze_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["blaze_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["blaze_final_assists_standard"])
    except:
        blaze_class_points = 0
    return blaze_class_points


def get_pigman_class_points(name, data):
    try:
        pigman_class_points = (int(data["player"]["stats"]["Walls3"]["pigman_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["pigman_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["pigman_final_assists_standard"])
    except:
        pigman_class_points = 0
    return pigman_class_points


def get_spider_class_points(name, data):
    try:
        spider_class_points = (int(data["player"]["stats"]["Walls3"]["spider_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["spider_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["spider_final_assists_standard"])
    except:
        spider_class_points = 0
    return spider_class_points


def get_werewolf_class_points(name, data):
    try:
        werewolf_class_points = (int(data["player"]["stats"]["Walls3"]["werewolf_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["werewolf_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["werewolf_final_assists_standard"])
    except:
        werewolf_class_points = 0
    return werewolf_class_points


def get_pirate_class_points(name, data):
    try:
        pirate_class_points = (int(data["player"]["stats"]["Walls3"]["pirate_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["pirate_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["pirate_final_assists_standard"])
    except:
        pirate_class_points = 0
    return pirate_class_points


def get_phoenix_class_points(name, data):
    try:
        phoenix_class_points = (int(data["player"]["stats"]["Walls3"]["phoenix_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["phoenix_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["phoenix_final_assists_standard"])
    except:
        phoenix_class_points = 0
    return phoenix_class_points


def get_skeleton_class_points(name, data):
    try:
        skeleton_class_points = (int(data["player"]["stats"]["Walls3"]["skeleton_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["skeleton_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["skeleton_final_assists_standard"])
    except:
        skeleton_class_points = 0
    return skeleton_class_points


def get_assassin_class_points(name, data):
    try:
        assassin_class_points = (int(data["player"]["stats"]["Walls3"]["assassin_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["assassin_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["assassin_final_assists_standard"])
    except:
        assassin_class_points = 0
    return assassin_class_points


def get_renegade_class_points(name, data):
    try:
        renegade_class_points = (int(data["player"]["stats"]["Walls3"]["renegade_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["renegade_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["renegade_final_assists_standard"])
    except:
        renegade_class_points = 0
    return renegade_class_points


def get_snowman_class_points(name, data):
    try:
        snowman_class_points = (int(data["player"]["stats"]["Walls3"]["snowman_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["snowman_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["snowman_final_assists_standard"])
    except:
        snowman_class_points = 0
    return snowman_class_points


def get_automaton_class_points(name, data):
    try:
        automaton_class_points = (int(data["player"]["stats"]["Walls3"]["automaton_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["automaton_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["automaton_final_assists_standard"])
    except:
        automaton_class_points = 0
    return automaton_class_points


def get_cow_class_points(name, data):
    try:
        cow_class_points = (int(data["player"]["stats"]["Walls3"]["cow_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["cow_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["cow_final_assists_standard"])
    except:
        cow_class_points = 0
    return cow_class_points


def get_shark_class_points(name, data):
    try:
        shark_class_points = (int(data["player"]["stats"]["Walls3"]["shark_wins_standard"]) * 10) + int(data["player"]["stats"]["Walls3"]["shark_final_kills_standard"]) + int(data["player"]["stats"]["Walls3"]["shark_final_assists_standard"])
    except:
        shark_class_points = 0
    return shark_class_points














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
        get_class_wins = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_wins_standard"])
    except:
        get_class_wins = 0
    return get_class_wins


def get_class_final_deaths(name, Class, data):
    
    try:
        class_final_deaths = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_final_deaths_standard"])
    except:
        class_final_deaths = 0
    return class_final_deaths


def get_class_losses(name, Class, data):
    
    try:
        class_final_losses = int(data["player"]["stats"]["Walls3"][f"{Class.lower()}_losses_standard"])
    except:
        class_final_losses = 0
    return class_final_losses









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


def get_bsg_wins_teams_normal(name, data):
    try:
        bsg_wins_teams_normal = int(data["player"]["stats"]["HungerGames"]["wins_teams_normal"])
    except:
        bsg_wins_teams_normal = 0
    return bsg_wins_teams_normal


def get_bsg_wins_solo_normal(name, data):
    try:
        bsg_wins_solo_normal = int(data["player"]["stats"]["HungerGames"]["wins_solo_normal"])
    except:
        bsg_wins_solo_normal = 0
    return bsg_wins_solo_normal



def get_bsg_losses_teams_normal(name, data):
    try:
        bsg_losses_teams_normal = int(data["player"]["stats"]["HungerGames"]["losses_teams_normal"])
    except:
        bsg_losses_teams_normal = 0
    return bsg_losses_teams_normal


def get_bsg_losses_solo_normal(name, data):
    try:
        bsg_losses_solo_normal = int(data["player"]["stats"]["HungerGames"]["losses_solo_normal"])
    except:
        bsg_losses_solo_normal = 0
    return bsg_losses_solo_normal








#GUILD
#GUILD
#GUILD
#GUILD
#GUILD





def get_guild_name(name, gdata):
    guild_name = str(gdata["name"])
    return guild_name

def get_guild_tag(name, gdata):
    try:
        guild_tag = str(gdata["tag"])
    except:
        guild_tag = "unknown guild tag"
    return guild_tag

def get_guild_description(name, gdata):
    try:
        guild_description = str(gdata["description"])
    except:
        guild_description = "unknown guild description"
    if guild_description == "":
        guild_description = "No Guild Description"
        

    return guild_description

def get_guild_exp(name, gdata):
    try:
        guild_exp = int(gdata["exp"])
    except:
        guild_exp = 0
    return guild_exp


def get_guild_date(name, gdata):
    try:
        guild_date = int(gdata["created"])
    except:
        guild_date = 0
    return guild_date

def get_guild_exp_history(name, gdata):
    guild_exp_history = dict(gdata["exp_history"])

    return guild_exp_history




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








