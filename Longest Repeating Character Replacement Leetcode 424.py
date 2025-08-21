class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        freqs = {}
        maxfreq = 0
        maxlen = 0
        while r < len(s):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            maxfreq = max(maxfreq, freqs[s[r]])
            diff = (r - l + 1) - maxfreq
            while l < r and diff > k:
                freqs[s[l]] -= 1
                l += 1
                diff = (r - l + 1) - maxfreq
            if (r - l + 1) > maxlen:
                maxlen = r - l + 1
            r += 1
        return maxlen
            
                
