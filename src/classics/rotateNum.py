class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        self.reverse(nums, 0, length - 1 - k)
        self.reverse(nums, length - k , length - 1)
        self.reverse(nums, 0, length - 1)
        # print(nums)

    def reverse(self, nums, i, j):
        while(i < j):
            k = nums[i]
            nums[i] = nums[j]
            nums[j] = k
            i = i + 1
            j = j - 1

Solution().rotate([1,2,3,4,5,6,7], 3)