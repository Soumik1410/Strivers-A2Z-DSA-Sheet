class Solution:
    def backtrack(self, idx, summ, nums, n, results):
        if idx == n:
            results.append(summ)
            return
        self.backtrack(idx + 1, summ + nums[idx], nums, n, results)
        self.backtrack(idx + 1, summ, nums, n, results)
    def subsetSums(self, nums):
        #your code goes here
        results = []
        self.backtrack(0, 0, nums, len(nums), results)
        return results
