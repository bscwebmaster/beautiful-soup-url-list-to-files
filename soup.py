import sys
import re
from bs4 import BeautifulSoup
if not sys.argv[1:]:
    print("add filename")
    sys.exit()
# open file
sourcefile = sys.argv[1]
with open(sourcefile) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
# delete specific tags and their contents
for script in soup("script"):
    script.decompose()
for noscript in soup("noscript"):
    noscript.decompose()
for head in soup("head"):
    head.clear()
skip = soup.find("a", {"class": "skip-link"})
skip.decompose()
nav1 = soup.find("div", {"id": "top-navigation"})
nav1.decompose()
navbarheader = soup.find("div", {"class": "navbar-header"})
navbarheader.decompose()
banner = soup.find("div", {"class": "container banner"})
banner.decompose()
soup.header.decompose()
soup.aside.decompose()
soup.footer.decompose()
# remove the prefix and other attributes
REMOVE_ATTRIBUTES = ['prefix', 'class', 'id', 'data-off-canvas-main-canvas', 'role', 'property', 'data-history-node-id', 'typeof', 'valign', 'data-drupal-messages-fallback']
for attribute in REMOVE_ATTRIBUTES:
    for tag in soup.findAll():
        del(tag[attribute])
print(soup.prettify())
# pretty = open("pretty.html", "w")
# print(soup.prettify(), file = pretty)
# pretty.close()
