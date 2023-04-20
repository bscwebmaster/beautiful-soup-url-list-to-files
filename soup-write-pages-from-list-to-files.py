import sys
import re
import os.path
import requests
from bs4 import BeautifulSoup
# open file, create the list of URLs
myurls = open('url-list.txt').read().splitlines()
# loop through that list
for myurl in myurls:
    # first get the url
    R = requests.get(myurl)
    # split the url into bits
    MYPATH = myurl.split(os.sep)
    # delete https: and domain
    del MYPATH[0]
    del MYPATH[1]
    # concatenate filename
    MYFN = 'bsc.coop' + '_'.join(MYPATH) + ".html"
    # make soup
    soup = BeautifulSoup(R.content, features="html5lib")
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
    REMOVE_ATTRIBUTES = ['prefix', 'data-off-canvas-main-canvas', 'role', 'property', 'data-history-node-id', 'typeof', 'valign', 'data-drupal-messages-fallback']
    for attribute in REMOVE_ATTRIBUTES:
        for tag in soup.findAll():
            del(tag[attribute])
    # unwrap span tags (make them go away)
    for SPAN in soup.find_all('span'):
        SPAN.unwrap()
    # play an accordian, go to jail
    THETAGS = []
    THETAGS = ["div", "a"]
    THEATTBS = []
    THEATTBS = ["class", "id", "aria-controls"]
    for THETAG in THETAGS:
        for THEATTB in THEATTBS:
            for ACCTAG in soup.find_all(THETAG, {THEATTB: re.compile(".*accordion.*")}):
                ACCTAG.unwrap()
    soup.smooth()
    f = open(MYFN, "w")
    f.write(soup.prettify())
    f.close
