class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, row, col):
            if (not 0 <= row < len(grid) or not 0 <= col < len(grid[0]) or grid[row][col] == '0'):
                return
            grid[row][col] = '0'
            dfs(grid, row-1, col)
            dfs(grid, row+1, col)
            dfs(grid, row, col-1)
            dfs(grid, row, col+1)
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    dfs(grid, row, col)
        return count


# BFS来遍历岛屿
# class Solution:
#     def numIslands(self, grid: [[str]]) -> int:
#         def bfs(grid, i, j):
#             queue = [[i, j]]
#             while queue:
#                 [i, j] = queue.pop(0)
#                 if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
#                     grid[i][j] = '0'
#                     queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '0': continue
#                 bfs(grid, i, j)
#                 count += 1
#         return count

        