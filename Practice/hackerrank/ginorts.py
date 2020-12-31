string = input()
a = sorted(string)
string = "".join(a)
a=""
for i in string:
    if i.islower():
        a+=i
for i in string:
    if i.isupper():
        a+=i
for i in string:
    if i.isdigit() and int(i)%2!=0:
        a+=i
for i in string:
    if i.isdigit() and int(i)%2==0:
        a+=i
print(a)
        
