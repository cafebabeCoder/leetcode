#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        track = []
        # flag = {}
        self.back_track(track, 0)
        return self.res
    
    def back_track(self, track, flag):
        self.res.append(track[:])
        if flag >= len(self.nums):
            return
        for i in range(flag, len(self.nums),1):
            track.append(self.nums[i])
            self.back_track(track, i + 1)
            track.pop()



# @lc code=end

