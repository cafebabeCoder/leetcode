#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows = {}
        l = 0
        r=0
        m = 0
        while r < len(s):
            c = s[r]
            windows[c] = windows.get(c, 0) +1
            r +=1
            while windows[c] >1:
                c1 = s[l]
                windows[c1] -= 1
                l +=1
            m = max(m, r - l)
        return m



# @lc code=end

