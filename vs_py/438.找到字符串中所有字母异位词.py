#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        windows = {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        
        l = 0
        r = 0
        res = []
        valid = 0
        while r < len(s):
            c = s[r]
            if c in need:
                windows[c] = windows.get(c, 0) + 1
                if windows[c] == need[c]:
                    valid += 1
            r += 1 
            while r -l >= len(p):
                if valid == len(need.keys()):
                    res.append(l)
                c = s[l]
                if c in need:
                    if windows[c] == need[c]:
                        valid -= 1
                    windows[c] = windows[c] - 1
                l += 1
        return res



# @lc code=end

