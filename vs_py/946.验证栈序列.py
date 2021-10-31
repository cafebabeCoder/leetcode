#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

# @lc code=start
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # instack = []
        outstack = []
        j = 0 # pushed
        i = 0 # popped
        # pushed 可以达到边界， 这时只弹出
        while i  < len(popped) and j <= len(pushed):
            # 先判断是否弹出, 因为上一次可能是弹出
            if len(outstack) > 0 and outstack[-1] == popped[i]:
                i = i+1
                outstack.pop()
            # 相等就直接跳过 
            elif j < len(pushed) and popped[i] == pushed[j]:
                i = i +1
                j = j +1
            # 压栈
            elif j < len(pushed):
                outstack.append(pushed[j])
                j = j+1
            # 都不满足，且不能压栈
            else:
                return False

        if len(outstack) ==0 :# and i == len(popped):
            return True
        else:
            return False

# @lc code=end

