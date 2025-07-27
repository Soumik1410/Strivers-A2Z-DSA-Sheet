class Solution:
    def backtrack(self, idx, current, nums, n, last_used, results):
        if idx == n:
            results.append(current[:])
            return
        if idx == 0 or nums[idx] != nums[idx - 1] or last_used:
            current.append(nums[idx])
            self.backtrack(idx + 1, current, nums, n, True, results)
            current.pop()
        self.backtrack(idx + 1, current, nums, n, False, results)
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        self.backtrack(0, [], nums, len(nums), True, results)
        return results
        
