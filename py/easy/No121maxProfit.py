class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        minPri = prices[0]  # 当前最小价格
        profit = 0
        for sell in prices:
            profit = max(profit, sell - minPri)
            minPri = min(minPri, sell)
        return profit

Solution().maxProfit([7,1,5,3,6,4])