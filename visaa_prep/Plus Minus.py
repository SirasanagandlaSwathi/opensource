#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos=0
    neg=0
    ze=0
    for i in arr:
        if i<0:
            neg+=1
        elif i>0:
            pos+=1
        else:
            ze+=1
    print(pos/len(arr))
    print(neg/len(arr))
    print(ze/len(arr))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
