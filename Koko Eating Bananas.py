class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            hours_needed = 0
            for i in piles:
                hours_needed += math.ceil(i / mid)
            if hours_needed <= h:
                if mid < ans:
                    ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
