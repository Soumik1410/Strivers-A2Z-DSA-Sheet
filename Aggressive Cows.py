class Solution:
    def aggressiveCows(self, nums, k):
        nums.sort()
        low = 1
        high = max(nums) - min(nums)
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            last = nums[0]
            count = 1
            for i in range(1, len(nums)):
                if nums[i] - last >= mid:
                    count += 1
                    last = nums[i]
            if count < k:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        return ans
                
        
