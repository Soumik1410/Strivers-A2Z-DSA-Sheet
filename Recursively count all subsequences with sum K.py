class Solution:
    def backtrack(self, current_sum, nums,k):
        if len(nums) == 0:
            if current_sum == k:
                return 1
            else:
                return 0
        ans = 0
        elem = nums[0]
        rest = nums[1:]
        ans += self.backtrack(current_sum + elem, rest, k)
        ans += self.backtrack(current_sum, rest, k)
        return ans

    def countSubsequenceWithTargetSum(self, nums, k):
        #your code goes here
        return self.backtrack(0, nums, k)
