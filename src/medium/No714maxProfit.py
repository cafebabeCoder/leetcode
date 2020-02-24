class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        profit = dict()
        def dp(start):
            if start >= len(prices) - 1:
                return 0
            if start in profit:
                return profit[start]

            res = 0
            curMin = prices[start]
            for p in range(start + 1, len(prices)):
                curMin = min(curMin, prices[p])
                res = max(res, dp(p + 1) + prices[p] - curMin - fee)
            profit[start] = res
            return res
        return dp(0)

print(Solution().maxProfit([1,3,2,8,4,9], 2))
