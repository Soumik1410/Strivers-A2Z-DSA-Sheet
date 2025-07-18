class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for x in s:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        ans = list(freq.items())
        ans.sort(key = lambda x: x[1], reverse = True)
        result = []
        for ch, count in ans:
            result.append(ch * count)
        return ''.join(result)
        
