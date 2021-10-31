#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
# [4,2,0,3,2,5]

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        if len(height) < 1:
            return 0
        # left_max[i] i左侧最高
        left_max = [0]
        for i in range(0, len(height)-1, 1):
            left_max.append(max(left_max[-1], height[i]))
        # right_max[i] i 右侧最高
        right_max = [0]
        for i in range(len(height)-1, 0, -1): 
            right_max.insert(0, max(right_max[0], height[i]))
        for i in range(0, len(height), 1):
            res += max(0, min(left_max[i], right_max[i]) - height[i])
        return res


# @lc code=end

