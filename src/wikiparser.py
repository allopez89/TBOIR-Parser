from mediawiki import MediaWiki
from bs4 import BeautifulSoup
import requests

tboi = MediaWiki(url="https://bindingofisaacrebirth.fandom.com/api.php", user_agent="TBOIR-WikiParser/0.1.0 (axellpz89@hotmail.com) pymediawiki/0.7.0")
sections = tboi.page("A Pony").sections
sections.remove("")
print(sections)