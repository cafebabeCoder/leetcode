class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        stack = []
        for a in A:
            if a%2 == 0:
                res.append(a)
            else:
                stack.append(a)
        return res + stack

print(Solution().sortArrayByParity([3,1,2,4]))
