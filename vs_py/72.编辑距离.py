#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
# badcase: i走完s1， 或者j走完s2.
# 状态： s1, s2剩余子串
# 选择： 如果 s1[i] == s2[j]: skip, i+1,j+1;  否则：（插入、删除、替换）三选一
# 【hint】
# 两个字符串动归问题，一般用2个指针 i, j 分别指向两个字符串的最后，然后一步步往前走。
# 递归会超时， 加一个备忘录
# 动归的写法，s1 s2都需要加一个空串（对应badcase)。
#

# @lc code=start
class Solution:
    # 动归写法
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        dp = [[9999 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(len1+1):
            dp[i][0] = i 
        for j in range(len2+1):
            dp[0][j] = j
        dp[0][0] =0
        for i in range(1, len1 +1,1):
            for j in range(1, len2 + 1, 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j-1] + 1, dp[i-1][j] + 1)
        return dp[len1][len2]

        
    # 递归写法    
    def minDistance2(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i ==-1:
                return j+1
            elif j == -1:
                return  i+1
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i-1, j-1)
                return memo[(i, j)] 
            else:
                cur_min = min(dp(i, j-1) + 1, # 插入
                dp(i-1, j-1)+1,  # 替换
                dp(i-1, j) +1 )  # 删除

                memo[(i, j)] = cur_min
                return memo[(i, j)]
            
        return dp(len(word1) -1, len(word2)-1)



# @lc code=end