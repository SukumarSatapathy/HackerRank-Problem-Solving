#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    first_rock  = set(arr[0])
    count_gems = 0
    for mineral in first_rock:
        count_mineral = 0
        for i in range(1,n):
            if mineral in arr[i]:
                count_mineral += 1
        if count_mineral == len(arr)-1:
            count_gems += 1
    return count_gems
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
