class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        summ = 0
        maxL = 0
        maxR = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxL:
                    maxL = height[left]
                else:
                    summ += maxL - height[left]
                left += 1
            else:
                if height[right] >= maxR:
                    maxR = height[right]
                else:
                    summ += maxR - height[right]
                right -= 1
        return summ
