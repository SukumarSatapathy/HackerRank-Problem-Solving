#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    n, res = len(s), 0
    for i in range(0, n, 3):
        if s[i] != 'S':
            res += 1
        if s[i+1] != 'O':
            res += 1
        if s[i+2] != 'S':
            res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

