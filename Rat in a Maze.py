class Solution:
    def backtrack(self, i, j, current, grid, n, results, visited):
        if i == n - 1 and j == n - 1 and grid[i][j] == 1:
            results.append(current)
            return
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j] == 1:
            return
        visited[i][j] = 1
        self.backtrack(i - 1, j, current + "U", grid, n, results, visited)
        self.backtrack(i + 1, j, current + "D", grid, n, results, visited)
        self.backtrack(i, j - 1, current + "L", grid, n, results, visited)
        self.backtrack(i, j + 1, current + "R", grid, n, results, visited)
        visited[i][j] = 0

        
    def findPath(self, grid):
        #your code goes here
        results = []
        if grid[0][0] == 0:
            return -1
        visited = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
        self.backtrack(0, 0, "", grid, len(grid), results, visited)
        if len(results) == 0:
            return -1
        return results
