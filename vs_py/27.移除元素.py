#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l =0
        r = 0
        while r < len(nums):
            if nums[r] != val: 
                nums[l] = nums[r]
                # print(nums)
                l += 1
            r += 1
        return l
# @lc code=end

