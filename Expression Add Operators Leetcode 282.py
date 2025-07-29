class Solution:
    def backtrack(self, idx, curr, ans, last_operand, num, target, n, results):
        if idx == n:
            if ans == target:
                results.append(curr)
            return
        for i in range(idx, n):
            if i != idx and num[idx] == '0':
                break
            current_str = num[idx:i+1]
            current_val = int(current_str)
            if idx == 0:
                self.backtrack(i + 1, current_str, current_val, current_val, num, target, n, results)
            else:
                self.backtrack(i + 1, curr + '+' + current_str, ans + current_val, current_val, num, target, n, results)
                self.backtrack(i + 1, curr + '-' + current_str, ans - current_val, -current_val, num, target, n, results)
                new_ans = ans - last_operand + (last_operand * current_val)
                self.backtrack(i + 1, curr + '*' + current_str, new_ans, last_operand * current_val, num, target, n, results)
        
    def addOperators(self, num: str, target: int) -> List[str]:
        results = []
        self.backtrack(0, "", 0, 0, num, target, len(num), results)
        return results
        
