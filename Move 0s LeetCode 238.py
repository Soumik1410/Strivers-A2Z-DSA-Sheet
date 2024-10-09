class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        i= 0
        while i < n:
            if nums[i] == 0:
                count += 1
                nums.pop(i)
                n = len(nums)
            else:
                i += 1
        for i in range(count):
            nums.append(0)
