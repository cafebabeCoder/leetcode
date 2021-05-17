class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        max_seq = dict()
        for i in range(len(text1)):
            max_seq[(i, -1)] = 0
        for j in range(len(text2)):
            max_seq[(-1, j)] = 0
        max_seq[(-1, -1)] = 0
        res = 0
        for i in range(0, len(text1)):
            for j in range(0, len(text2)):
                if text1[i] == text2[j]:
                    max_seq[(i, j)] = max_seq[(i-1, j-1)] + 1
                else:
                    max_seq[(i, j)] = max(max_seq[(i-1, j)], max_seq[i, j-1])
                if res < max_seq[(i, j)]:
                    res = max_seq[(i, j)]
        return res

print(Solution().longestCommonSubsequence("abc", "abc"))
