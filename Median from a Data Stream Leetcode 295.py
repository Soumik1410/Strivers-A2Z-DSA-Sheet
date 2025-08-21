import heapq
class MedianFinder:

    def __init__(self):
        self.k = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        if len(self.max_heap) - len(self.min_heap) > 1:
            transfer = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -transfer)
        if len(self.min_heap) > len(self.max_heap):
            transfer = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -transfer)
        self.k += 1

    def findMedian(self) -> float:
        if self.k % 2 == 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2         


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
