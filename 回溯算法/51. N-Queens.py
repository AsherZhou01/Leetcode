class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n):
        board = [["."] * n for _ in range(n)]
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board, row):
        # last row + 1
        if row == len(board):
            self.res.append(["".join(r) for r in board])  # r代表行
            return
        n = len(board[row])
        for col in range(n):
            # check if this position is valid, skip it if not
            if not self.isValid(board, row, col):
                continue
            board[row][col] = "Q"
            # enter next level
            self.backtrack(board, row + 1)
            # reset the operation
            board[row][col] = "."
            
    def isValid(self, board, row, col):
        n = len(board)
        # 检查列是否有皇后冲突
        for i in range(row):  # 只需要检查当前行之前的行
            if board[i][col] == "Q":
                return False
        # 检查右上方是否有皇后冲突
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
        # 检查左上方是否有皇后冲突
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        return True

