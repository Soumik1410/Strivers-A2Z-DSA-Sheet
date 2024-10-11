class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict = {}
        for x in nums:
            if x in mydict:
                mydict[x] += 1
            else:
                mydict[x] = 1
        for key, value in mydict.items():
            if value >= (len(nums) + 1)//2:
                return key
        return -1
