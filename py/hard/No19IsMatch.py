class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = dict()
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            # 终止条件
            if j == len(p):
                return i == len(s)
            first = i < len(s) and p[j] in {s[i], '.'}
            if j <= len(p) - 2 and p[j+1] == '*':
                bol = dp(i, j+2) or first and dp(i+1, j)
            else:
                bol = first and dp(i+1, j+1)
            memo[(i, j)] = bol
            return bol
        return dp(0, 0)

print(Solution().isMatch("aab", "a*bc"))