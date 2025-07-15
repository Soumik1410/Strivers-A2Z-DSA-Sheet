class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = 1
        high = sum(weights)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            total_weight = 0
            req_days = 1
            for val in weights:
                if val > mid:
                    req_days = days + 1
                    break
                total_weight += val
                if total_weight > mid:
                    req_days += 1
                    total_weight = val
            if req_days <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans
