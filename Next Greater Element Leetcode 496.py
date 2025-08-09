class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mymap = {}
        for i in range(len(nums2) - 1, -1, -1):
            current = nums2[i]
            while stack and stack[-1] <= current:
                stack.pop()
            if stack:
                mymap[current] = stack[-1]
            else:
                mymap[current] = -1
            stack.append(current)
        ans = []
        for i in range(len(nums1)):
            ans.append(mymap[nums1[i]])
        return ans

        
