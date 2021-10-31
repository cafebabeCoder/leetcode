#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small, mid = None, None
        for i in nums:
            if small is None or i <= small:
                small = i
            elif mid is None or i <= mid:
                print(mid, i)
                mid = i
            else:
                if small is None and mid is not None and small != mid:
                    return True
            print(small, mid, i)

        return False


# @lc code=end

s = Solution()
s.increasingTriplet([1,5,0,4,1,3])
