class Solution:
    def backtrack(self, idx, current, mappings, digits, n, results):
        if idx == n:
            if current != "":
                results.append(current)
            return
        elem = digits[idx]
        letters = mappings[elem]
        for i in range(len(letters)):
            self.backtrack(idx + 1, current + letters[i], mappings, digits, n, results)

    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        mappings = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        self.backtrack(0, "", mappings, digits, len(digits), results)
        return results
        
