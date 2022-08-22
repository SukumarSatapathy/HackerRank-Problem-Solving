#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    mid = len(s)//2
    res = 'NO'
    for i in range(mid):
        start_str = s[:i+1]
        start_int = int(start_str)
        start_num = start_int
        while(len(start_str) < len(s)):
            start_int += 1
            start_str += str(start_int)
        if s == start_str:
            res = f'''YES {start_num}'''
            break
    print(res)

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
