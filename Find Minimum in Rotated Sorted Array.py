class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = nums[0]
        if len(nums) == 1:
            return nums[0]
        while low <= high:
            mid = (low + high) // 2

            if mid == 0 and nums[mid + 1] > nums[mid] and nums[mid] < nums[len(nums) - 1]:
                return nums[mid]
            if mid == len(nums) - 1 and nums[mid] < nums[mid - 1] and nums[mid] < nums[0]:
                return nums[mid]
            if mid>0 and mid<len(nums) - 1 and nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            if nums[low] <= nums[mid]:
                if nums[low] <= ans:
                    ans = nums[low]
                low = mid + 1
            else:
                if nums[mid + 1] < ans:
                    ans = nums[mid + 1]
                high = mid - 1
            
        return ans
