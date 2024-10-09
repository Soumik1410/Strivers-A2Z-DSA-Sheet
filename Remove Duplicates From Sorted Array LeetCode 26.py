class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        n = len(nums)
        i = 1
        while i < n:
            if nums[i - 1] != nums[i]:
                k += 1
            else:
                nums.pop(i)
                i -= 1
                n = len(nums)
            i += 1
        return k
