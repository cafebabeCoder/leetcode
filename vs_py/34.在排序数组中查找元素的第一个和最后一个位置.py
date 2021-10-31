#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.leftSearch(nums, target)
        last = self.rightSearch(nums, target)
        return [first, last]

    def leftSearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        while(l <= r):
            m = int(l + (r-l)/2)
            if nums[m] == target:
                r = m-1
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
        if l >= len(nums) or nums[l] != target:
            return -1
        return l

    def rightSearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        while(l <=r):
            m = int(l + (r - l) / 2)
            if nums[m] == target:
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m-1
        if r <0 or nums[r] != target:
            return -1 
        return r
    

# @lc code=end

