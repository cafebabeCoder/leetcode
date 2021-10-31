#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from typing import List
# @lc code=start
class Solution:
    res = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = ['.'*n ] * n   # 初始化board
        self.back_track(0, board)  
        return self.res

    def back_track(self, n, board):  # 每一行遍历
        # 终止条件
        sz = len(board)
        if  n== sz:
            self.res.append(board[:])
            return
        
        for j in range(sz):   #放每一列
            if self.valid(n, j, board):
                tmp = board[n]   # 选择
                board[n] = tmp[:j]+ 'Q' + tmp[j+1:]
                self.back_track(n+1, board)   # 下一步
                board[n]=tmp   # 回溯
            else:
                continue
    
    def valid(self, i, j, board):
        sz = len(board)
        # 检查列
        for k in range(sz):
            if board[k][j]=='Q':
                return False

        # 检查 斜线
        for p, q in zip(range(i-1, -1, -1), range(j+1, sz, 1)):
            if board[p][q] == 'Q':
                return False
    
        for p, q in zip(range(i-1, -1, -1), range(j-1, -1, -1)):
            if  board[p][q]=='Q':
                return False
    
        return True

# @lc code=end
s = Solution()
res = s.solveNQueens(4)
print("\n\n".join(["\n".join(i) for i in res]))
# print("\n".join(res))
