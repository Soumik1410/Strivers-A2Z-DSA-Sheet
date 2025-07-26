class Solution:
    def backtrack(self, idx, summ, current, candidates, n, target, results):
        if summ > target:
            return
        if idx == n:
            if summ == target:
                results.append(current[:])
                return
            else:
                return
        elem = candidates[idx]
        current.append(elem)
        self.backtrack(idx, summ + elem, current, candidates, n, target, results)
        current.pop()
        self.backtrack(idx + 1, summ, current, candidates, n, target, results)
                

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        self.backtrack(0, 0, [], candidates, len(candidates), target, results)
        return results
        
