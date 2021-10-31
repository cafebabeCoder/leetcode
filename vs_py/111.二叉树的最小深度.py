#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        dep = 0
        if root is None:
            return 0
        dep = self.bfs(root)
        return dep

    def bfs(self, node):
        if node.left is None and node.right is None:
            return 1
        elif node.right is None:
            return 1 + self.bfs(node.left)
        elif node.left is None:
            return 1 + self.bfs(node.right)
        else:
            return min(1 + self.bfs(node.left), 1 + self.bfs(node.right))


# @lc code=end
