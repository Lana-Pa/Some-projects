#search housing for rent in Craigslist and create html page with links

import urllib
from BeautifulSoup import *
import re
zcode = int(raw_input("Zip code: "))
dist = int(raw_input("Distance from the zip: "))
max_price = int(raw_input("Max price: "))
min_bedr = int(raw_input("Min number of bedrooms: "))

url = "https://sfbay.craigslist.org/search/hhh?srchType=T&search_distance={dist}&postal={zcode}&max_price={max_price}&min_bedrooms={min_bedr}&min_bathrooms=1&availabilityMode=2&pets_cat=1&sale_date=all+dates".format(dist=dist,zcode=zcode,max_price=max_price,min_bedr=min_bedr)
print url
html = urllib.urlopen(url).read()
outfile = open('listing.html', 'w')
soup = BeautifulSoup(html)
l = []
tags = soup.findAll(href = re.compile("sfbay.craigslist.org"))
for tag in tags:
    link = tag.get('href', None)
    l.append(link)

l =list(set(l))  

print >>outfile, """<html>
<head>
 <title>Housing for rent</title>
</head>
<body>
<h1>Search results</h1>
"""
for i in range(len(l)):
    print >>outfile, "<p>"
    print >>outfile, '<a href="{}">Apartment {}:</a>'.format(l[i],i+1)
    print >>outfile, "</p>"
    

print >>outfile, """
</body></html>"""

outfile.close()


print "File listing.html is ready!"