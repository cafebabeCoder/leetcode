class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_seq = dict()
        for i in range(len(nums)):
            max_seq[i] = 1
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] >= nums[i]:
                    continue
                else:
                    max_seq[i] = max(max_seq[i], max_seq[j] + 1)
        res = 0
        for i in max_seq.values():
            res = max(res, i)
        return res

print(Solution().findNumberOfLIS([1]))