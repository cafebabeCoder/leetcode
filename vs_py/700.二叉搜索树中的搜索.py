#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        self.res = None
        self.search(root, val)
        return self.res
    
    def search(self, root, val):
        if root is not None and root.val == val:
            self.res = root
            return
        if root is None:
            return
        
        elif root.val > val:
            self.search(root.left, val)
        else:
            self.search(root.right, val)



# @lc code=end

