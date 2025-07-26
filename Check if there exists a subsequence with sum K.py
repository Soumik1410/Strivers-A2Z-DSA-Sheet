class Solution:
    def backtrack(self, idx, summ, nums, n, k):
        if summ > k:
            return False
        if idx == n:
            if summ == k:
                return True
            else:
                return False
        if self.backtrack(idx + 1, summ + nums[idx], nums, n, k) == True:
            return True
        if self.backtrack(idx + 1, summ, nums, n, k) == True:
            return True
        return False

    def checkSubsequenceSum(self, nums, k):
        #your code goes here
        return self.backtrack(0, 0, nums, len(nums), k)
