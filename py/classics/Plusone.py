class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        order = 1
        i = len(digits) - 1
        while i>=0 :
            num = digits[i]
            digits[i] = (num + order) % 10
            order = int((num + order) / 10)
            i -= 1
        if order == 1:
            digits.insert(0, 1)

Solution().plusOne([9,9,9])