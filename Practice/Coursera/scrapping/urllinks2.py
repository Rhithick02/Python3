import urllib.request
from bs4 import BeautifulSoup
import re, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter- ')
html = urllib.request.urlopen(url,context=ctx).read()
file = BeautifulSoup(html,'html.parser')
Sum = 0
tags = file('span')
for tag in tags:
    Sum += int(tag.text)
    # (or)
    # tag = str(tag)
    # store = re.findall('[0-9]+',tag)
    # for val in store: Sum += int(val)
print(Sum)



