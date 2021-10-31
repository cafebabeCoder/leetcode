#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.subIsValid(root, None, None)
        
    def subIsValid(self, root, maxs, mins): # 左边最大值  右边最小值
        if root is None:
            return True
        if maxs is not None and root.val >= maxs.val:
            return False
        if mins is not None and root.val <= mins.val:
            return False
        return self.subIsValid(root.left, root, mins) and self.subIsValid(root.right, maxs, root)




# @lc code=end

