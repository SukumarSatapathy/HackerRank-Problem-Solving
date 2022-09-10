#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    uppercase = []
    lowercase = []
    len_of_str = len(s)
    ciphertext = []
    for i in range(26):
        uppercase.append(chr(i+65))
        lowercase.append(chr(i+97))
    #print(uppercase)
    #print(lowercase)
    print(ord('`'))
    
    for j in range(len_of_str):
        if s[j] in lowercase:
            key = ord(s[j]) + k%26
            if key > 122:
                key -=26
            ciphertext += chr(key)
        elif s[j] in uppercase:
            key = ord(s[j]) + k%26
            if key > 90:
                key -=26
            ciphertext += chr(key)
        else:
            ciphertext += s[j]
    return ''.join(ciphertext)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

