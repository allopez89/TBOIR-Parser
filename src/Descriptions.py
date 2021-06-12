from mediawiki import MediaWiki
from bs4 import BeautifulSoup
import requests
import Titles

tboi = MediaWiki(url="https://bindingofisaacrebirth.fandom.com/api.php", user_agent="TBOIR-WikiParser/0.1.0 (axellpz89@hotmail.com) pymediawiki/0.7.0")

Actives = Titles.GetActiveItems()
for active in Actives:
    Sections = tboi.page(active).sections
    Sections.remove("")
    #for section in Sections:
        
