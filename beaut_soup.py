import urllib
from BeautifulSoup import *

url = "https://sfbay.craigslist.org/"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
tags = soup('a')

for tag in tags:
    print "-------------------------------------------------"
    print 'TAG:', tag
    print 'URL:', tag.get('href', None)
    print 'Content:', tag.contents[0]
    print 'Attrs:', tag.attrs 