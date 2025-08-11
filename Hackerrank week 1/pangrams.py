#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    count = defaultdict(int)
    
    for char in s:
        if char in string.ascii_letters:
            count[char.lower()] += 1
    
    if len(count.keys()) == 26:
        for key in count:
            if count[key] == 0:
                return "not pangram"
    else:
        return "not pangram"
    
    return "pangram"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()


