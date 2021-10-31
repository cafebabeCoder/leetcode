#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        self.subConv(root, 0)
        return root

    def subConv(self, root, s):
        if root.right is not None:
            s = self.subConv(root.right, s)
        s += root.val
        root.val = s 
        if root.left is not None:
            s = self.subConv(root.left, s)
        return s


# @lc code=end

