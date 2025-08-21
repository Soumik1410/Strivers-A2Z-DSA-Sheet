class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        for x in t:
            target[x] = target.get(x, 0) + 1
        target_len = len(target)
        window = {}
        l = r = 0
        minlen = float('inf')
        res = [-1, -1]
        have = 0
        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in target and window[s[r]] == target[s[r]]:
                have += 1
            while have == target_len:
                if (r - l + 1) < minlen:
                    minlen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = res
        return s[l:r + 1] if minlen != float('inf') else ""
        
