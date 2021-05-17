# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        it = head.next
        # head.next = None
        while(it.next is not None):
            # print("cur:" ,cur.val , cur.next.val)
            next = it.next
            it.next = cur
            cur = it
            it = next
            print(cur.val , cur.next.val)
        it.next = cur
        head.next = None
        return it

l1=ListNode(1)
l2=ListNode(2)
l1.next =l2
l3=ListNode(3)
l2.next=l3
l4=ListNode(4)
l3.next=l4

n=Solution().reverseList(l1)
while(n.next!=None):
    print(n.next.val)
    n = n.next
print("----")