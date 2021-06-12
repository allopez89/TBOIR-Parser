from mediawiki import MediaWiki
from bs4 import BeautifulSoup
import requests
import Titles

tboi = MediaWiki(url="https://bindingofisaacrebirth.fandom.com/api.php", user_agent="TBOIR-WikiParser/0.1.0 (axellpz89@hotmail.com) pymediawiki/0.7.0")

def GetActiveImages(active):
    images = tboi.page(active).images
    images[:] = [x for x in images if (active in x) or ("Item_altar" in x) or ("Recharge_" in x)]
    return images


