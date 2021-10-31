#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def track_back():
            if len(buff) == len(nums):
                res.append(buff[:])
                return
            for i in range(len(snums)):
                if visit.get(i, False) or (i>0 and not visit[i-1] and snums[i]==snums[i-1]):
                    continue
                visit[i] = True
                buff.append(snums[i])
                track_back()
                buff.pop()
                visit[i] = False
    
        buff=[]
        res = []
        visit={}
        snums = sorted(nums)
        track_back()
        return res
# @lc code=end
s = Solution()
res = s.permuteUnique([1,1, 2])
print(res)