from mediawiki import MediaWiki
from bs4 import BeautifulSoup
import requests

tboi = MediaWiki(url="https://bindingofisaacrebirth.fandom.com/api.php", user_agent="TBOIR-WikiParser/0.1.0 (axellpz89@hotmail.com) pymediawiki/0.7.0")

def GetActiveItems():
   ActiveItems =  tboi.categorymembers("Activated collectibles", None, False)
   for i, s in enumerate(ActiveItems):
        ActiveItems[i] = s.replace("/es", "").replace("/ja", "").replace("/zh", "")
   return ActiveItems

def GetPassiveItems():
    PassiveItems = tboi.categorymembers("Passive collectibles", None, False)
    return PassiveItems

def GetCharacters():
    Characters = tboi.categorymembers("Characters", None, False)
    not_needed = ["Co-op", "Isaac/es", "NPCs", "Tainted Characters"]
    for i, s in enumerate(Characters):
        Characters[i] = s.replace(" (Character)", "")
    for x in range(0, len(not_needed)):
        if not_needed[x] in Characters: Characters.remove(not_needed[x])
    return Characters

def GetAchievements():
    Achievements = tboi.categorymembers("Achievement images", None, False)
    for i, s in enumerate(Achievements):
        Achievements[i] = s.replace("File:", "").replace(".png", "").replace(" icon", "")
    return Achievements

def GetBosses():
    Bosses = tboi.categorymembers("Bosses", None, False)
    Bosses[:] = [x for x in Bosses if not "Bosses" in x]
    if "Seven Deadly Sins" in Bosses: Bosses.remove("Seven Deadly Sins")
    for i, s in enumerate(Bosses):
        Bosses[i] = s.replace(" (Boss)", "")
    return Bosses

def GetHearts_Bombs_Pills_Cards_Runes(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="mw-parser-output")
    trow = results.find_all("tr", id=True)

    for i, tcell in enumerate(trow):
        trow[i] = tcell["id"]
    for i, s in enumerate(trow):
        trow[i] = s.replace("_", " ").replace(".21", "!").replace(".3F", "?").replace(".27", "'")
    return trow

def GetCoins_Keys(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("table", class_="wikitable")
    tbody = results.find("tbody")
    tcell = tbody.find_all("span", id=True)

    for i, cell in enumerate(tcell):
        tcell[i] = cell["id"]
    for i, s in enumerate(tcell):
        tcell[i] = s.replace("_", " ")
    return tcell

def GetBatteries_Chests_Sacks(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="mw-parser-output")
    trow = results.find_all("span", id=True)

    for i, tcell in enumerate(trow):
        trow[i] = tcell["id"]
    for i, s in enumerate(trow):
        trow[i] = s.replace("_", " ")
    discard = ["Lil.27 Battery", "Notes", "Unlockable Achievements", "Gallery", "Reward Chances", "Trivia", "Bugs", "Mom.27s Chest"]
    for i in range(0, len(discard)):
        if discard[i] in trow: trow.remove(discard[i])
    return trow

def GetPools():
    page = requests.get("https://bindingofisaacrebirth.fandom.com/wiki/Item_Pool")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("table", class_="nav-header")
    tbody = results.find("tbody")
    Pools = tbody.find_all("a")
    for i, cell in enumerate(Pools):
        Pools[i] = cell["title"]
    Pools[:] = [x for x in Pools if ("Item Pool" in x) and not ("Greed Mode Item Pool" in x)]
    for i, s in enumerate(Pools):
        Pools[i] = s.replace(" (Item Pool)", "")
    return Pools

def GetChallenges():
    Challenges = tboi.categorymembers("Challenges", None, False)
    for i, s in enumerate(Challenges):
        Challenges[i] = s.replace(" (Challenge)", "")
    return Challenges

def GetChapters():
    Chapters = tboi.categorymembers("Chapters", None, False)
    discardCategory = ["Greed Mode", "The Void/Locating Delirium"]
    for i, s in enumerate(Chapters):
        Chapters[i] = s.replace(" (Floor)", "")
    for x in range(0, len(discardCategory)):
        if discardCategory[x] in Chapters: Chapters.remove(discardCategory[x])
    return Chapters

def GetMiniBosses():
    Mini_Bosses = tboi.categorymembers("Mini-bosses", None, False)
    discardMiniBoss = ["All Mini-Bosses (Bosses)", "Tainted Jacob"]
    Mini_Bosses.append("Dark Esau")
    Mini_Bosses.sort()
    for x in range(0, len(discardMiniBoss)):
        if discardMiniBoss[x] in Mini_Bosses: Mini_Bosses.remove(discardMiniBoss[x])
    return Mini_Bosses

def GetMonsters():
    Monsters = tboi.categorymembers("Monsters", None, False)
    if "Monsters" in Monsters: Monsters.remove("Monsters")
    for i, s in enumerate(Monsters):
        Monsters[i] = s.replace(" (Enemy)", "")
    return Monsters

def GetRooms():
    Rooms = tboi.categorymembers("Rooms", None, False)
    return Rooms
    
def GetTransformations():
    Transformations = tboi.categorymembers("Transformations", None, False)
    if "Transformations" in Transformations: Transformations.remove("Transformations")
    for i, s in enumerate(Transformations):
        Transformations[i] = s.replace(" (Transformation)", "")
    return Transformations

def GetTrinkets():
    Trinkets = tboi.categorymembers("Trinkets", None, False)
    return Trinkets