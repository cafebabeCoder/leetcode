#!/usr/bin/env python3

import sys
from typing import List

print(sys.version)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j = j + 1
        print(nums)
        print(j)
        return j


solution = Solution()
solution.removeElement(nums=[1,3,0,2], val=3)