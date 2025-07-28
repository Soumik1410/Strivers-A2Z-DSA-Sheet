class Solution:
    def backtrack(self, r, n, board, cols, main_diag, anti_diag, results):
        if r == n:
            solution = [''.join(row) for row in board]
            results.append(solution)
            return
        for c in range(n):
            if c in cols or (r - c) in main_diag or (r + c) in anti_diag:
                continue
            board[r][c] = 'Q'
            cols.add(c)
            main_diag.add(r - c)
            anti_diag.add(r + c)

            self.backtrack(r + 1, n, board, cols, main_diag, anti_diag, results)

            board[r][c] = '.'
            cols.remove(c)
            main_diag.remove(r - c)
            anti_diag.remove(r + c)

    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        main_diag = set()
        anti_diag = set()
        self.backtrack(0, n, board, cols, main_diag, anti_diag, results)
        return results
