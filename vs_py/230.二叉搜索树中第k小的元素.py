#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return 0
        self.res= 0
        self.c =k 
        self.subKsmall(root)
        return self.res

    def subKsmall(self, root):
        if root.left is not None:
            self.subKsmall(root.left)
        self.c -= 1
        print(self.c)
        if self.c == 0:
            self.res = root.val
            return
        if root.right is not None:
            self.subKsmall(root.right)





# @lc code=end

