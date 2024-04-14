class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # 定义：preSum[i][j] 记录 matrix 中子矩阵 [0, 0, i-1, j-1] 的元素和
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0: return
        # 构造前缀和矩阵
        self.preSum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 计算每个矩阵 [0, 0, i, j] 的元素和
                self.preSum[i][j] = self.preSum[i-1][j] + self.preSum[i][j-1] + matrix[i-1][j-1] - self.preSum[i-1][j-1]

        
    # x: row, y: col
    def sumRegion(self, x1, y1, x2, y2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # 目标矩阵之和由四个相邻矩阵运算获得
        return self.preSum[x2+1][y2+1] - self.preSum[x1][y2+1] - self.preSum[x2+1][y1] + self.preSum[x1][y1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)