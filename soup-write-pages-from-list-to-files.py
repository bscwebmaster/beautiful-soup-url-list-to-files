import sys
import os.path
import requests
from bs4 import BeautifulSoup
# open file, create the list of URLs
myurls = open('sitemap.txt').read().splitlines()
# loop through that list
for myurl in myurls:
    r = requests.get(myurl)
    soup = BeautifulSoup(r.content)
    fn = os.path.basename(myurl)
    f = open(fn, "w")
    f.write(soup.prettify())
    f.close
