class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        ans = ""
        while i >= 0:
            if (ord(num[i]) - 48) % 2 == 1:
                ans = num[:i + 1]
                break
            i -= 1
        return ans
        
