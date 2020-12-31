#If only plain texts then this can be applicable if it is html then beautiful soup will be needed
import urllib.request, urllib.parse, urllib.error

count = dict()
fh = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fh:
    words = line.strip().split()
    for word in words:
        count[word] = count.get(word,0) + 1
print(*count)