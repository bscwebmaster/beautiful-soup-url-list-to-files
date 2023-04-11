import sys
import os.path
import requests
from bs4 import BeautifulSoup
# open file, create the list of URLs
myurls = open('url-list.txt').read().splitlines()
# loop through that list
for myurl in myurls:
    # first get the url
    r = requests.get(myurl)
    # split the url into bits
    mypath = myurl.split(os.sep)
    # delete https: and domain
    del mypath[0]
    del mypath[1]
    # concatenate filename
    myfn = 'bsc.coop' + '_'.join(mypath) + ".html"
    # make soup
    soup = BeautifulSoup(r.content, features="html5lib")
    # delete specific tags and their contents
    for a in soup.find_all("a",string="Skip to main content"):
        a.string = ""
    for script in soup("script"):
        script.decompose()
    for noscript in soup("noscript"):
        noscript.decompose()
    for head in soup("head"):
        head.clear()
    nav1 = soup.find("div", {"id": "top-navigation"})
    nav1.decompose()
    navbarheader = soup.find("div", {"class": "navbar-header"})
    navbarheader.decompose()
    banner = soup.find("div", {"class": "container banner"})
    banner.decompose()
    soup.header.decompose()
    soup.aside.decompose()
    soup.footer.decompose()
    for e in soup.find_all(True):
        e.attrs = {}
    f = open(myfn, "w")
    f.write(soup.prettify())
    f.close
