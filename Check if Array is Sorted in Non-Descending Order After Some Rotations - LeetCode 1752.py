class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
        if nums[0] < nums[len(nums) - 1]:
            count += 1
        if count >= 2:
            return False
        else:
            return True
        
