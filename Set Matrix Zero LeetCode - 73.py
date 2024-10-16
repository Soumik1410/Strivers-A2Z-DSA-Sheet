class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = {}
        cols = {}
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            rows[i] = 1
        for i in range(m):
            cols[i] = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0
        for i in range(n):
            for j in range(m):
                if rows[i] != 0 and cols[j] != 0:
                    continue
                else:
                    matrix[i][j] = 0

        
