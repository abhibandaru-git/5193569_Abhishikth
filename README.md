# 5193569_Abhishikth


<pdf src="https://github.com/abhibandaru-git/5193569_Abhishikth/blob/main/Git%20simple%20learn%20certification/5193569_Abhishikth%20bandaru.pdf" alt="pdf">




 
    WEEK 1 



1. MINUS PLUS

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









2 MINI MAX SUM









#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    l1 = []
    for i in arr:
        x=-i
        for j in arr:
            x += j
        l1.append(x)
    print(min(l1),max(l1))       
            
            

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)










3  TIME CONVERSION









#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    m=s[-2:]
    if m=='PM'and s[:2]!='12':
        s=str(12+int(s[:2]))+s[2:]
    if m=='AM' and s[:2]=='12':
        s='00'+s[2:]
    return s[:-2]
    
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()









   

4  SPARSE ARRAYS











#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    a=[]
    for i in queries:
        c=0
        for j in strings:
            if i==j:
                c+=1
        a.append(c)
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()











5 LONELY INTEGER










#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    dict_ = {}
    for item in a:
        if item in dict_:
            dict_[item] += 1
        else:
            dict_[item] = 1
    return(list(dict_.keys())[list(dict_.values()).index(1)])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()







6  FLIPPING BITS









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











6  DIAGNONAL DIFFERENCE






#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    l_r = 0
    r_l = 0
    l = len(arr[0]) - 1
    j = 0
    for i in arr:
        l_r += i[j]
        r_l += i[l - j]
        j += 1
    return(abs(l_r - r_l))

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()








7 COUNTING SORT 1







#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    ind = [0 for _ in range(100)]
    for i in arr:
        ind[i] += 1
    return ind

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()









8    PANGRAMS







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













9      PERMUTING TWO ARRAYS









#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i]+B[i]>=k:
            continue
        else:
            return "NO"
    return "YES"
    
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()












10      SUBARRAY DIVISION









#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    count=0
    if(m==1):
        return s.count(d)
    for  i in range(len(s)-m+1):
        if(sum(s[i:i+m])==d):
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()










11     XOR STRINGS 2








def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res= res+ '0'
        else:
            res = res + '1'

    return res

s = input()
t = input()
print(strings_xor(s, t))







    
