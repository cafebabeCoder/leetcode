class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ["0"]*(len(num1) + len(num2))
        for i in range(len(num2)-1, -1, -1):
            for j in range(len(num1)-1, -1, -1):
                s_i = int(num2[i])
                s_j = int(num1[j])
                bit_sum = s_i * s_j
                carry = int((bit_sum % 10 + int(res[i + j + 1])) / 10)
                res[i + j + 1] = str(bit_sum % 10 + int(res[i + j + 1]))[-1]
                bit_sum = int(bit_sum / 10)
                k = 1
                while carry > 0 or bit_sum != 0:
                    tmp_sum = bit_sum % 10 + int(res[i + j + 1 - k]) + carry
                    res[i + j + 1 - k] = str(tmp_sum)[-1]
                    carry = int(tmp_sum / 10)
                    bit_sum = int(bit_sum / 10)
                    k += 1
        while len(res) > 0 and res[0] == "0":
            res.pop(0)
        if len(res) == 0:
            return "0"
        else:
            return "".join(res)

print(Solution().multiply("0", "0"))