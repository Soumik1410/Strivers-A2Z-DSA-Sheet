class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        k = 10 ** 9 + 7
        nse = [n] * n
        pse = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        summ = 0
        for i in range(n):
            summ = (summ + (arr[i] * (i - pse[i]) * (nse[i] - i)) % k) % k
        return summ
