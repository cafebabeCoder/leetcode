#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.k = k
        self.n = n
        self.back_track(1, [])
        return self.res
    
    def back_track(self, idx, track):
        if len(track) == self.k:
            self.res.append(track[:])
        for i in range(idx, self.n+1, 1):
            track.append(i)
            self.back_track(i+1, track)
            track.pop()


        





# @lc code=end

