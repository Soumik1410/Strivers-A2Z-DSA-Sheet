def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x and mid > 0 and arr[mid - 1] <= x:
            return mid
        if arr[mid] <= x:
            low = mid + 1
        else:
            high = mid - 1
    if n > 1 and arr[0] <= x and arr[1] > x:
        return 1
    if arr[0] > x:
        return 0
    return n;
