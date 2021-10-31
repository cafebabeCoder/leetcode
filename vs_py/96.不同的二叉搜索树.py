#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        self.dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
        # for i in range(n+1):
        #     for j in range(n+1):
        #         self.dp[i][j] = 0
        r = self.cul(1, n)
        print(self.dp)
        return r


    
    def cul(self, n, m):
        if n>m:
            return 1
        if self.dp[n][m] != 0:
            return self.dp[n][m]
        res = 0
        for i in range(n, m+1, 1):
            left = self.cul(n, i-1)
            right = self.cul(i+1, m)
            res += (left * right)
        
        self.dp[n][m] = res
        
        return res




# @lc code=end
s = Solution()
t = s.numTrees(4)
print(t)
