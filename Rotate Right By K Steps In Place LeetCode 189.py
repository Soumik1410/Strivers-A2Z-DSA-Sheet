class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        B = []
        for i in range(len(nums)):
            B.append(0)
        for i in range(len(nums)):
            B[(i + k) % len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i] = B[i]
