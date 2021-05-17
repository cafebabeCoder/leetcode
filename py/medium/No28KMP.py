class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def kmp(patten):
            knext = []
            knext.insert(0, -1)
            i = 0
            j = -1
            while i < len(patten):
                if j == -1 or patten[i] == patten[j]:
                    j += 1
                    i += 1
                    knext.insert(i, j)
                else:
                    j = knext[j]
            # print(knext)
            return knext

        def kmpHigh(patten):
            knext = []
            knext.insert(0, -1)
            i = 0
            j = -1
            while i < len(patten) - 1:
                if j == -1 or patten[i] == patten[j]:
                    j += 1
                    i += 1
                    # print(i, j)
                    if patten[i] != patten[j]:
                        knext.insert(i, j)
                    else:
                        knext.insert(i, knext[j])
                else:
                    j = knext[j]
            print(knext)
            return knext

        knext = kmpHigh(needle)
        knext = kmp(needle)
        # for i, c in enumerate(haystack):
        if needle is None or len(needle) == 0:
            return 0
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:  #边界判断同KMP生成
                i += 1
                j += 1
            else:
                j = knext[j]
            # print(i, j)
            if j == len(needle):
                return i - j
        return -1

print(Solution().strStr("ABABD", "ABCDABD"))