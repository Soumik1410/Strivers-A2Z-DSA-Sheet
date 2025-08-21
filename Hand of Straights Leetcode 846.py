class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)
        min_heap = list(freq.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                if freq[i] == 0:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    if i == min_heap[0]:
                        heapq.heappop(min_heap)
        return True
