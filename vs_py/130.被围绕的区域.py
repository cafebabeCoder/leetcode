#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

from typing import List
# @lc code=start
# from typing import Sized


class UF():

    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.count = n

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        if self.size[rootp] > self.size[rootq]:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        self.count -= 1
        
    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p


    def connect(self, p, q) -> bool:
        rootp = self.find(p)
        rootq = self.find(q)
        return rootp == rootq

    def count(self) -> int:
        return self.count


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        uf = UF(m*n + 1)
        dummy = m * n

        for i in range(m):
            if board[i][0] == 'O':
                uf.union(i*n, dummy)
            if board[i][n-1] == 'O':
                uf.union(i*n+n-1, dummy)
        
        for j in range(n):
            if board[0][j] == 'O':
                uf.union(j, dummy)
            if board[m-1][j] == 'O':
                uf.union((m-1) * n + j, dummy)
        
        d = [[1,0], [-1,0], [0,-1], [0,1]]
        for i in range(1, m-1, 1):
            for j in range(1, n-1, 1):
                if board[i][j] == 'O':
                    for t in range(4):
                        x = i+d[t][0]
                        y = j+d[t][1]
                        if board[x][y] == 'O':
                            uf.union(i*n + j, x*n+y)
        
        for i in range(1, m-1, 1):
            for j in range(1, n-1, 1):
                if (not uf.connect(i*n + j, dummy)):
                    board[i][j] = 'X'
        return board



# @lc code=end

s = Solution()
print(s.solve([["O","O","O"],["O","O","O"],["O","O","O"]]))
