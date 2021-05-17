class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = dict()

        def dp(start):
            if start >= len(prices):
                return 0
            if start in profit:
                return profit[start]
            res = 0
            curMin = prices[start]
            for p in range(start + 1, len(prices)):
                curMin = min(curMin, prices[p])
                res = max(res, dp(p + 2) + prices[p] - curMin)
            profit[start] = res
            return res
        return dp(0)

print(Solution().maxProfit([1,2,3,0,2]))