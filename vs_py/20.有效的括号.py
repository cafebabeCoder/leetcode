#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_right_dict = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if  i in ['(', '[', '{']:
                stack.append(i)
            else:
                if len(stack) <= 0:
                    return False
                if stack[-1] == left_right_dict[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
# @lc code=end

