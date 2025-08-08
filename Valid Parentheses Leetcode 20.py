class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if len(stack) == 0 and (x == ')' or x == ']' or x == '}'):
                return False
            if len(stack) == 0:
                stack.append(x)
                continue
            if x == '(' or x == '[' or x == '{':
                stack.append(x)
                continue
            if (x == ')' and stack[-1] == '(') or (x == ']' and stack[-1] == '[') or (x == '}' and stack[-1] == '{'):
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        
