#
# @lc app=leetcode.cn id=1860 lang=python3
#
# [1860] 增长的内存泄露
#
# @lc code=start
class Solution:
    def memLeak(self, memory1: int, memory2: int):
        if memory1 ==0 and memory2 ==0:
            return [1, 0, 0] 
        t = 1 
        while(memory1 >= t or memory2 >= t):
            if(memory1 >= memory2):
                memory1 = memory1 - t
                t += 1 
            else:
                memory2 = memory2 - t
                t += 1
            # print(t, memory1, memory2)
        return [t, memory1, memory2]



# @lc code=end
s= Solution()
print(s.memLeak(2, 2))

