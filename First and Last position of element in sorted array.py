class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        results = []
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                results.append(mid)
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        if low > high:
            results.append(-1)
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target):
                results.append(mid)
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if low > high:
            results.append(-1)
        
        return results
        
