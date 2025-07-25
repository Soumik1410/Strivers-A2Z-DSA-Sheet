class Solution:
    def backtrack(self, current, results, nums):
        if len(nums) == 0:
            results.append(current[:])
            return
        elem = nums[0]
        rest = nums[1:]
        current.append(elem)
        self.backtrack(current, results, rest)
        current.pop()
        self.backtrack(current, results, rest)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        current = []
        self.backtrack(current, results, nums)
        return results
        
