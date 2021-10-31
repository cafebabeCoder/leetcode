#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#  f(n) = f(n-1) + f(n - 2)

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        f0 = 1
        f1 = 1 
        for i in range(1, n, 1):
            tmp = f0 + f1
            f0 = f1
            f1 =tmp 
        return f1 


# @lc code=end

