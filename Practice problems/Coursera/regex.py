import re

fname = input('Enter the file name: ')
handle = open(fname)
tot = 0
for line in handle:
    line = line.rstrip()
    store = re.findall('[0-9]+',line)
    for val in store:
        tot = tot + int(val)
print(tot)