#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        l = []
        self.back_track(n, n, l)
        return self.res
    
    def back_track(self, left, right, l):
        if left ==0 and right == 0:
            self.res.append("".join(l))
        if left > right:
            return
        if left < 0 or right < 0:
            return
        #z 尝试放左括号
        l.append('(')
        self.back_track(left -1, right, l[:])
        l.pop()

        # 尝试放右括号
        l.append(')')
        self.back_track(left, right-1, l[:])
        l.pop()

# @lc code=end

