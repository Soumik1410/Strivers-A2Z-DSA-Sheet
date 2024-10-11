class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum = 0
        maxi = 0
        largest = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum < 0:
                sum = 0
            if sum > maxi:
                maxi = sum
            if nums[i] > largest:
                largest = nums[i]
        if largest >= 0:
            return maxi
        else:
            return largest
