#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

from typing import List
# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.trav(graph, 0, [])
        return self.res

    
    def trav(self, graph, s, path):
        path.append(s)
        if s == len(graph)-1:
            self.res.append(path[:])
            path.pop()
            return
        for n in graph[s]:
            self.trav(graph, n, path)
        
        path.pop()




# @lc code=end

