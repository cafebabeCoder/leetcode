#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
# 同 [583]
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        mem = [[0 for _ in range(len2+1)] for _ in range(len1 + 1)]

        for i in range(1, len1+1, 1):
            for j in range(1, len2 + 1, ):
                if text1[i-1] == text2[j-1]:
                    mem[i][j] = mem[i-1][j-1] + 1
                else:
                    mem[i][j] = max(mem[i-1][j], mem[i][j-1])
        return mem[i][j]


# @lc code=end

