def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x and mid > 0 and  arr[mid - 1] < x:
            return mid
        if arr[mid] >= x:
            high = mid - 1
        else:
            low = mid + 1
    if arr[0] >= x:
        return 0
    else:
        return n
