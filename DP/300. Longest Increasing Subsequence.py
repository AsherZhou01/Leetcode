# DP解法，时间复杂度为O(n^2)，可以用二分查找优化
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 定义：dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1) 


        res = 0
        for i in range(len(dp)):
            res = max(res, dp[i])
        return res


# O（nlogn），详细的请看拉不拉东DP的那个章节
# class Solution(object):
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         top = [0 for _ in range(len(nums))]  # 牌顶数组初始化为 0
#         piles = 0  # 牌堆数初始化为 0
#         for i in range(len(nums)):
#             poker = nums[i]  # 要处理的扑克牌

#             # 搜索左侧边界的二分查找
#             left, right = 0, piles
#             while left < right:
#                 mid = (left + right) // 2
#                 if top[mid] > poker:
#                     right = mid
#                 elif top[mid] < poker:
#                     left = mid + 1
#                 else:
#                     right = mid

#             # 没找到合适的牌堆，新建一堆
#             if left == piles:
#                 piles += 1

#             # 把这张牌放到牌堆顶
#             top[left] = poker

#         # 牌堆数就是 LIS 长度
#         return piles