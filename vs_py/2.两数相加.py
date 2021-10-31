#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        prenode = ListNode(0)
        node = prenode
        while l1 is not None and l2 is not None:
            v = l1.val + l2.val +flag
            flag = int(v/10)
            node.next = ListNode(int(v%10))
            node = node.next
            l1 = l1.next
            l2 = l2.next
            # print(prenode)
        
        cur = None
        if l2 is not None:
            cur = l2
        elif l1 is not None:
            cur = l1
        while cur is not None:
            v = cur.val + flag
            flag = int(v/10)
            node.next = ListNode(int(v%10))
            node = node.next
            cur = cur.next
        if flag == 1:
            node.next = ListNode(1)

        return prenode.next
        



# @lc code=end

