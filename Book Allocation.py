class Solution:
    def findPages(self, nums, m):
        low = 1
        high = sum(nums)
        ans = -1
        if m > len(nums):
            return ans

        while low <= high:
            mid = (low + high) // 2
            pages = 0
            students = 1
            for val in nums:
                if val > mid:
                    students = m + 1
                    break
                pages += val
                if pages > mid:
                    pages = val
                    students += 1
            if students > m:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
