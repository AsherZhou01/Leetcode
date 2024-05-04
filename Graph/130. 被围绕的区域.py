class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        def dfs(board, row, col):
            if ( not 0 <= row < len(board) or not 0 <= col < len(board[0]) or board[row][col] != 'O'):
                return
            board[row][col] = 'A'
            dfs(board, row + 1, col)
            dfs(board, row - 1, col)
            dfs(board, row, col + 1)
            dfs(board, row, col - 1)

        for row in range(len(board)):
            dfs(board, row, 0)
            dfs(board, row, len(board[0])-1)
        for col in range(len(board[0])):
            dfs(board, 0, col)
            dfs(board, len(board)-1, col)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'A':
                    board[row][col] = 'O'