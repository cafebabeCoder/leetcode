class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        num = 0
        for k in nums:
            if count == 0:
                num = k
                count += 1
            else:
                if num == k:
                    count += 1
                else:
                    count -= 1
        return num

Solution().majorityElement([2,2,1,1,1,2,2])