#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# Definition for a binary tree node.
# from typing import ByteString


# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# @lc code=start
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root = self.build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
        return root
    
    def build(self, inorder, istart, iend, postorder, pstart, pend):
        if pstart > pend:
            return None
        r = postorder[pend]
        idx = 0
        for i in range(istart, iend+1, 1) :
            if inorder[i]  == r:
                idx = i
                break
        leftsize = idx - istart
        left = self.build(inorder, istart, idx-1, postorder, pstart, pstart+leftsize-1)
        right = self.build(inorder, idx +1, iend, postorder, pstart+leftsize, pend-1)
        root = TreeNode(r, left, right)

        return root
        

# build(in, 0, 4, po, 0, 4)
# idx=1, leftsize = 1
# left=build(in, 0, 0, po, 0, 1)
# right = build(in, 2, 4, po, 1,3)

# @lc code=end

