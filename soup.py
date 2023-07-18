import sys
import re
from bs4 import BeautifulSoup
from def_list import *
if not sys.argv[1:]:
    print("add filename")
    sys.exit()
# open file
sourcefile = sys.argv[1]
# make soup
with open(sourcefile) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

accoconv(soup)

decomposetags(soup)

cleanuptags(soup)

print(soup.prettify())
# print(soup.a)
# pretty = open("pretty.html", "w")
# print(soup.prettify(), file = pretty)
# pretty.close()
