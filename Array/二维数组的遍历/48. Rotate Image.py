# 旋转90 = 镜像对称 + reverse row （顺逆时针不一样）
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先沿对角线镜像对称二维矩阵
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 然后反转二维矩阵的每一行
        for row in matrix:
            self.reverse(row)

    # 反转一维数组
    def reverse(self, arr):
        i, j = 0, len(arr)-1
        while j > i:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
        