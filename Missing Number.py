from typing import *

def missingNumber(arr : List[int], N : int) -> int:
    # Write your code here.
    count = []
    for i in range(N + 1):
        count.append(0)
    for i in range(len(arr)):
        count[arr[i]] = 1
    for i in range(1, N + 1):
        if count[i] == 0:
            return i
    return -1
