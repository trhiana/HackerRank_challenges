#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sums = 0
    length = len(arr)
    for i in range(length):
        sums += arr[i]
    min_sum = sums - max(arr)
    max_sum = sums - min(arr)

    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
