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
    disk = {"pos" : 0, "neg":0, "zero":0}
    for i in arr:
        if int(i) > 0:
            disk["pos"] +=1
        elif int(i) <0:
            disk ["neg"] +=1
        else:
             disk["zero"] +=1
    print(format(disk["pos"]/n, '.3f'))
    print(format(disk["neg"]/n, '.3f'))
    print(format(disk["zero"]/n, '.3f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)