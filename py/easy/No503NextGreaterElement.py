#!/usr/bin/env python3

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        nums = nums + nums
        nextElem = [-1 for _ in range(length)]
        stack = list()
        for index, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                nextElem[stack[-1]] = num
                stack.pop()
            if index < length:
                stack.append(index)
        return nextElem


print(Solution().nextGreaterElements([1,2,1]))