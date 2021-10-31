#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                tmp = int(num1[i]) * int(num2[j])
                s = tmp + res[i+j+1]
                res[i+j+1]=int(s%10)
                res[i+j]=res[i+j]+int(s/10)

        i=0
        while i < len(num1) + len(num2) and res[i]==0:
            i+=1
        if i == len(num1) + len(num2):
            return "0"
        return "".join([str(k) for k in res[i:]])


# @lc code=end

s=Solution()
print(s.multiply("0", '0'))

