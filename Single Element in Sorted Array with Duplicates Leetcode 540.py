class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 and nums[mid] != nums[mid + 1]) or \
               (mid == len(nums) - 1 and nums[mid] != nums[mid - 1]):
                return nums[mid]

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] == nums[mid + 1]:
                    low = mid + 2
                else:
                    high = mid - 1

        return nums[low]
