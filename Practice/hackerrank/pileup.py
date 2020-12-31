# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    myser=set(arr)
    if len(myser)<=2:
        print("Yes")
    else:
        count=0
        x=0
        y=len(arr)-1
        for i in range(n):
            if arr[x]>=arr[x+1] and arr[x]>=arr[y]:
                x+=1
            elif arr[y]>=arr[y-1]:
                y-=1
            elif x==y:
                break
            else:
                count=-1
                break
        if count!=-1:
            print("Yes")
        else:
            print("No")
    t-=1

        
        
