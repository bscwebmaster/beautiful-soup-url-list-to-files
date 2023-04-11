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
    # testing: print the url
    print(os.path.relpath(myurl))
    # split the url into bits
    mypath = myurl.split(os.sep)
    # delete https: and domain
    del mypath[0]
    del mypath[1]
    myfn = 'bsc.coop' + '_'.join(mypath) + ".html"
    print(myfn)
    soup = BeautifulSoup(r.content, features="html5lib")
    fn = os.path.basename(myurl) + ".html"
    f = open(fn, "w")
    f.write(soup.prettify())
    f.close
