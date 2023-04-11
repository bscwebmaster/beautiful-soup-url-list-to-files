import sys
from bs4 import BeautifulSoup
for i in range(1, len(sys.argv)):
    prettyfile = sys.argv[1]
html_doc  = open(prettyfile, "r")
soup = BeautifulSoup(html_doc, 'html.parser')
pretty = open("pretty.html", "w")
print(soup.prettify(), file = pretty)
pretty.close()
