import urllib.request, xml.etree.ElementTree as ET
url = input('Enter- ')
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
Sum = 0
for item in lst:
    Sum+= int(item.find('count').text)
print(Sum)
# print(tree.find('comments').find('comment').find('name').text)

