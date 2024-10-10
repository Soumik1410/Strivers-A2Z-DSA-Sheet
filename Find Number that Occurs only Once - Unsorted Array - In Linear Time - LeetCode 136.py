class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            result ^= nums[i]
        return result
