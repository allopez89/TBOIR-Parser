from mediawiki import MediaWiki
from bs4 import BeautifulSoup
import requests
import Titles

tboi = MediaWiki(url="https://bindingofisaacrebirth.fandom.com/api.php", user_agent="TBOIR-WikiParser/0.1.0 (axellpz89@hotmail.com) pymediawiki/0.7.0")

def GetSections(obj):
    unusedSec = ["Trivia", "Gallery", "Seeds", "In-game Footage",
     "Bugs", "References", "In-game footage", "Links", 
     "Unlockable Achievements", "Activated Collectible", "Passive Collectible", "",
     "No Effect", "In-game footage", "In Rebirth", "In Repentance",
     "Seed", "Reference", ""]
    Sections = tboi.page(obj).sections
    for x in range(0, len(unusedSec)):
        if unusedSec[x] in Sections: Sections.remove(unusedSec[x])  
    return Sections

def GetQuote(obj):
    obj.replace("?", "%3F")
    page = requests.get("https://bindingofisaacrebirth.fandom.com/wiki/{}".format(obj))
    soup = BeautifulSoup(page.content, "html.parser")
    side = soup.find("aside", role="region")
    quote = side.find("div", {"data-source":"quote"})
    return quote.text.replace("\n", "").replace("\"", "").replace("Pickup Quote", "")  


        
