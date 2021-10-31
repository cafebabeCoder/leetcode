#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
# 先排序， 再求递增子序列。
# 排序： 按宽升序，相同宽 长降序。
#
from typing import List
# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 排序
        order_env = sorted(envelopes, key=lambda s:(s[0], -s[1]))
        order_env_last = [k for (_, k) in order_env]

        # 最长递增子序列
        dp = [1 for _ in range(len(order_env_last))]
        for i in range(len(order_env_last)):
            for j in range(i):
                if order_env_last[i] > order_env_last[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

# @lc code=end

s = Solution()
s.maxEnvelopes([[30,50],[12,2],[3,4],[12,15]])
