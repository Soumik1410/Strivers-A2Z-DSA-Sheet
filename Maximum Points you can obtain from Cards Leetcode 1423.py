class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        mini = summ = sum(cardPoints[:n - k])
        total = sum(cardPoints)
        l = 0
        r = n - k
        while r < len(cardPoints):
            summ += cardPoints[r] - cardPoints[l]
            mini = min(mini, summ)
            r += 1
            l += 1
        return total - mini
