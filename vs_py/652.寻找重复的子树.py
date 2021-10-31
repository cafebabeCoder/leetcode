#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.mem = {}
        self.roots = []
        self.find(root)
        return self.roots

    def find(self, root):
        if root is None:
            return "#"
        left = self.find(root.left)
        right = self.find(root.right)
        seris = left + ',' + right +','+ str(root.val)
        self.mem[seris] = self.mem.get(seris, 0) +1
        if self.mem[seris] == 2:
            self.roots.append(root)

        return seris
        
        
# @lc code=end

