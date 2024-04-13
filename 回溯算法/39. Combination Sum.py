# 子集/组合（元素无重可复选）=>在向下一层传递的时候传递的是i（因为可以重复，所以把自己也包括进去）
class Solution(object):
    def __init__(self):
        self.res = []
        # 记录回溯的路径
        self.track = []
        # 记录 track 中的路径和
        self.trackSum = 0

    def combinationSum(self, candidates, target):
        if len(candidates) == 0:
            return self.res
        self.backtrack(candidates, 0, target)
        return self.res

    # 回溯算法主函数
    def backtrack(self, nums, start, target):
        # base case，找到目标和，记录结果
        if self.trackSum == target:
            self.res.append(list(self.track))
            return
        # base case，超过目标和，停止向下遍历
        if self.trackSum > target:
            return

        for i in range(start, len(nums)):
            # 选择 nums[i]
            self.trackSum += nums[i]
            self.track.append(nums[i])
            # 递归遍历下一层回溯树, 同一元素可重复使用，注意参数
            self.backtrack(nums, i, target)
            # 撤销选择 nums[i]
            self.trackSum -= nums[i]
            self.track.pop()
        