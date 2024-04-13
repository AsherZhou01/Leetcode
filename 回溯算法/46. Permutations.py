class Solution(object):
    def __init__(self):
        self.res = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 记录「路径」
        track = []
        # 「路径」中的元素会被标记为 true，避免重复使用
        used = [False] * len(nums)
        
        self.backtrack(nums, track, used)
        return self.res

    # 路径：记录在 track 中
    # 选择列表：nums 中不存在于 track 的那些元素（used[i] 为 false）
    # 结束条件：nums 中的元素全都在 track 中出现
    def backtrack(self, nums, track, used):
        # 触发结束条件
        if len(track) == len(nums):
            # 这里是一个浅拷贝（对于int来说已经够了）
            self.res.append(track[:])
            return
        for i in range(len(nums)):
            # 排除不合法的选择
            if used[i]: 
                # nums[i] 已经在 track 中，跳过
                continue
            # 做选择
            track.append(nums[i])
            used[i] = True
            # 进入下一层决策树
            self.backtrack(nums, track, used)
            # 回溯：取消选择
            track.pop()
            used[i] = False

# 优化：swap，这样不用used
# class Solution:
#     def __init__(self):
#         self.result = []

#     def permute(self, nums):
#         self.backtrack(nums, 0)
#         return self.result

#     # 回溯算法核心框架
#     def backtrack(self, nums, start):
#         if start == len(nums):
#             # 找到一个全排列，Java 需要转化成 List 类型
#             self.result.append(nums[:])
#             return

#         for i in range(start, len(nums)):
#             # 做选择
#             self.swap(nums, start, i)
#             # 递归调用，传入 start + 1
#             self.backtrack(nums, start + 1)
#             # 撤销选择
#             self.swap(nums, start, i)

#     def swap(self, nums, i, j):
#         temp = nums[i]
#         nums[i] = nums[j]
#         nums[j] = temp
