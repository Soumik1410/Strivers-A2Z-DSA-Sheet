class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0
        i = 0
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                flag = 1
                break
        
        if flag == 0:
            nums.reverse()
            return
        
        j = n - 1
        while j >= i + 1:
            if nums[j] > nums[i]:
                break
            j -= 1
        
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

        i = i + 1
        j = n - 1
        while i <= j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
