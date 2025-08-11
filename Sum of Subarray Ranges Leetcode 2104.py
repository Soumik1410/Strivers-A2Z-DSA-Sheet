class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        nse = [n] * n
        pse = [-1] * n
        nge = [n] * n
        pge = [-1] * n

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                nge[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                pge[i] = stack[-1]
            stack.append(i)
        
        summ = 0
        for i in range(n):
            summ = summ + nums[i] * (nge[i] - i) * (i - pge[i]) - nums[i] * (nse[i] - i) * (i - pse[i])
        return summ
