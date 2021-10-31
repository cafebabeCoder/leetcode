#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left < len(nums) and right >= 0 and left < right:
            mid = int((right - left)/2 +left)
            if nums[mid] == target:
                return mid 
            if nums[mid] >= nums[left]:
                if nums[mid] > target and nums[left]<=target:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        mid = int((right - left)/2 +left)
        if mid < len(nums) and mid >=0 and nums[mid] == target:
            return mid 
        else:
            return -1

# @lc code=end

