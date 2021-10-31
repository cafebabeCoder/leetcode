#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.inorder(root, 0)
        return root


    def inorder(self, root, s):
        if root == None:
            return s 
        
        s = self.inorder(root.right, s)
        s += root.val
        root.val = s
        s = self.inorder(root.left, s)
        return s
# @lc code=end

