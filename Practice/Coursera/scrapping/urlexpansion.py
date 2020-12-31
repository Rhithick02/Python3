import urllib.request,ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter- ')
tags = []
for i in range(7):
    html = urllib.request.urlopen(url,context=ctx).read()
    file = BeautifulSoup(html,'html.parser')
    tags = file('a')
    url = str(tags[17].get('href',None))
print(tags[17].text)
