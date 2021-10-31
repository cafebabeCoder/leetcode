#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^y
        cnt = 0
        while diff:
            cnt += diff & 1
            diff = diff // 2
            # print(cnt)
        return cnt

# @lc code=end
s = Solution()
print(s.hammingDistance(1, 3))

