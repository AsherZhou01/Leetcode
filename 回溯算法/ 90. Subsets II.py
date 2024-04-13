# 子集/组合（元素可重不可复选）=> 元素重复用sort+跳过相邻元素来处理
class Solution(object):
    def __init__(self):
        self.res = []
        self.track = []
        
    def subsetsWithDup(self, nums):
        # 对给定的数组进行排序，这样相同的元素就会排在一起。
        nums.sort()
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, start):
        # 前序位置，每个节点的值都是一个子集
        self.res.append(self.track[:])
        # 从start开始遍历nums数组
        for i in range(start, len(nums)):
            # 剪枝逻辑，值相同的相邻树枝，只遍历第一条
            if i > start and nums[i] == nums[i-1]:
                continue
            # 把当前数值添加到走过的路径列表中
            self.track.append(nums[i])
            # 从下一个数字的位置继续回溯
            self.backtrack(nums, i+1)
            # 回溯过程中要把当前数值从走过的路径中移除
            self.track.pop()
        