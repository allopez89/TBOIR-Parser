from mediawiki import MediaWiki
from bs4 import BeautifulSoup
import requests
from src import Titles

tboi = MediaWiki(url="https://bindingofisaacrebirth.fandom.com/api.php", user_agent="TBOIR-WikiParser/0.1.0 (axellpz89@hotmail.com) pymediawiki/0.7.0")
images = tboi.page("A Pony").images

def Get_Active_Images(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("aside", class_="portable-infobox pi-background pi-theme-wikia pi-layout-stacked")
    trow = results.find_all("img", title = True)
    return trow

def Get_Active_Images2(active):
    name = [active, "Item_altar", "Recharge_4"]
    images = tboi.page("A Pony").images
    images[:] = [x for x in images if ("A_Pony" in x) or ("Item_altar" in x) or ("Recharge_4" in x)]
    return images

for x in Titles.GetActives():
    x.replace(" ", "_")
    print(Get_Active_Images2(x))
