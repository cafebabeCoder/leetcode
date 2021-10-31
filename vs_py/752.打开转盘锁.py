#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
from typing import List
# @lc code=start
class Solution:
    #  注意2点： 1. 拨动之前先判断
    #           2. python list 默认是栈， 需要pop(0) 才是队列 。  BFS是队列 

    def openLock(self, deadends: List[str], target: str) -> int:
        nodes = [] # 待访问队列
        root = '0000'   # 根节点
        nodes.append(root)   # 加入根节点
        visited = {root}  # 访问过队列， 避免重复访问
        step = 0  # 记录步数
        deadends_set = set(deadends) # 障碍

        while(len(nodes) > 0):
            # print(nodes)
            for _ in range(len(nodes)):
                cur = nodes.pop(0)
                if cur == target : # 判断结束
                    return step
                if cur in deadends_set:
                    continue
                for k in range(4):
                    new_up_num = self.up(cur, k)
                    new_down_num = self.down(cur, k)
                    # print("%s\t %s\n" %(new_up_num, new_down_num))
                    if new_down_num not in visited:
                        nodes.append(new_down_num)
                        visited.add(new_down_num)
                    if new_up_num not in visited:
                        nodes.append(new_up_num)
                        visited.add(new_up_num)
            step += 1
        return -1
    
    def up(self, s, i):
        char_i = int(s[i])
        if char_i ==9:
            return s[:i] + '0' + s[i+1:]
        else:
            return s[:i] + str(int(s[i]) + 1) + s[i+1:]
    
    def down(self, s, i):
        char_i = int(s[i])
        if char_i == 0:
            return s[:i] +  '9' + s[i+1:]
        else:
            return s[:i] + str(int(s[i]) - 1) + s[i+1:]

# @lc code=end
s = Solution()
res = s.openLock(["0000"], '8888')
print(res)


