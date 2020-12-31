# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
while t>0:
    card=input().strip()
    count=0
    if len(card)>19 or not(card[0]=='4' or card[0]=='5' or card[0]=='6'):
        print("Invalid")
    else:
        for cha in card:
            if cha.isdigit():
                count+=1
        if count!=16:
            print("Invalid")
        else:
            count=0
            string=card.replace('-','')
            if len(string)==16:
                for i in range(15):
                    if string[i]==string[i+1]:
                        count+=1
                    elif count>0 and string[i]!=string[i+1]:
                        count=0
                    if count==3:
                        break
                if count==3:
                    print("Invalid")
                elif len(card)==16:
                    print("Valid")
                elif len(card)==19:
                    if card[4]=='-' and card[9]=='-' and card[14]=='-':
                        print("Valid")
                    else: 
                        print("Invalid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
    t-=1
