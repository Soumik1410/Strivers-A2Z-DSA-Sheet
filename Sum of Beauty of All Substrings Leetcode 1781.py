class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                freq[ord(s[j]) - 97] += 1
                max_freq = max(freq)
                min_freq = min([f for f in freq if f > 0])
                ans += (max_freq - min_freq)
        return ans

        
