#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    if n == 1:
        return 'Richard'
    no_of_plays = 0
    
    while n != 1:
        if math.floor(math.log2(n)) == math.ceil(math.log2(n)):
            n //= 2
        else:
            lowest_power = math.floor(math.log2(n))
            n -= pow(2,lowest_power)
        no_of_plays +=1
    
    if no_of_plays % 2 == 0:
        return 'Richard'
    else:
        return 'Louise'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
