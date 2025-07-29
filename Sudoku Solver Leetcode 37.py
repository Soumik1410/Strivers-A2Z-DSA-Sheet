class Solution:
    def findBox(self, r, c):
        if r <= 2 and c <= 2:
            return 0
        if r <= 2 and c <= 5:
            return 1
        if r <= 2 and c <= 8:
            return 2
        if r <= 5 and c <= 2:
            return 3
        if r <= 5 and c <= 5:
            return 4
        if r <= 5 and c <= 8:
            return 5
        if r <= 8 and c <= 2:
            return 6
        if r <= 8 and c <= 5:
            return 7
        if r <= 8 and c <= 8:
            return 8
        
    def backtrack(self, r, c, board, rows, cols, boxes):
        if c == 9:
            r += 1
            if r == 9:
                return True
            c = 0
        if board[r][c] != '.':
            return self.backtrack(r, c + 1, board, rows, cols, boxes)
        box_no = self.findBox(r, c)
        for number in range(1, 10):
            if rows[r][number - 1] == 1 or cols[c][number - 1] == 1 or boxes[box_no][number - 1] == 1:
                continue
            board[r][c] = str(number)
            rows[r][number - 1] = 1 
            cols[c][number - 1] = 1 
            boxes[box_no][number - 1] = 1
            if self.backtrack(r, c + 1, board, rows, cols, boxes):
                return True

            board[r][c] = '.'
            rows[r][number - 1] = 0 
            cols[c][number - 1] = 0 
            boxes[box_no][number - 1] = 0
        
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9)]
        boxes = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i][num - 1] = 1
                    cols[j][num - 1] = 1
                    box_no = self.findBox(i, j)
                    boxes[box_no][num - 1] = 1
        
        self.backtrack(0, 0, board, rows, cols, boxes)

        
