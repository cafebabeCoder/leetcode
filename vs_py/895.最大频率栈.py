#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

# @lc code=start
class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.fv = {} # {f, [vals]}
        self.vf = {}  

    def push(self, val: int) -> None:
        f = self.vf.get(val, 0) + 1
        self.vf[val] = f

        if f not in self.fv:
            self.fv[f] = [val]
        else:
            self.fv[f].insert(0, val)
            
        if self.max_freq < f:
            self.max_freq = f

    def pop(self) -> int:

        vals = self.fv[self.max_freq]
        res = vals.pop(0)
        self.vf[res] = self.vf[res] - 1
        if len(vals) == 0:
            self.max_freq = self.max_freq - 1
        return res



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

