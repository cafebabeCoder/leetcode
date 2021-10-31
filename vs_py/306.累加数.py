#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#

# @lc code=start
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return self.track_back(num, [])


    def track_back(self, num, numseq):
        if len(num) <=0 and len(numseq) > 2:
            return True
        if len(numseq) >=3 and numseq[-1]!= numseq[-2]+numseq[-3]:
            return False
        for i in range(len(num)):
            if num[0]=='0' and len(num)!=1:
                break
            numseq.append(int(num[:i+1]))
            if self.track_back(num[i+1:], numseq):
                return True
            numseq.pop()
        return False
# @lc code=end

s = Solution()
s.isAdditiveNumber("111")