from re import S, findall
from mediawiki import MediaWiki
from bs4 import BeautifulSoup
import requests
import Titles

tboi = MediaWiki(url="https://bindingofisaacrebirth.fandom.com/api.php", user_agent="TBOIR-WikiParser/0.1.0 (axellpz89@hotmail.com) pymediawiki/0.7.0")

def GetActiveImages(active):
    images = tboi.page(active).images
    if "Broken_Shovel" in active: active2 = "Broken_Shovel_1"
    active2 = active.replace("!", "%21").replace("?", "").replace("'", "%27")
    images[:] = [x for x in images if 
    ("Collectible_{}_icon".format(active2) in x) or 
    ("Item_altar" in x) or 
    ("Collectible_{}_appearance".format(active2) in x) or
    ("Collectible_{}_tears".format(active2) in x) or 
    ("Recharge_" in x)]
    img = [x for x in images if "Recharge_" in x]
    if len(img) == 2:
        images.remove(img[0])
    return images      

def GetActiveImages2(active):
    page = requests.get("https://bindingofisaacrebirth.fandom.com/wiki/{}".format(active))
    soup = BeautifulSoup(page.content, "html.parser")
    aside = soup.find("aside", role="region")
    imgs = aside.find_all("img", class_="lazyload")
    for i, img in enumerate(imgs):
        imgs[i] = img["data-src"]
    active2 = active.replace("!", "%21").replace("?", "").replace("'", "%27")
    if "Broken_Shovel" in active: active2 = "Broken_Shovel_1"
    imgs[:] = [x for x in imgs if 
    ("Collectible_{}_icon".format(active2) in x) or 
    ("Item_altar" in x) or 
    ("Collectible_{}_appearance".format(active2) in x) or
    ("Collectible_{}_tears".format(active2) in x) or 
    ("Recharge_" in x)]
    img = [x for x in imgs if "Recharge_" in x]
    if len(img) == 2:
        imgs.remove(img[0])
    return imgs 

def GetPassiveImages(passive):
    images = tboi.page(passive).images
    if "Broken_Shovel" in passive: passive2 = "Broken_Shovel_2"
    passive2 = passive.replace("!", "%21").replace("?", "").replace("'", "%27").replace("/", "%2F")
    images[:] = [x for x in images if 
    ("Collectible_{}_icon".format(passive2) in x) or 
    ("Item_altar" in x) or 
    ("Collectible_{}_appearance".format(passive2) in x) or
    ("Collectible_{}_tears".format(passive2) in x)]
    return images  

def GetPassiveImages2(passive):
    page = requests.get("https://bindingofisaacrebirth.fandom.com/wiki/{}".format(passive))
    soup = BeautifulSoup(page.content, "html.parser")
    aside = soup.find("aside", role="region")
    imgs = aside.find_all("img", class_="lazyload")
    for i, img in enumerate(imgs):
        imgs[i] = img["data-src"]
    passive2 = passive.replace("!", "%21").replace("?", "").replace("'", "%27").replace("/", "%2F")
    if "Broken_Shovel" in passive: passive2 = "Broken_Shovel_2"
    if "???'s_Only_Friend" in passive: 
        passive2 = "Blue_Baby%27s_Only_Friend"
        imgs.append("")
    imgs[:] = [x for x in imgs if 
    ("Collectible_{}_icon".format(passive2) in x) or 
    ("Item_altar" in x) or 
    ("Collectible_{}_appearance".format(passive2) in x) or
    ("Collectible_{}_tears".format(passive2) in x)]
    return imgs  

#GetActiveImages("Best_Friend")
images = tboi.page("Best_Friend").images
print(images)
#print(GetPassiveImages("???'s_Only_Friend"))