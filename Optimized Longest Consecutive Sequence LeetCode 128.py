class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mydict = {}
        for x in nums:
            if x not in mydict:
                mydict[x] = 1
        maxi = 1
        for k,v in mydict.items():
            length = 1
            if k-1 not in mydict:
                j = 1
                while(True):
                    if k+j in mydict:
                        length += 1
                        j += 1
                        continue
                    break
            if length > maxi:
                maxi = length
        return maxi
