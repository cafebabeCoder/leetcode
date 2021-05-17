class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        second = 0
        first = 0
        while first < len(nums):
            while(first < len(nums) and nums[first] == nums[second]):
                print(first, second)
                first += 1
            if first < len(nums) and second < len(nums):
                second += 1
                nums[second] = nums[first]
                first += 1
        return second + 1

Solution().removeDuplicates([1,1,2])