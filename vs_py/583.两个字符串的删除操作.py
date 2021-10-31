#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
# 同 [1143]
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        mem = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(1, len1+1, 1):
            for j in range(1, len2+1, 1):
                if word1[i-1] == word2[j-1]:
                    mem[i][j] = mem[i-1][j-1]+1
                else:
                    mem[i][j] = max(mem[i-1][j], mem[i][j-1])
        return len1 + len2 - 2 * mem[i][j]


# @lc code=end

