#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x ==0:
            return x 
        y = int(x/2)
        while y * y > x:
            y = int(y/2)
        while y*y<=x:
            y= y+1
        return y-1


# @lc code=end

