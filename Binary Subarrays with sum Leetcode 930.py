class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mymap = {}
        mymap[0] = 1
        summ = 0
        count = 0
        for i in range(len(nums)):
            summ += nums[i]
            diff = summ - goal
            if diff in mymap:
                count += mymap[diff]
            mymap[summ] = mymap.get(summ, 0) + 1
        return count
        
