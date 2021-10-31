#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
class Solution:
    # 递归写法
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l2 == None:
            return l1
        if l1 == None:
            return l2
        if l1.val < l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        return head
       

    # while循环写法
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = n = None
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            head = n = l2 
            l2 = l2.next
        elif l2 is None:
            head = n = l1
            l1 = l1.next
        else:
            if l1.val > l2.val:
                head = n = l2
                l2 = l2.next
            else:
                head = n = l1
                l1 = l1.next

        while l1!= None and l2 !=None:
            if l1.val < l2.val:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            n = n.next
        if l2!=None:
            n.next = l2
        if l1!=None:
            n.next = l1
        return head


# @lc code=end

