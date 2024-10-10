from typing import *

def getSingleElement(arr : List[int]) -> int:
    # Write your code here.
    n = len(arr)
    if n == 1:
        return arr[0]
    for i in range(n):
        if i == 0 :
            if arr[i] != arr[i + 1]:
                return arr[i]
            else:
                continue
        if i == n - 1:
            if arr[i] != arr[i - 1]:
                return arr[i]
            else:
                continue
        if arr[i] != arr[i + 1] and arr[i] != arr[i - 1]:
            break
    return arr[i]
