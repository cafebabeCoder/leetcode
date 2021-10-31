#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        len1 = len(grid)
        len2 = len(grid[0])
        visit = [[0 for _ in range(len2)] for _ in range(len1)] #记录访问
        dicts = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        que = []  #访问队列
        for i in range(len1):
            for j in range(len2):
                if visit[i][j] == 1:
                    continue
                if grid[i][j] == '0':
                    visit[i][j] = 1 
                    continue
                if visit[i][j] == 0:
                    que.append((i, j))
                    visit[i][j] = 1
                    while len(que) > 0:
                        m, n = que.pop()
                        for d in dicts:
                            a = m + d[0]
                            b = n + d[1]
                            if a<len1 and b < len2 and a>=0 and b >=0 and grid[a][b] == '1':
                                if visit[a][b] == 0:
                                    que.append((a, b))
                                    visit[a][b] = 1
                    # print(i, j, grid[i][j])
                    count +=1
        return count


# @lc code=end

