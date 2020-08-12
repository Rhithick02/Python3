#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    ls=list(s)
    i='a'
    lis=[0]*26
    se=set(s)
#    print(*se)
    for i in se:
        lis[ord(i)-97]=ls.count(i)
#        print(lis[ord(i)-97])
    
    for j in range(3):
        maxi=0
        maxin=0
        for i in range(len(lis)):
            if lis[i]>maxi:
                maxi=lis[i]
                maxin=i
        print(chr(maxin+97),maxi)
        lis[maxin]=0
        
        

        
