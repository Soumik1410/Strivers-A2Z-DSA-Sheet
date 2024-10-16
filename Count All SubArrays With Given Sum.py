from os import *
from sys import *
from collections import *
from math import *

def findAllSubarraysWithGivenSum(arr, s):
    # Write your code here.
    mydict = {}
    mydict[0] = -1
    sum = 0
    count = 0
    for i in range(len(arr)):
        sum += arr[i]
        diff = sum - s
        if diff in mydict:
            count += 1
        if sum not in mydict:
            mydict[sum] = i
            if sum == s:
                count = 1
    return count
