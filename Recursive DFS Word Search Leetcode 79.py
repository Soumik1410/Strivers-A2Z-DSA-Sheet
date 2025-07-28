class Solution:
    def backtrack(self, idx, word, i, j, board, visited):
        if idx == len(word):
            return True
        if i == len(board) or i == -1:
            return False
        if j == len(board[0]) or j == -1:
            return False
        if visited[i][j] == 1:
            return False
        if board[i][j] != word[idx]:
            return False
        visited[i][j] = 1
        ans = (self.backtrack(idx + 1, word, i - 1, j, board, visited) or
                self.backtrack(idx + 1, word, i, j + 1, board, visited) or
                self.backtrack(idx + 1, word, i + 1, j, board, visited) or
                self.backtrack(idx + 1, word, i, j - 1, board, visited))
        visited[i][j] = 0
        return ans
        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = []
        for i in range(len(board)):
            visited.append([0] * len(board[0]))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.backtrack(0, word, i, j, board, visited):
                        return True

        return False
        
