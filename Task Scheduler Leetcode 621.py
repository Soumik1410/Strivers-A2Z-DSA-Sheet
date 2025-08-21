import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)
        time = 0
        cooldown = deque()
        while max_heap or cooldown:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap)
                cnt += 1
                if cnt != 0:
                    cooldown.append((time + n, cnt))
            if cooldown and cooldown[0][0] == time:
                ready_time, task_cnt = cooldown.popleft()
                heapq.heappush(max_heap, task_cnt)
        return time
