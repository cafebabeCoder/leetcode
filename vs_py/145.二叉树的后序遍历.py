#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res =[]
        if not root:
            return res
        node = root
        stack.append(root)
        while node or stack:
            while node.left:
                node = node.left
                stack.append(node)
            node = stack.pop()
            if not node.right:
                res.append(node.val)
                node=None
            else:
                node = node.right
        return res

# @lc code=end


s = Solution()
s.postorderTraversal()