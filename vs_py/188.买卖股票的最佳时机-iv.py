#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        sz = len(prices)
        if sz < 1:
            return 0
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(sz)]
        # 
        for s in range(1, k + 1, 1):
            dp[0][s][1] = -prices[0]
        for i in range(sz):
            dp[i][0][1] = float('-inf')

        for i in range(1, sz, 1):
            for s in range(1, k+1, 1):
                dp[i][s][0] = max(dp[i-1][s][0], dp[i-1][s][1]+prices[i])
                dp[i][s][1] = max(dp[i-1][s][1], dp[i-1][s-1][0]-prices[i])
        
        return dp[sz-1][k][0]


# @lc code=end
s = Solution()
res = s.maxProfit(2, [3,2,6,5,0,3])
print(res)


