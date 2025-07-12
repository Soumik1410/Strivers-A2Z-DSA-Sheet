class Solution:
    def floorSqrt(self, n: int) -> int:
        low = 1
        high = n // 2
        if n == 0 or n == 1:
            return n
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= n and (mid + 1) * (mid + 1) > n:
                return mid
            elif  mid * mid < n and (mid + 1) * (mid + 1) <= n:
                low = mid + 1
            else:
                high = mid - 1
