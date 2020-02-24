class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charMap = dict()
        for c in s:
            if c in charMap:
                charMap[c] = charMap[c] + 1
            else:
                charMap[c] = 1
        for c in t:
            # print(c, charMap)
            if c in charMap:
                charMap[c] = charMap[c] - 1
                if charMap[c] == 0:
                    charMap.pop(c)
            else:
                return False
        if len(charMap) == 0:
            return True


print(Solution().isAnagram("anagram", "nagaram"))