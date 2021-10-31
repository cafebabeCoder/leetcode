#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        i = len(nums) - 1
        j = i-1
        while i>=0 and j >= 0 and nums[j] - nums[i]>=0:
            i = i-1
            j = j-1
        idx = len(nums) -1
        while idx>=0 and nums[idx] <= nums[j]:
            idx -=1
        if j != -1:
            swap(j, idx)
        nums[j+1:] = list(reversed(nums[j+1:]))

        print(i, j)
        print(nums)

# @lc code=end

s = Solution()
s.nextPermutation([5,1,1])
                # [4,2,0,3,2,2,0]
                # 1, 4, 3, 2, 0  -> 2 4 3 1 0
