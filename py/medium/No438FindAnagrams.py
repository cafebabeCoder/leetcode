class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left = 0
        right = 0
        window = dict()
        needle = dict()
        res = []
        for c in p:
            if c in needle:
                needle[c] += 1
            else:
                needle[c] = 1
        match = 0
        while right < len(s):
            c = s[right]
            if c in needle:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if window[c] == needle[c]:
                    match += 1
            right += 1

            while match == len(needle):
                if right - left ==len(p):
                    res.append(left)
                c = s[left]
                if c in needle:
                    window[c] -= 1
                    if window[c] < needle[c]:
                        match -= 1
                left += 1

        return res

print(Solution().findAnagrams("aaaabaaaaa","aaaa"))


