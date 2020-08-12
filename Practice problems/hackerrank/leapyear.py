def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year%100==0 and year%400==0:
            leap=True
        elif year%100!=0:
            leap=True
        else:
            pass
    else:
        pass    
    return leap

inp=input()
year=int(inp)
print(is_leap(year))