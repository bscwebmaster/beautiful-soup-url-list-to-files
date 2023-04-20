# play an accordion, go to jail
import re
# convert accordions to definition lists
# first delete all tags with "accordion" in them
def accoconv(soup):
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

def decomposetags(soup):
    # delete script/noscript tags and their contents
    for script in soup("script"):
        script.decompose()
    for noscript in soup("noscript"):
        noscript.decompose()
    # delete specific tags
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

def cleanuptags(soup):
    # empty head tag
    # put charset back
    a_tag = (soup.head)
    a_tag.clear()
    new_tag = soup.new_tag("meta", charset="utf-8")
    a_tag.insert(1, new_tag)
    # remove the prefix and other attributes
    REMOVE_ATTRIBUTES = []
    REMOVE_ATTRIBUTES = ['prefix', 'data-off-canvas-main-canvas', 'role', 'property', 'data-history-node-id', 'typeof', 'valign', 'data-drupal-messages-fallback']
    for attribute in REMOVE_ATTRIBUTES:
        for tag in soup.find_all():
            del(tag[attribute])
    # unwrap span tags (make them go away)
    for SPAN in soup.find_all('span'):
        SPAN.unwrap()
