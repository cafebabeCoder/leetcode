#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        # c = 0
        while r < len(nums):
            if nums[r] == nums[l]:
                r += 1
            else:
                l += 1
                nums[l]=nums[r]
                r += 1
        # print(l)
        return l+1





# @lc code=end

