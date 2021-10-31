#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {} 
        for i in range(len(nums)):
            nums_dict[nums[i]] = i 
        for i in range(len(nums)):
            other = target - nums[i] 
            if other in nums_dict and nums_dict[other]!=i:
                return [i, nums_dict[other]]
        return [-1, -1]


# @lc code=end

