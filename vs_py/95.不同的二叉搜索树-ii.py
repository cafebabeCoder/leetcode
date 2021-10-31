#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 1:
            return [TreeNode(1)]
        nodes = self.gen(1, n)
        return nodes

    def gen(self, m, n):
        if m > n:
            return [None]
        nodes = []
        for i in range(m, n+1, 1):
            lefts = self.gen(m, i-1)
            rights = self.gen(i+1, n)

            for left in lefts:
                for right in rights:
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    nodes.append(node)
            
        return nodes 


# @lc code=end

