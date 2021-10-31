#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        mid = int((l+r)/2)
        while(l < r):
            if nums[mid] == target:
                return mid
            elif(nums[mid] < target):
                l = mid+1
                mid = int((l + r)/2)
            elif( nums[mid] > target):
                r = mid-1
                mid = int((r + l)/ 2)
        
        if nums[mid] == target:
            return mid
        else:
            return -1

# @lc code=end

