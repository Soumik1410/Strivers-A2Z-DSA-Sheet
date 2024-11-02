class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target and mid > 0 and nums[mid - 1] < target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            
        if nums[0] > target:
            return 0
        if nums[n - 1] < target:
            return n
