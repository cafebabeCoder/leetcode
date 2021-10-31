#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        n1 = headA
        n2 = headB
        while n1 != n2:
            if n1 == None:
                n1 = headB 
            else:
                n1 = n1.next
            if n2 == None:
                n2 = headA
            else:
                n2 = n2.next
        return n1
        
# @lc code=end
#[4, 1, 8, 4, 5] 
#[5, 0, 1, 8, 4, 5]


a = [1,8,4,5]
b = [0,1,8,4,5]
headA =node= ListNode(4)
for i in a:
    n = ListNode(i)
    node.next = n
    node = n
headB =node= ListNode(5)
for j in b:
    n = ListNode(j)
    node.next = n
    node = n

s = Solution()
n1 = s.getIntersectionNode(headA, headB)
print(n1)

