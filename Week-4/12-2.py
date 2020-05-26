# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
pos = int(input('posistion'))
count = int(input('count'))
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
    tags = soup('a')

    x = []
    y = []

    for tag in tags :
        a = tag.get('href', None)
        x.append(a)
        b =tag.text
        y.append(a)
    print(x[pos - 1])
    print(y[pos-1])
    url = x[pos - 1]



