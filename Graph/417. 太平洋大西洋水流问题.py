class Solution(object):
    def __init__(self):
        self.res = []
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = [[False for _ in range(n)] for _ in range(m)]
        atlantic_reachable = [[False for _ in range(n)] for _ in range(m)]

        def dfs(row, col, reachable):
            reachable[row][col] = True
            # Up
            if row > 0 and not reachable[row-1][col] and heights[row-1][col] >= heights[row][col]:
                dfs(row-1, col, reachable)
            # Down
            if row < m-1 and not reachable[row+1][col] and heights[row+1][col] >= heights[row][col]:
                dfs(row+1, col, reachable)
            # Left
            if col > 0 and not reachable[row][col-1] and heights[row][col-1] >= heights[row][col]:
                dfs(row, col-1, reachable)
            # Right
            if col < n-1 and not reachable[row][col+1] and heights[row][col+1] >= heights[row][col]:
                dfs(row, col+1, reachable)

        # Initialize DFS from the pacific and atlantic edges
        for col in range(n):
            dfs(0, col, pacific_reachable)
            dfs(m-1, col, atlantic_reachable)
        for row in range(m):
            dfs(row, 0, pacific_reachable)
            dfs(row, n-1, atlantic_reachable)

        # Gather cells that can reach both oceans
        result = []
        for row in range(m):
            for col in range(n):
                if pacific_reachable[row][col] and atlantic_reachable[row][col]:
                    result.append([row, col])
        return result


# 当你设置 reachable[row][col] = True 表示从特定的起点（如太平洋或大西洋边缘）开始，该点已经被访问并且已经考虑过从这个点可达的所有路径。这意味着从这个点出发的所有可访问的单元格都已经被标记为可达。因此，如果后续的DFS过程再次遇到这个单元格，并发现它已经被标记为 True，就没有必要再次从这个单元格启动DFS，因为这会导致重复的工作，并且不会提供任何新的信息。

# 简单来说，这个条件确保了：

# 每个单元格只被探索一次，避免无效的计算。
# 避免DFS进入无限循环，尤其是在处理环状结构或者相互连通的网格时。
# 提高算法效率，减少运行时间。