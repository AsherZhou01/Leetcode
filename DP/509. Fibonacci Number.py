# 方法一： 自顶向下，使用memo
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 备忘录全初始化为 0
        memo = [0] * (n + 1)
        return self.dp(memo, n)

    def dp(self, memo, n):
        # base case
        if n == 0 or n == 1: 
            return n
        # 已经计算过，不用再计算了
        if memo[n] != 0: 
            return memo[n]
        memo[n] = self.dp(memo, n - 1) + self.dp(memo, n - 2)
        return memo[n]
        
    # 方法二：自底向上，使用 dp table
    # class Solution(object):
    #     def fib(self, n):
    #         """
    #         :type n: int
    #         :rtype: int
    #         """
    #         if n == 0:
    #             return 0
    #         dp = [0] * (n + 1)
    #         # base case
    #         dp[0] = 0
    #         dp[1] = 1
    #         # 状态转移
    #         for i in range(2, n + 1):
    #             dp[i] = dp[i - 1] + dp[i - 2]
    #         return dp[n]
        
    # 进一步优化，空间为Q(1)
    # class Solution(object):
    #     def fib(self, n):
    #         """
    #         :type n: int
    #         :rtype: int
    #         """
    #         if n == 0 or n == 1:
    #             # base case
    #             return n
    #         dp_i_1, dp_i_2 = 1, 0
    #         for i in range(2, n + 1):
    #             dp_i = dp_i_1 + dp_i_2
    #             # 滚动更新
    #             dp_i_2 = dp_i_1
    #             dp_i_1 = dp_i
    #         return dp_i_1
        