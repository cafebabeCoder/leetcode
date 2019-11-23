#!/usr/bin/env python3

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorder(self, root, result):
        cur = root
        if cur is not None:
            result.append(cur.val)
            if cur.left is not None:
                self.preorder(cur.left, result)
            if cur.right is not None:
                self.preorder(cur.right,result)
        return result

a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(4)
b.left = a
b.right = c
result = []
Solution().preorder(b, result)
print(result)