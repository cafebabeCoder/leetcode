#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
# badcase & 初始值:  初始dp[i] = 1
# 状态: 已知dp[0..i-1]的结果， 求dp[i]
# 选择： 对小于nums[i]的数，找到最小子序列+1
# dp[i] 以num[i]为结尾的最长递增子序列的长度
#

# @lc code=start
class Solution:
    # 二分查找
    def lengthOfLIS(self, nums: List[int]) -> int:
        top = []

        for i in range(0, len(nums), 1):
            left = 0
            right = len(top) - 1
            target = nums[i]
            while left <= right:
                mid = left + int((right - left) / 2)
                if top[mid] < target:
                    left = mid + 1
                elif top[mid] > target:
                    right = mid - 1
                else:
                    right = mid - 1  # 收缩右边界
            
            if left >= len(top):
                top.append(nums[i])
            else:
                top[left] = nums[i]
        
        return len(top)


    # 动归写法
    def lengthOfLIS2(self, nums: List[int]) -> int:
        # dp[i] 以num[i]为结尾的最长递增子序列的长度
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums), 1):
            for j in range(0, i, 1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        m = 1
        for val in dp:
            m = max(val, m)
        return m

# @lc code=end

