class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = 1
        high = max(bloomDay)
        ans = high
        flag = 0
        while low <= high:
            mid = (low + high) // 2
            flowersinarow = 0
            bouqets = 0
            for val in bloomDay:
                if val <= mid:
                    flowersinarow += 1
                else:
                    flowersinarow = 0
                if flowersinarow == k:
                    bouqets += 1
                    flowersinarow = 0
            if bouqets >= m:
                flag = 1
                if mid < ans:
                    ans = mid
                high = mid - 1
            else:
                low = mid + 1
        if flag == 0:
            return -1
        else:
            return ans
