# 排列（元素可重不可复选）
class Solution(object):
    # 定义成实例变量而不是类变量（不然tests的输出会append在一起）
    def __init__(self):
        self.res = []
        self.track = []
        self.used = []

    def permuteUnique(self, nums):
        # 先排序，让相同的元素靠在一起
        nums.sort()
        self.used = [False] * len(nums)
        self.backtrack(nums)
        return self.res
    
    def backtrack(self, nums):
        if len(self.track) == len(nums):
            self.res.append(self.track[:])
            return
        
        for i in range(len(nums)):
            if self.used[i]:
                continue
            # 新添加的剪枝逻辑，固定相同的元素在排列中的相对/前后位置(not self.used[i - 1])
            # 比如输入 nums = [1,2,2',2'']，2' 只有在 2 已经被使用的情况下才会被选择
            # 同理，2'' 只有在 2' 已经被使用的情况下才会被选择
            if i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]:
                continue
            self.track.append(nums[i])
            self.used[i] = True
            self.backtrack(nums)
            self.track.pop()
            self.used[i] = False