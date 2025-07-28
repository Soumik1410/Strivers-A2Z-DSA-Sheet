import random
class Solution:
    def palindrome(self, s):
        return s == s[::-1]
    def backtrack(self, idx, current, s, results):
        if idx == len(s):
            results.append(current[:])
            return
        for i in range(idx + 1, len(s) + 1):
            substring = s[idx:i]
            if self.palindrome(substring):
                current.append(substring)
                self.backtrack(i, current, s, results)
                current.pop()
        
    def partition(self, s: str) -> List[List[str]]:
        results = []
        self.backtrack(0, [], s, results)
        return results
    
