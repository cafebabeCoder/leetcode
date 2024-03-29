#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
from typing import List
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            t = s[l]
            s[l] = s[r]
            s[r] = t
            l += 1
            r -= 1

# @lc code=end

s = Solution()
st = ["h","e","l","l","o"]
s.reverseString(st)
print(st)
