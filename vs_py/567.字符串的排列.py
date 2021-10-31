#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        windows = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1
        
        l = 0
        r = 0
        valid = 0
        while r < len(s2):
            c = s2[r]
            if c in need.keys():
                windows[c] = windows.get(c, 0) + 1
                if windows[c] == need[c]:
                    valid += 1
            r += 1
            # print(l, r)
            while r -l >= len(s1):
                if valid == len(need.keys()):
                    return True
                c = s2[l]
                if c in need:
                    if windows[c] == need[c]:
                        valid -= 1
                    windows[c] = windows[c] - 1


                l += 1

        # print(valid)
        if valid == len(need.keys()):
            return True
        return False


# @lc code=end

s = Solution()
print(s.checkInclusion('a', 'ab'))
