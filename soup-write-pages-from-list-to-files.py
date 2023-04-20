import sys
import re
import os.path
import requests
from bs4 import BeautifulSoup
from def_list import *
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

    decomposetags(soup)

    cleanuptags(soup)

    accoconv(soup)

    soup.smooth()
    f = open(MYFN, "w")
    f.write(soup.prettify())
    f.close
