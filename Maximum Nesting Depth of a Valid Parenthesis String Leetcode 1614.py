class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        ans = 0
        for x in s:
            if x == '(':
                count += 1
                if count > ans:
                    ans = count
            if x == ')':
                count -= 1
        return ans
        
