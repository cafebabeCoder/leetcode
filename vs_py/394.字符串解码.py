#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# 输入：s = "3[a]2[bc]"
# 输入：s = "3[a2[c]]"
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        cur_s = [] 
        res = '' 
        mul = 0
        for i in range(len(s)):
            c = s[i]
            if c =='[':
                cur_s.append((res, mul))
                res = ''
                mul = 0
            elif c <='9' and c>='0':
                mul = mul*10 + int(s[i])
            elif c ==']':
                last_res, muls = cur_s.pop()
                res = last_res + muls * res 
            else:
                res += s[i]
            

        return res


# @lc code=end
s = Solution()
# res = s.decodeString("2[abc]3[cd]ef")
res = s.decodeString("3[a]2[bc]")
# res = s.decodeString("3[a]2[c2[bc]]")
print(res)

