class Solution:
    def atMostK(self, s, k):
        if k == 0:
            return 0
        l = r = 0
        freqs = {}
        count = 0
        while r < len(s):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            while l < r and len(freqs) > k:
                freqs[s[l]] -= 1
                if freqs[s[l]] == 0:
                    del freqs[s[l]]
                l += 1
            count += r - l + 1
            r += 1
        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)
