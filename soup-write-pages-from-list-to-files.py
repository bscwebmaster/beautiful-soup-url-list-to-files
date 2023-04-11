import sys
import os.path
import requests
from bs4 import BeautifulSoup
# open file, create the list of URLs
myurls = open('url-list.txt').read().splitlines()
# loop through that list
for myurl in myurls:
    r = requests.get(myurl)
    soup = BeautifulSoup(r.content, features="html5lib")
    fn = os.path.basename(myurl) + ".html"
    f = open(fn, "w")
    f.write(soup.prettify())
    f.close
