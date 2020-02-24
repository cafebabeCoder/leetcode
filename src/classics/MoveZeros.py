class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0 # long
        j = 0 # short
        while i < len(nums):
            while i < len(nums) and nums[i] == 0:
                i += 1
            if j < len(nums) and i < len(nums):
                nums[j] = nums[i]
                j += 1
                i += 1
        while j < len(nums):
            nums[j] = 0
            j += 1
        print(nums)

Solution().moveZeroes([0])