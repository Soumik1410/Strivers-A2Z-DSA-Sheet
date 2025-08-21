import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in nums[k:]:
            heapq.heappushpop(min_heap, i)
        return min_heap[0]
