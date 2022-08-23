#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):

    arr_len, brr_len = len(arr), len(brr)
    max_length = max(max(arr), max(brr))
    arr_count, brr_count = [0]*max_length, [0]*max_length
    missing_nums = []
    
    for num in brr:
        brr_count[num-1] += 1
    for num in arr:
        arr_count[num-1] += 1
    for i in range(max_length):
        if arr_count[i] != brr_count[i]:
            missing_nums.append(i+1)
    
    return missing_nums

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
