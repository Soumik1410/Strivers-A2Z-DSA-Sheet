from typing import *

def longestSuccessiveElements(a : List[int]) -> int:
    # Write your code here.
    a.sort()
    max = 1
    sum = 1
    n = len(a)
    i = 0
    while i < n - 1:
        if a[i] == a[i + 1]:
            a.pop(i)
            n = len(a)
            continue
        i += 1
    #print(a)
    n = len(a)
    for i in range(n-1):
        #print(sum, i, end = "\t")
        if a[i + 1] - a[i] == 1:
            sum += 1
        else:
            if sum > max:
                max = sum
            sum = 1
    
    if sum > max:
        max = sum
    return max
