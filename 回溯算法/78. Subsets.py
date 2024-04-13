# 子集（元素无重不可复选）
class Solution(object):
    def __init__(self):
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.backtrack(nums, 0)
        return self.res

    # 回溯算法核心函数，遍历子集问题的回溯树
    def backtrack(self, nums, start):
        # 前序位置，每个节点的值都是一个子集 (start with emoty set)
        self.res.append(list(self.track))
        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 做选择
            self.track.append(nums[i])
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集 （i+1 => start）
            self.backtrack(nums, i + 1)
            # 撤销选择
            self.track.pop()
        