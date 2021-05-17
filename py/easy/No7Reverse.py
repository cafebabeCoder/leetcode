class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        # t = 1
        if x >=0:
            posNeg = 1
        else :
            posNeg = -1
        x = abs(x)
        while x > 0:
            res = res * 10 + (x % 10)
            # t *= 10
            x = int(x / 10)
        if -2**31 < res * posNeg < 2**31 - 1:
            return res * posNeg
        else:
            return 0

Solution().reverse(120)