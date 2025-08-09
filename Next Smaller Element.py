class Solution:
    def nextSmallerElements(self, arr):
        # Your code goes here
        stack = []
        results = [-1] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                results[i] = stack[-1]
            stack.append(arr[i])
        return results
