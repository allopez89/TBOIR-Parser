from mediawiki import MediaWiki
from bs4 import BeautifulSoup
import requests

tboi = MediaWiki(url="https://bindingofisaacrebirth.fandom.com/api.php", user_agent="wikiparser/0.0 (axellpz89@hotmail.com) pymediawiki/0.7.0")

#region Scrape Pickups
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
    #tbody = results.find("tbody")
    trow = results.find_all("span", id=True)

    for i, tcell in enumerate(trow):
        trow[i] = tcell["id"]
    for i, s in enumerate(trow):
        trow[i] = s.replace("_", " ")
    discard = ["Lil.27 Battery", "Notes", "Unlockable Achievements", "Gallery", "Reward Chances", "Trivia", "Bugs", "Mom.27s Chest"]
    for i in range(0, len(discard)):
        if discard[i] in trow: trow.remove(discard[i])
    return trow
#endregion

Actives = tboi.categorymembers("Activated collectibles", None, False)
Passives = tboi.categorymembers("Passive collectibles", None, False)
Characters = tboi.categorymembers("Characters", None, False)
Achievements = tboi.categorymembers("Achievement images", None, False)
Bosses = tboi.categorymembers("Bosses", None, False)
Hearts = GetHearts_Bombs_Pills_Cards_Runes("https://bindingofisaacrebirth.fandom.com/wiki/Hearts")
Coins = GetCoins_Keys("https://bindingofisaacrebirth.fandom.com/wiki/Coins")
Bombs = GetHearts_Bombs_Pills_Cards_Runes("https://bindingofisaacrebirth.fandom.com/wiki/Bombs")
Keys = GetCoins_Keys("https://bindingofisaacrebirth.fandom.com/wiki/Keys")
Batteries = GetBatteries_Chests_Sacks("https://bindingofisaacrebirth.fandom.com/wiki/Batteries")
Pills = GetHearts_Bombs_Pills_Cards_Runes("https://bindingofisaacrebirth.fandom.com/wiki/Pills")
Cards_Runes = GetHearts_Bombs_Pills_Cards_Runes("https://bindingofisaacrebirth.fandom.com/wiki/Cards_and_Runes")
Chests = GetBatteries_Chests_Sacks("https://bindingofisaacrebirth.fandom.com/wiki/Chests")
Sacks = GetBatteries_Chests_Sacks("https://bindingofisaacrebirth.fandom.com/wiki/Sacks")

#region Parse Characters, Achievements, Bosses
# Delete not needed characters
not_needed = ["Co-op", "Isaac/es", "NPCs", "Tainted Characters"]
for i, s in enumerate(Characters):
    Characters[i] = s.replace(" (Character)", "")
for x in range(0, len(not_needed)):
    if not_needed[x] in Characters: Characters.remove(not_needed[x])

# Parse achievementes
for i, s in enumerate(Achievements):
    Achievements[i] = s.replace("File:", "").replace(".png", "").replace(" icon", "")

# Delete not needed and parse bosses
Bosses.append("Angel")
Bosses.sort()
Bosses[:] = [x for x in Bosses if not "Bosses" in x]
if "Seven Deadly Sins" in Bosses: Bosses.remove("Seven Deadly Sins")
for i, s in enumerate(Bosses):
    Bosses[i] = s.replace(" (Boss)", "")
#endregion

print(Sacks)