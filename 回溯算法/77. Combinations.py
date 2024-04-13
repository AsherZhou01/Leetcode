# 子组合（元素无重不可复选）
class Solution(object):
    def __init__(self):
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []

    def combine(self, n, k):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.backtrack(1, n, k)
        return self.res

    # 回溯算法核心函数，遍历子集问题的回溯树
    def backtrack(self, start, n, k):
        # different with lc 78
        if k == len(self.track):
            # 遍历到了第 k 层，收集当前节点的值
            self.res.append(self.track[:])
            return
        # 回溯算法标准框架
        for i in range(start, n + 1):
            # 做选择
            self.track.append(i)
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集 （i+1 => start）
            self.backtrack(i + 1, n, k)
            # 撤销选择
            self.track.pop()
        