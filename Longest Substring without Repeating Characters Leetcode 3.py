class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxi = float('-inf')
        myset = set()
        i = 0
        for j in range(len(s)):
            while i < j and s[j] in myset:
                myset.remove(s[i])
                i += 1
            myset.add(s[j])
            maxi = max(maxi, j -i + 1)
        return maxi
            
        
