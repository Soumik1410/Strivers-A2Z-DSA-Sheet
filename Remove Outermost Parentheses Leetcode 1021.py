class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s = list(s)
        count = 0
        ans = []
        for i in range(len(s)):
            if s[i] == '(':
                if count > 0:
                    ans.append(s[i])
                count += 1
            else:
                count -= 1
                if count > 0:
                    ans.append(s[i])
        return ''.join(ans)

            
        
