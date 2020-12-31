import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter- ')
html = urllib.request.urlopen(url,context=ctx).read()
file = BeautifulSoup(html,'html.parser')
tags = file('a')
for tag in tags:
    print(tag.get('href',None))
    #To view the content instead of above line, tag.text
