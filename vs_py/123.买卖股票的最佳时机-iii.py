#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_trade_times = 2 
        sz = len(prices)
        dp = [[[0] * 2 for _ in range(max_trade_times+1)] for _ in range(sz)]
        for k in range(max_trade_times+1):  # 第0天
            dp[0][k][1] = -prices[0] 
        for i in range(0, sz, 1):  # 没有交易笔数
            dp[i][0][1] = float('-inf')

        for i in range(1, sz, 1):
            for k in range(1, max_trade_times+1, 1):   # k=0时， 值为0
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
        
        return dp[sz-1][max_trade_times][0]


# @lc code=end
s = Solution()
res = s.maxProfit([1,2,3,4,5])
print(res)

