class Solution(object):
    def __init__(self):
        self.count = 0
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid, row, col):
            if ( not 0 <= row < len(grid) or not 0 <= col < len(grid[0]) or grid[row][col] == 0):
                return
            # 这一题要的是每一个单元格的数量，而不是一整块陆地的数量
            self.count += 1
            grid[row][col] = 0
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)

        for row in range(len(grid)):
            if grid[row][0] == 1:
                dfs(grid, row, 0)
            if grid[row][len(grid[0])-1] == 1:
                dfs(grid, row, len(grid[0])-1)
        for col in range(len(grid[0])):
            if grid[0][col] == 1:
                dfs(grid, 0, col)
            if grid[len(grid)-1][col] == 1:
                dfs(grid, len(grid)-1, col)
        
        # 这里要记得清零
        self.count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(grid, row, col)

        return self.count
