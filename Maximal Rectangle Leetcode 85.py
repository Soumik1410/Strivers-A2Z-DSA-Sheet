class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse = [n] * n
        pse = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        
        maxi = 0
        for i in range(n):
            rect = (nse[i] - pse[i] - 1) * heights[i] 
            if rect > maxi:
                maxi = rect
        return maxi 
        
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0

        for row in matrix:
            for j in range(n):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area
