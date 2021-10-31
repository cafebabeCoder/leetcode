#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0 
        while n:
            c += 1
            n = (n-1) & n
        return c


        
# @lc code=end

