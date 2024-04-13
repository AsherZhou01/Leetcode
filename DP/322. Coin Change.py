# method1: bottom -> top (memo)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[1] can't be larger than amount + 1
        dp = [amount + 1] * (amount + 1)
        # base case
        dp[0] = 0
        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(len(dp)):
            # 内层 for 循环在求所有选择的最小值
            for coin in coins:
                # 子问题无解，跳过
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin]) 
        # 如果结果是初始值，则表示没有找到解。
        return -1 if dp[amount] == amount + 1 else dp[amount]
        
        


# method2: top -> bottom (memo)
# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         # initialize it with value won't be used
#         memo = [-100] * (amount + 1)
#         def dp(coins, amount):
#             if amount == 0:
#                 return 0
#             if amount < 0:
#                 return -1
#             # 查备忘录，防止重复计算
#             if memo[amount] != -100:
#                 return memo[amount]
#             res = float('inf')
#             for coin in coins:
#                 # 计算子问题的结果
#                 subProblem = dp(coins, amount - coin)
#                 # 子问题无解则跳过
#                 if subProblem == -1:
#                     continue
#                 # 在子问题中选择最优解，然后加一
#                 res = min(res, subProblem + 1)
#             # 把计算结果存入备忘录
#             memo[amount] = -1 if res == float('inf') else res
#             return memo[amount]
#         return dp(coins, amount)
        