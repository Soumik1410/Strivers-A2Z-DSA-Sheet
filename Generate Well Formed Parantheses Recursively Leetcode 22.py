class Solution:
    def backtrack(self, current, count, n, result):
        if len(current) == 2*n:
            if count == 0:
                result.append(current)
            return
        if count < 0:
            return
        self.backtrack(current + '(', count + 1, n, result)
        self.backtrack(current + ')', count - 1, n, result)
    
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack('', 0, n, result)
        return result
        
