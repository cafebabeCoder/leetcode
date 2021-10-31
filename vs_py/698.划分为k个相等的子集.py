#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
from typing import List
# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        nums.sort()
        if nums[-1]>target:
            return False
        bucket = [target for _ in range(k)]
        return self.dfs(bucket, nums, k, len(nums)-1)

    def dfs(self, bucket, nums, k, cur):
        if cur < 0:
            return True
        for i in range(0, k):
            if bucket[i] == nums[i] or bucket[i]-nums[i]>=nums[0]:
                bucket[i] -= nums[i]
                if self.dfs(bucket, nums, k, cur-1):
                    return True
                
                bucket[i] += nums[i]
        
        return False
# @lc code=end
s = Solution()
nums = [1,2,2,2,2]
k = 3
s.canPartitionKSubsets(nums, k)

