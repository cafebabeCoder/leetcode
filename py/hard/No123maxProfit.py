class Solution(object):
    # 动归模板
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = dict()
        def dp(start, k):
            if start >= len(prices):
                return 0;
            if (start, k) in profit:
                return profit[(start, k)]
            if k == 0:
                return 0
            res = 0
            curMin = prices[start]
            for sell in range(start + 1, len(prices)):
                curMin = min(curMin, prices[sell])
                res = max(dp(sell + 1, k - 1) + prices[sell] - curMin, res)
            profit[(start, k)] = res
            return res
        return dp(0, 2)

print(Solution().maxProfit([1,2,3,4,5]))
