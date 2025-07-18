class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = float('inf')
        for x in strs:
            if len(x) < mini:
                mini = len(x)
        low = 0
        high = mini
        lcp_len = 0
        while low <= high:
            mid = (low + high) // 2
            prefix = strs[0][:mid]
            flag = 1
            for s in strs:
                if not s.startswith(prefix):
                    flag = 0
                    break
            if flag == 1:
                lcp_len = mid
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:lcp_len]

        
