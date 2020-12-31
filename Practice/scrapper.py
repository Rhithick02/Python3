import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests
#ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cnt = 10
url = "https://www.tradewindsnews.com/archive"
turl = url
news = []
while cnt < 30:
    try:
        html = urllib.request.urlopen(turl, context = ctx).read()
        file = BeautifulSoup(html, 'html.parser')
        tags = file('a')
        for tag in tags:
            line = tag.get('href', None)
            if '/bulkers/' in line:
                news.append(url + line)
            if '/dry-cargo/' in line:
                news.append(url + line)
        cnt += 10
        turl = url + '?' + 'offset=' + str(cnt)
        print("page {}".format(cnt//10))
    except:
        break

newsRe = [news[0]]
for ind in range(1, len(news)):
    if news[ind] == news[ind-1]:
        continue
    newsRe.append(news[ind])

with open("links.txt", "w") as temp:
    for new in newsRe:
        temp.write(new+"\n")
