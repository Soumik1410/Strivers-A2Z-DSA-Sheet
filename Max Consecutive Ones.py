class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_so_far = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                if count > max_so_far:
                    max_so_far = count
                count = 0
        if count > max_so_far:
            max_so_far = count
        return max_so_far
