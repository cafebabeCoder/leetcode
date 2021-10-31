#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        windows = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        # print(need)

        l = 0
        r = 0
        valid = 0
        start = 0
        length = float('inf')
        while r < len(s):
            # 右滑
            if s[r] in need:
                windows[s[r]] = windows.get(s[r], 0) + 1
                if windows[s[r]] == need[s[r]]:
                    valid += 1
            r += 1
            # print(l, r)
            # 判断收缩
            while valid == len(need.keys()):
                if r - l < length:
                    start = l
                    length = r - l 

                if s[l] in need:
                    if windows[s[l]] == need[s[l]]:
                        valid -= 1
                    windows[s[l]] = windows[s[l]] - 1
                l += 1
        if length == float('inf'):
            return ""
        else:
            return s[start:start+length]



# @lc code=end
s = Solution()
res = s.minWindow("ADOBECODEBANC", 'ABC')
print(res)