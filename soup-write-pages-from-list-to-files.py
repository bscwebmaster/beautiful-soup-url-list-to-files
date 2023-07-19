import sys
import re
import os.path
import requests
from bs4 import BeautifulSoup
from def_list import *
# open file, create the list of URLs
myurls = open('html/url-list.txt').read().splitlines()
# loop through that list
for myurl in myurls:
    # first get the url
    R = requests.get(myurl)
    # split the url into bits
    myname = myurl.split(os.sep)
    # delete https: and domain
    del myname[0]
    del myname[1]
    # concatenate filename
    MYFN = 'html/bsc.coop' + '_'.join(myname) + ".html"
    # make soup
    soup = BeautifulSoup(R.content, features="html5lib")

    decomposetags(soup)

    accoconv(soup)

    cleanuptags(soup)

    soup.smooth()
    f = open(MYFN, "w")
    f.write(soup.prettify())
    f.close
