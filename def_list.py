import re
# play an accordion, go to jail
# convert accordions to definition lists
def accoconv(soup):
#   change parent accordion div to dl, give faq-dl class
    PTTAGS = []
    PTTAGS = soup.find_all("div", "paragraph--bp-accordion-container")
    for PTTAG in PTTAGS:
        PTTAG.name = "dl"
        PTTAG["class"] = "faq-dl"

# delete all tags with "accordion" in them
    THETAGS = ["div", "a"]
    THEATTBS = ["class", "id", "aria-controls"]
    for THETAG in THETAGS:
        for THEATTB in THEATTBS:
            for ACCTAG in soup.find_all(THETAG, {THEATTB: re.compile(".*accordion.*")}):
                ACCTAG.unwrap()

# delete card panel panel-default div
    MYTAG = soup.find("div", "card panel panel-default")
    if MYTAG is not None:
        MYTAG.unwrap()

# change panel-title divs to question dts
    PTTAGS = []
    PTTAGS = soup.find_all("div", "panel-title")
    for PTTAG in PTTAGS:
        PTTAG.name = "dt"
        PTTAG["class"] = "dl-question"

# blast away the extra paragraph tags when they're siblings of .dl-question
    SIBLINGS = []
    SIBLINGS = soup.css.select(".dl-question ~ .paragraph")
    for SIB in SIBLINGS:
        SIB.unwrap()

# rename the div.paragraph__column tags when they're siblings of .dl-question
    SIBLINGS = []
    SIBLINGS = soup.css.select(".dl-question ~ .paragraph__column")
    for SIB in SIBLINGS:
        SIB.name = "dd"
        SIB["class"] = "dl-answer"

# blast away the extra div.field tags when they're children of .dl-answer
    CHILDREN = []
    CHILDREN = soup.css.select(".dl-answer > .field")
    for CHILD in CHILDREN:
        CHILD.unwrap()

def decomposetags(soup):
    # delete script/noscript tags and their contents
    for script in soup("script"):
        script.decompose()
    for noscript in soup("noscript"):
        noscript.decompose()
    # delete specific tags
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
    # grab title
    t_tag = (soup.title)
    # empty head tag
    # put charset and title back
    a_tag = (soup.head)
    a_tag.clear()
    m_tag = soup.new_tag("meta", charset="utf-8")
    a_tag.insert(1, m_tag)
    a_tag.insert(2, t_tag)
    # remove the prefix and other attributes
    REMOVE_ATTRIBUTES = []
    REMOVE_ATTRIBUTES = ["hreflang",
                         "target",
                         "rel",
                         "title",
                         "loading",
                         "about",
                         "prefix",
                         "data-off-canvas-main-canvas",
                         "role",
                         "property",
                         "data-history-node-id",
                         "typeof",
                         "valign",
                         "data-drupal-messages-fallback"]
    for attribute in REMOVE_ATTRIBUTES:
        for tag in soup.find_all():
            del(tag[attribute])
    # unwrap span tags (make them go away)
    for SPAN in soup.find_all("span"):
        SPAN.unwrap()
