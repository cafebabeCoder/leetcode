#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        l = root
        r = root

        hl = 0
        hr = 0
        while l :
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        
        if hl == hr:
            return pow(2, hl) - 1
        
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        





# @lc code=end

