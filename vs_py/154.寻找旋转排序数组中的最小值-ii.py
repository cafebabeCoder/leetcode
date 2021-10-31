#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
# hint: 考虑 O(log)
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i < j and nums[i] >= nums[j]:
            m = int((j- i )/2) + i
            # 通过三头都相等，无法移动坐标
            #  [2, 2, 2, 0, 2] 或者 [2, 0, 2, 2, 2] 
            if nums[m] == nums[i] and nums[m] == nums[j]:
                return self.order(nums, i, j)
            # m > i ->  最小数在i之后
            # m == i -> j!=i 所以 j<i, 最小数还是在i之后。
            if nums[m] >= nums[i]:
                i = m + 1
            # m < i  -> 最小数在m(包括m之前) 
            elif nums[m] < nums[i]:
                j = m
        return nums[i]
                
    def order(self, nums, low, high):
        mins = nums[low]
        for k in nums[low:high+1]:
            mins = min(mins, k)
        return mins


# @lc code=end
s = Solution()
print(s.findMin([2,2,2,0,1]))