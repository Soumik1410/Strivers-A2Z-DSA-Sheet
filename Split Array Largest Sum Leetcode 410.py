class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = 0
        high = sum(nums)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            summ = 0
            count = 1
            for val in nums:
                if val > mid:
                    count = k + 1
                    break
                summ += val
                if summ > mid:
                    count += 1
                    summ = val
            if count > k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
