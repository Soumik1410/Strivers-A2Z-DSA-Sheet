class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freqs = {}
        l = r = 0
        count = 0
        while r < len(s):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            while len(freqs) == 3:
                count += len(s) - r
                freqs[s[l]] -= 1
                if freqs[s[l]] == 0:
                    del freqs[s[l]]
                l += 1
            r += 1
        return count
