class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s) == 0:
        #     return 1
        left = 0
        right = 0
        windows = dict()
        max_len = 0
        while right < len(s):
            c = s[right]
            right += 1
            if c not in windows:
                windows[c] = 1
            else:
                windows[c] += 1
            if len(windows) > max_len:
                max_len = len(windows)
            while windows[c] > 1:
                c_left = s[left]
                windows[c_left] -= 1
                if windows[c_left] == 0:
                    windows.pop(c_left)
                left += 1
        return max_len

print(Solution().lengthOfLongestSubstring(" "))