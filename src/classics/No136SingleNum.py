class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        for k in nums:
            n = n ^ k
        return n

Solution().singleNumber([1,2, 2])