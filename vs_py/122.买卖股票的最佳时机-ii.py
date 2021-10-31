#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.profis = [-1 for _ in range(len(prices))]
        self.days= len(prices)

        def dp(start):
            if start >= self.days:
                return 0
            if self.profis[start] != -1:
                return self.profis[start]

            mpro = 0
            cur_min = prices[start]
            for sell in range(start+1, self.days):
                cur_min = min(prices[sell], cur_min)
                mpro = max(prices[sell] - cur_min + dp(sell + 1), mpro)
                print(start, sell,mpro)

            self.profis[start] = mpro
            return self.profis[start]
        t = dp(0)
        print(self.profis)
        return dp(0)


# @lc code=end

s= Solution()
s.maxProfit([7,1,5,3,6,4])