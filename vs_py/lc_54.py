#
# @lc code=start
# Definition for singly-linked list.
# Definition for a binary tree node.
#[5,3,6,2,4,null,null,1]
#3

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return 0

        self.th = 0
        self.k = k
        s = self.tree(root)
        print(s, self.th)
        return self.th

    def tree(self, root):

        if root.right is not None:
            return self.tree(root.right)
        self.th += 1
        if self.th == self.k:
            self.res = root.val
            return
        if root.left is not None:
            return self.tree(root.left)

node5 = TreeNode(5)
node3 = TreeNode(3)
node6 = TreeNode(6)
node2 = TreeNode(2)
node4 = TreeNode(4)
node1 = TreeNode(1)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)


node5.right = node7
node3.left = node2
node3.right = node4
node2.left = node1
node7.right = node9
node9.left = node8
node7.left = node6
s = Solution()
re = s.kthLargest(node5, 5)
print(re)