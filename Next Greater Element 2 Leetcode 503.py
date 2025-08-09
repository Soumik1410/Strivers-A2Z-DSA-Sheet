class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        results = [-1] * len(nums)
        for i in range(2 * len(nums) - 1, -1, -1):
            current = nums[i % len(nums)]
            while stack and stack[-1] <= current:
                stack.pop()
            if i < len(nums) and stack:
                results[i] = stack[-1]
            stack.append(current)
        return results
        
