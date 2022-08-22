#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s)//2
    s1 = s[:mid]
    s2 = s[mid:]
    count_s1 = [0]*26
    count_s2 = [0]*26
    chr_rep = 0
    
    for i in range(mid):
        pos_s1 = ord(s1[i])-97
        count_s1[pos_s1] += 1
        pos_s2 = ord(s2[i])-97
        count_s2[pos_s2] += 1
    
    for i in range(26):
        if count_s2[i] != count_s1[i]:
            chr_rep += abs(count_s1[i]-count_s2[i])
    
    return chr_rep//2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
