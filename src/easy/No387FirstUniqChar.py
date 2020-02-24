class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letterSet = dict()
        for letter in s:
            if letter in letterSet:
                letterSet[letter] = letterSet[letter] + 1
            else:
                letterSet[letter] = 1
        i = -1
        index = -1
        for letter in s:
            i = i + 1
            if letterSet[letter] == 1:
                index = i
                return index
        return index

print(Solution().firstUniqChar("loveleetcode"))