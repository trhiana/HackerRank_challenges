#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    positive = 0
    negative = 0
    neither = 0

    for i in range(length):
        if arr[i]  == 0:
            neither += 1
        elif arr[i] > 0:
            positive += 1
        else:
            negative += 1
    print(round(positive / length, 6))
    print(round(negative / length, 6))
    print(round(neither / length, 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
