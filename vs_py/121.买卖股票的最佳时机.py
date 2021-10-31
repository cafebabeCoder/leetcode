#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List

# @lc code=start
class Solution:
    # dp[-1][k][0] = dp[i][0][0]= [0]
    # dp[-1][k][1] = dp[i][0][1]= -ini
    # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1][1]+price[i])
    # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-price[i])

    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)
        dp = [[0] * 2 for _ in range(sz)]
        dp[0][1] = -prices[0] 
        for i in range(1, sz, 1):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1], -prices[i])   # 只能买卖一次， 相当于每次买之前都归0
        
        print(dp)
        return dp[sz-1][0]

        
# @lc code=end

s = Solution()
res = s.maxProfit([7,1,5,3,6,4])
print(res)
