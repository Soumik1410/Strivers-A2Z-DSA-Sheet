def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    sum = 0
    i = 0
    j = 0
    result = 0
    while j < len(a):
        sum += a[j]
        if sum == k:
            result = max(result, j - i + 1)
        while sum > k:
            sum -= a[i]
            i += 1
        if sum == k:
            result = max(result, j - i + 1)
        j += 1
    return result
