#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

from typing import List
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        p = 0
        q = 0 
        sm = 0
        m = len(matrix)
        sn = 0
        n = len(matrix[0])
        res =[]
        while sm <= m  and sn <= n:
            for i, j in dirs:
                while sm <= p < m  and sn<= q < n:
                    # print(p, q, matrix[p][q])
                    res.append(matrix[p][q])
                    p = i+p
                    q = j+q
                if i == 0 and j == 1:
                    sm +=1
                    q -= 1
                    p += 1
                elif i == 1 and j ==0:
                    n -=1
                    p -= 1
                    q -= 1
                elif i == 0 and j == -1:
                    m -= 1
                    q += 1
                    p -= 1
                else:
                    sn += 1
                    p += 1
                    q += 1
        return res

# @lc code=end
s = Solution()
s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])

