# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    preSum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur = root
        if root is None:
            return 0
        if cur.right is not None:
            self.convertBST(cur.right)
        cur.val = cur.val + self.preSum
        self.preSum = cur.val
        if cur.left is not  None:
            self.convertBST(cur.left)
        return root

a = TreeNode(2)
b = TreeNode(5)
c = TreeNode(13)
b.left = a
b.right = c
t = Solution().convertBST(b)
print(t.val, t.left.val, t.right.val)