#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binary_n = "{0:b}".format(n)
    inverse_s = ''
    bin_32 = binary_n.zfill(32)
    for i in list(bin_32):
        if i == '0':
            inverse_s += '1' 
        else:
            inverse_s += '0' 
    return(int(inverse_s, 2))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
