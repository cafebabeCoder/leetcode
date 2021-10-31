#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        lens =len(s)
        left = -lens
        right = 0
        res = [lens for _ in range(lens)]

        i = 0
        while i < len(s):
            while right< lens and s[right] != 'e':
                right +=1
            while i< lens and i <= right:
                if right ==lens and res[right-1]!='e':
                    res[i] = i-left
                else:
                    res[i] = min(i - left, right - i)
                i +=1
            left = right
            right +=1
        
        return res


# @lc code=end

s = Solution()
s.shortestToChar("aaab", 'b')
