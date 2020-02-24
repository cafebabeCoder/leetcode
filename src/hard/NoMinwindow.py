import sys
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        windows = dict()
        needle = dict()
        left = 0
        right = 0
        for c in t:
            if c in needle:
                needle[c] += 1
            else:
                needle[c] = 1
        match = 0
        max_len = sys.maxsize
        min_str = s
        while right < len(s):
            c = s[right]
            if c in needle:
                if c in windows:
                    windows[c] += 1
                else:
                    windows[c] = 1
                if windows[c] == needle[c]:
                    match += 1
            right += 1
            while match == len(needle):
                if len(s[left:right]) < max_len:
                    max_len = len(s[left:right])
                    min_str = s[left:right]
                c = s[left]
                if c in windows:
                    windows[c] -= 1
                    if windows[c] < needle[c]:
                        match -= 1
                left += 1
        if max_len == sys.maxsize:
            return ""
        else:
            return min_str


print(Solution().minWindow("ADOBECODEBANC", "ABC"))