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
# empty head tag
# put charset back
a_tag = (soup.head)
a_tag.clear()
new_tag = soup.new_tag("meta", charset="utf-8")
a_tag.insert(1, new_tag)
# delete some stuff
DELETE_TAGS = []
DELETE_TAGS = [
        ("a", "class", "skip-link"),
        ("div", "id", "top-navigation"),
        ("div", "class", "container banner"),
        ]
for DELETE_TAG in DELETE_TAGS:
    MYTAG = soup.find(DELETE_TAG[0], {DELETE_TAG[1]: DELETE_TAG[2]})
    MYTAG.decompose()
soup.header.decompose()
soup.aside.decompose()
soup.footer.decompose()

# remove the prefix and other attributes
REMOVE_ATTRIBUTES = []
REMOVE_ATTRIBUTES = ['prefix', 'data-off-canvas-main-canvas', 'role', 'property', 'data-history-node-id', 'typeof', 'valign', 'data-drupal-messages-fallback']
for attribute in REMOVE_ATTRIBUTES:
    for tag in soup.find_all():
        del(tag[attribute])
# unwrap span tags (make them go away)
for SPAN in soup.find_all('span'):
    SPAN.unwrap()
# play an accordian, go to jail
# first delete all tags with "accordion" in them
THETAGS = []
THETAGS = ["div", "a"]
THEATTBS = []
THEATTBS = ["class", "id", "aria-controls"]
for THETAG in THETAGS:
    for THEATTB in THEATTBS:
        for ACCTAG in soup.find_all(THETAG, {THEATTB: re.compile(".*accordion.*")}):
            ACCTAG.unwrap()
# modify all "panel-title" tags
PTTAGS = soup.find_all("div", "panel-title")
NEWTAG = soup.new_tag("h2")
for PTTAG in PTTAGS:
    PTTAG.replace_with(NEWTAG)

print(soup.prettify())
# print(soup.a)
# pretty = open("pretty.html", "w")
# print(soup.prettify(), file = pretty)
# pretty.close()
