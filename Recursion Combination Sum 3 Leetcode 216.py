class Solution:
    def backtrack(self, idx, summ, length, current, k, n, results):
        if summ > n:
            return
        if length == k:
            if summ == n:
                results.append(current[:])
                return
            else:
                return
        if idx == 9:
            return
        current.append(idx + 1)
        self.backtrack(idx + 1, summ + idx + 1, length + 1, current, k, n, results)
        current.pop()
        self.backtrack(idx + 1, summ, length, current, k, n, results)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        self.backtrack(0, 0, 0, [], k, n, results)
        return results
        
