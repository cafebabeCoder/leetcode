#
# @lc app=leetcode.cn id=1859 lang=python3
#
# [1859] 将句子排序
#
import re
# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        tokens = s.split(" ")
        pattern = re.compile(r'\d+')
        id_sen_map = {}
        for token in tokens:
            idx = re.findall(pattern, token)[-1]
            sent = token.replace(idx, "")
            # print(idx)
            id_sen_map[int(idx)] = sent
        
        print(id_sen_map)
        res = []
        for i in range(1, len(tokens)+1, 1):
            res.append(id_sen_map[i])
        return ' '.join(res)



# @lc code=end

s = Solution()
res = s.sortSentence("is2 sentence4 This1 a3")
print(res)
