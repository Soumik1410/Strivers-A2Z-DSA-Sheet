class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            summ = 0
            for val in nums:
                summ += math.ceil(val / mid)
            if summ <= threshold:
                if mid < ans:
                    ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
