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
    def getPrimIndices (arr):
        x = len(arr)
        return list(range(0, x*x, x+1))
    def getSecoIndices (arr):
        x = len(arr)
        return list(range(x-1, x*x-1, x-1))
    p_index = getPrimIndices(arr)
    s_index = getSecoIndices(arr)  
    fll = [ i for v in arr for i in v]
    prm = [fll[i] for i in p_index]
    sec = [fll[i] for i in s_index]
    return abs(sum(prm) - sum(sec))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
