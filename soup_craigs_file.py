#search housing for rent in Craigslist and create file with links


import urllib
from BeautifulSoup import *
import re

url = "https://sfbay.craigslist.org/search/hhh?srchType=T&search_distance=15&postal=94020&max_price=3500&min_bedrooms=2&min_bathrooms=1&availabilityMode=2&pets_cat=1&sale_date=all+dates"
html = urllib.urlopen(url).read()
fhand = open('listing.txt', 'w')
soup = BeautifulSoup(html)
l = []
tags = soup.findAll(href = re.compile("sby/"))
for tag in tags:
    link = tag.get('href', None)
    l.append(link)

l =list(set(l))  
for i in range(len(l)):
    fhand.write(l[i]+'\n')
fhand.close()