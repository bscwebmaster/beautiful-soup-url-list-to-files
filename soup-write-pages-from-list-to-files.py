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
    f = open(myfn, "w")
    f.write(soup.prettify())
    f.close
