#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        while fast is not None and n > 0:
            fast = fast.next
            n -= 1
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next 
        if fast is None:
            return head.next
        else:
           slow.next = slow.next.next
        return head

# @lc code=end

