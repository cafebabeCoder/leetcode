#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
# 两种写法， DFS或者回溯
# 方向遍历的写法： dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 最难的部分在 【退出条件】

# @lc code=start
class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.res = [] 
        visited = {}
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def back_track(i, j):
            # 访问
            visited[(i, j)] = True
            self.res.append(board[i][j])
            # 退出条件判断
            if "".join(self.res)  == word:
                return True
            # 选择方向
            f = True 
            for p, q in dirs:
                if (i, j) not in visited and i < m and i >=0 and j < n and j >=0:
                    f = f | back_track(i+p, j+q)
                # 注意退出条件
                self.res.pop()
            return f

        for i in range(0, m):
            for j in range(0, n):
                back_track(i, j)


# @lc code=end


