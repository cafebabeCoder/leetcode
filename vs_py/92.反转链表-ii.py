#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        node = head
        if left == 1:
            return self.reverseTopk(head, right)
        self.succor = None
        # head.next = self.reverseBetween(head.next, left-1, right-1)
        # return head

        pre = node
        while left>1 and node is not None:
            left -= 1
            right -=1
            pre = node
            node = node.next
        newhead = self.reverseTopk(node, right-left +1)
        pre.next = newhead
        return head
    
    def reverseTopk(self, head, k):
        if k==1:
            self.succor = head.next
            return head
        newhead = self.reverseTopk(head.next, k-1)
        head.next.next = head 
        head.next = self.succor 
        return newhead
        

# @lc code=end
head = ListNode(1)
node = head
for i in range(2, 6, 1):
    n = ListNode(i)
    node.next = n
    node = n

node = head
while(node is not None):
    print(node.val)
    node = node.next

print('-----')
s = Solution()
node = s.reverseBetween(head, 1, 2)
while(node is not None): 
    print(node.val)
    node = node.next
   
