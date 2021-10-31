#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List
# @lc code=start
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        track = []
        self.flag = {} 
        self.back_track(track)
        return self.res
    
    def back_track(self, track):
        if len(track) == len(self.nums):
            self.res.append(track[:])
        
        for i in self.nums:
            if self.flag.get(i, True):
                track.append(i)
                self.flag[i] = False
                self.back_track(track)
                track.pop()
                self.flag[i] = True


        


# @lc code=end
s = Solution()
r = s.permute([0, 1])
print(r)
