from typing import List
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        self.x = [-1, 1, 0, 0]
        self.y = [0, 0, -1, 1]
        self.maze = maze
        self.res = False
        self.n, self.m = len(maze[0]), len(maze)
        self.visit = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        self.visit[start[0]][start[1]] = 1
        self.back_track(start[0], start[1], destination[0], destination[1])
        return self.res

    def back_track(self, srow, scol, drow, dcol):
        print(srow, scol)
        if srow == drow and scol == dcol:
            self.res = True
            return
        for i in range(4):
            p =srow+self.x[i]
            q = scol+self.y[i]
            while p>=0 and p<self.m and q>=0 and q<self.n and self.maze[p][q]!=1:
                p += self.x[i]
                q += self.y[i]
            if not self.visit[p-self.x[i]][q-self.y[i]]:
                self.visit[p-self.x[i]][q-self.y[i]] = 1
                self.back_track(p-self.x[i], q-self.y[i], drow, dcol)
                self.visit[p-self.x[i]][q-self.y[i]] = 0


maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
s = [0,4]
d = [1,2]
# maze = [[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]]
# s =[0,0]
# d = [8,6]
so = Solution()
print(so.hasPath(maze, s, d))
