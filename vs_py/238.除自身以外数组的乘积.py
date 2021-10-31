#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
from typing import List

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left=1
        right=1
        res = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            res[i]*=left
            left*=nums[i]
            
            res[n-1-i]*=right
            right*=nums[n-1-i]
        
        return res
# @lc code=end

s = Solution()
s.productExceptSelf([1, 2, 3, 4])
