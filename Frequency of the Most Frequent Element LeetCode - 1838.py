class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        curr_sum = 0
        l = 0
        result = 0
        
        for r in range(n):
            target = nums[r]
            curr_sum += nums[r]

            while ((r - l + 1) * target - curr_sum) > k:
                curr_sum -= nums[l]
                l += 1
            
            if (r - l + 1) > result:
                result = r - l + 1
        
        return result
