#The link is here - http://py4e-data.dr-chuck.net/comments_761859.json
import json
import urllib.request
url = input('Enter- ')
data = urllib.request.urlopen(url).read()
jdata = json.loads(data)
Sum = 0
for val in jdata["comments"]:
    Sum+= int(val["count"])
print(Sum)
