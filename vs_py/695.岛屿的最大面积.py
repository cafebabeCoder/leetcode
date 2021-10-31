#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        # print(len(self.grid[0]))
        self.m = len(self.grid)
        self.n = len(self.grid[0])
        self.res = 0
        self.visit = {}
        self.cur_res = 0
        for i in range(self.m):
            for j in range(self.n):
                if not self.visit.get((i, j), False) and self.grid[i][j]==1:
                    self.cur_res = 0
                    self.dfs(i, j) 
                    self.res = max(self.res, self.cur_res)
        return self.res
                
    def dfs(self,i,j):
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        if not self.visit.get((i, j), False) and i>=0 and i<self.m and j>=0 and j<self.n and self.grid[i][j]==1: 
            self.visit[(i, j)] = True
            self.cur_res+=1
            for a, b in dir:
                if not self.visit.get((i+a, j+b), False):
                    self.dfs(i+a, j+b)



# @lc code=end

