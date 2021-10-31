#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

class Node:
    next=None
    pre=None
    def __init__(self, key=None, val=None) -> None:
        self.val=val
        self.key=key

# @lc code=start
class LRUCache:
    capacity = 0
    mmap = {}

    def __init__(self, capacity: int): 
        self.head = Node() 
        self.tail = Node() 
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.mmap:
            makeRecently(self.mmap[key])
            return self.mmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mmap:
            update(self.mmap[key], value)
            self.makeRecently(self.mmap[key])
        else:
            if len(self.mmap) < self.capacity:
                addRecently(key, value)
            else:
                removeLast()
                addRecently(key, value)
    
    def makeRecently(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = self.tail.pre
        self.tail.pre.next = node
        self.tail.pre = node
    
    def update(self, node, val):
        node.val = val
    def addRecently(self, key, value):
        node = Node(key, value)
        self.mmap[key]
        node.
    
    def addFirst



        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

