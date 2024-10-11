class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = []
        for i in range(3):
            count.append(0)
        for i in range(len(nums)):
            count[nums[i]] += 1
        k = 0
        for i in range(count[0]):
            nums[k] = 0
            k += 1
        for i in range(count[1]):
            nums[k] = 1
            k += 1
        for i in range(count[2]):
            nums[k] = 2
            k += 1
